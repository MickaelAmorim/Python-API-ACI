__author__ = 'Amorim'

import sys
import re
import yaml
import argparse
import getpass
from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant
from cobra.internal.codec.xmlcodec import toXMLStr

def apic_login(hostname, username, password):
    """Login to APIC"""
    lsess = LoginSession('https://'+hostname, username, password)
    modir = MoDirectory(lsess)
    modir.login()
    return modir

def commit_change(modir, changed_object):
    """Commit the changes to APIC"""
    config_req = ConfigRequest()
    config_req.addMo(changed_object)
    modir.commit(config_req)

def check_if_tenant_exist(modir, tenant_name):
    fv_tenant = modir.lookupByDn('uni/tn-' + tenant_name)
    if not isinstance(fv_tenant, Tenant):
        print ('Tenant', tenant_name, 'does not existed. \nPlease create a tenant.')
        sys.exit()
    return fv_tenant

def input_tenant_name(msg='\nPlease input Tenant info:'):
    print msg
    return get_raw_input("Tenant Name (required): ", required=True)

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