__author__ = 'Amorim'

#!/usr/bin/python

import xml.dom.minidom
import yaml
from util import *
import sys
import time
import requests

def post_type_file(package,url,file, cookies) :
    print 'url is (%s)' %url

    r = requests.post( url,cookies=cookies, files={'file':package} )

    result = xml.dom.minidom.parseString( r.text )
    status = r.status_code

    print '++++++++ RESPONSE (%s) ++++++++' % file
    print result.toprettyxml()
    print '-------------------------------' % file
    print status

def post_type_xml(package, url,file, config, cookies) :

    data = package.read()
    print '++++++++ REQUEST (%s) ++++++++' % file
    print data
    print '------------------------------'

    url = 'http://%s/api/node/mo/.xml' % config['host']
    r = requests.post( url,cookies=cookies,data=data )
    result = xml.dom.minidom.parseString( r.text )
    status = r.status_code

    print '++++++++ RESPONSE (%s) ++++++++' % file
    print result.toprettyxml()
    print '-------------------------------'
    print status

def post_runConfig( config, cookies):
    tests = config['tests']
    for t in tests:
        type = t['type']
        url = 'https://%s/%s' % (config['host'],t['path'])
        file = t['file']

        with open(file,'r') as package:
            if('wait' in t):
                time.sleep( t['wait'] )
            else:
                raw_input( 'Hit return to upload %s' % file )

            if type=='file':
                post_type_file(package, url,file, cookies)

            elif type=='xml':

                post_type_xml(package, url, file, config, cookies)
            else:
                print 'Unknown type:', type

def main() :
    try:
        cfgFile = sys.argv[1]
    except Exception as e:
        print str(e)
        sys.exit(0)

    with open( cfgFile, 'r' ) as config:
        config = yaml.safe_load( config )

    cookies=LoginApicRequest(config)
    #cookies=apic_login(config['host'], config['name'], config['passwd'])
    #print(cookies)
    post_runConfig(config, cookies )

if __name__ == '__main__':
    main()
