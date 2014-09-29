__author__ = 'Amorim'

import sys
import requests
import time
import json
import argparse
import yaml
import getpass
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.internal.codec.xmlcodec import toXMLStr
from cobra.mit.request import ConfigRequest

from cobra.model.fv import Tenant

login_args = [{'name': 'host', 'help': 'APIC host name or IP'},
    {'name': 'user', 'help': 'User name'},
    {'name': 'password', 'help': 'User password'}
]
def input_tenant_name(msg='\nPlease input Tenant info:'):
    print msg
    return get_raw_input("Tenant Name (required): ", required=True)


def input_login_info(msg='\nPlease follow the wizard and finish the configuration.'):
    print msg
    print 'Login info:'
    return [get_raw_input("Host Name (required): ", required=True),
            get_raw_input("User Name (required): ", required=True),
            getpass.getpass("Password (required): ")]

def read_config_yaml_file(config_file, login_info=True):
    f = open(config_file, 'r')
    data = yaml.load(f)
    f.close()
    if login_info:
        return data, data['host'], data['user'], data['password']
    return data

def get_raw_input(prompt='', lower=False, required=False):
    r_input = raw_input(prompt).strip()
    if required and r_input == '':
        return get_raw_input(prompt, lower=lower, required=required)
    return r_input.lower() if lower else r_input

def set_cli_argparse(description, keys, opts=None, return_parser=False, login_info=True):
    if not opts: opts = []
    parser = argparse.ArgumentParser(description=description)
    if keys is None:
        return
    for arg in login_args:
        parser.add_argument(arg['name'], help=arg['help'])
    for key in keys:
        parser.add_argument(key['name'], help=key['help'])
    for opt in opts:
        opt['default'] = opt['default'] if 'default' in opt.keys() else None
        opt['dest'] = opt['dest'] if 'dest' in opt.keys() else opt['name']
        opt['choices'] = opt['choices'] if 'choices' in opt.keys() else None
        parser.add_argument('-'+opt['flag'], '--'+opt['name'],
                            dest=opt['dest'], default=opt['default'],
                            choices=opt['choices'], help=opt['help'])
    if return_parser:
        return parser
    args = vars(parser.parse_args())
    if login_info:
        return args.pop('host'), args.pop('user'), args.pop('password'), args
    return args

def commit_change(modir, changed_object):
    """Commit the changes to APIC"""
    config_req = ConfigRequest()
    config_req.addMo(changed_object)
    modir.commit(config_req)

def check_if_requesting_help(args, opt_args=None):
    return len(args) > 1 and args[1] in get_flag_names(opt_args)

def get_flag_names(args, opt_args=None):
    return len(args) > 1 and args[1] in get_flag_names(opt_args)

def print_query_xml(xml_file, pretty_print=True):
    print toXMLStr(xml_file, prettyPrint=pretty_print)

def apic_login_cobra(hostname, username, password):
    """Login to APIC"""
    lsess = LoginSession('http://'+hostname, username, password)
    modir = MoDirectory(lsess)
    modir.login()
    return modir

def LoginApicRequest(config):
    auth = {
        'aaaUser': {
            'attributes': {
                'name': config['name'],
                'pwd': config['passwd']
                }
            }
        }

    status = 0
    i=0
    cpt=0
    while( status != 200 ):
        url = 'http://%s/api/aaaLogin.json' % config['host']
        while(1):
            try:
                r = requests.post( url, data=json.dumps(auth), timeout=1 )

                break
            except Exception as e:
                i=i+1
                timeout(i, 100, "break")

        status = r.status_code
        FailureRequest(status)
    #   print status
    #   print r.text
        cookies = r.cookies
        time.sleep(1)
        cpt=cpt+1
        timeout(status, cpt, 100, "exit")
        return cookies

def timeout(status, cpt, time, output) :

    if status != 200:
        print("Problem status")

    if cpt==time and output=="exit" :
        print("program exit")
        sys.exit(0)

    if cpt==time and output=="break" :
        print("break")
        sys.exit(0)

def FailureRequest(status) :
    print(status)
    if status==201 :
        print("error 201 -> Created : An asynchronous task has been completed, and the object has been created.")

    if status==202 :
        print("error 202 -> Accepted : An asynchronous task has been accepted, but the processing is not complete.")

    if status==204 :
        print("error 204 -> Accepted but with no JSON body : An HTTP GET request is successful, but the response body does not have any data")

    if status==400 :
        print("error 400 -> Bad Request : An invalid request has been submitted. Verify that the request uses the correct syntax.")

    if status==401 :
        print("error 401 -> Unauthorized : The user is not authorized to invoke the request due to invalid authentication parameters, or lack of authority.")

    if status==404 :
        print("error 404 -> Not Found : The specified resource cannot be found.")

    if status==405 :
        print("error 405 -> Method not Allowed :  The HTTP verb entered is not allowed, such as a POST on a read-only resource.")

    if status==500 :
        print("error 500 -> Internal Server Error : The request failed, and no other information is available.")

    if status==503 :
        print("error 503 -> Service Unavailable : The service is not up due to internal maintenance or an outage.")

def input_key_args(msg='\nPlease specify the Physical Domain:'):
    print msg
    return get_raw_input("Physical Domain Name (required): ", required=True)

def print_query_xml(xml_file, pretty_print=True):
    print toXMLStr(xml_file, prettyPrint=pretty_print)

def input_key_args(msg='\nPlease specify the VLAN Pool identity:', from_delete_function=False):
    print msg
    args = []
    args.append(get_raw_input("VLan Name (required): ", required=True))
    args.append(get_optional_input("Allocation Mode (required) ", ['dynamic(d)', 'static(s)'], required=True))
    if not from_delete_function:
        args.append(get_raw_input("Vlan Range From (required): ", required=True))
        args.append(get_raw_input("Vlan Range To (required): ", required=True))
    print args
    return args

def get_optional_input(prompt, options, num_accept=False, required=False):
    try:
        opt_string = '/'.join(options)
    except NameError:
        opt_string = ''
    opt_string = '[' + opt_string + ']: ' if not opt_string == '' else ': '
    r_input = get_raw_input(prompt + opt_string)
    if r_input == '':
        if required:
            return get_optional_input(prompt, options, num_accept=num_accept, required=required)
        else:
            return r_input
    opt = [a for a in options if a.startswith(r_input)]
    if len(opt) > 0:
        opt = opt[0].split('(')
        opt = opt[0]
        return opt
    elif num_accept:
        try:
            return int(r_input)
        except ValueError:
            pass
    print 'Not appropriate argument, please try again.'
    get_optional_input(prompt, options, num_accept=num_accept, required=required)
