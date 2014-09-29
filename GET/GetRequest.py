__author__ = 'Amorim'


import xml.dom.minidom
import yaml
from util import *
import sys
import time
import requests
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant


def check_if_tenant_exist(modir, tenant_name):
    fv_tenant = modir.lookupByDn('uni/tn-' + tenant_name)
    if not isinstance(fv_tenant, Tenant):
        print 'Tenant', tenant_name, 'does not existed. \nPlease create a tenant.'
        sys.exit()
    else :
        print 'Tenant', tenant_name, 'exist.'
    return fv_tenant

def main() :
    try:
        cfgFile = sys.argv[1]
    except Exception as e:
        print str(e)
        sys.exit(0)

    with open( cfgFile, 'r' ) as config:
        config = yaml.safe_load( config )

    modir=apic_login_cobra(config['host'], config['name'], config['passwd'])
    result=check_if_tenant_exist(modir, "EDF003")

if __name__ == '__main__':
    main()







