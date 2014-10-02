__author__ = 'Amorim'

from util import *
import sys

from cobra.model.fv import Tenant


def check_if_tenant_exist(modir, tenant_name):
    fv_tenant = modir.lookupByDn('uni/tn-' + tenant_name)
    if not isinstance(fv_tenant, Tenant):
        print 'Tenant', tenant_name, 'does not existed. \nPlease create a tenant.'
        sys.exit()
    else :
        print 'Tenant', tenant_name, 'exist.'
    return fv_tenant


def input_log_info() :
    config={}
    print('Please insert required informations')
    config['host']=raw_input("Host Name (required) :    ")
    config['name']=raw_input("User Name (required):     ")
    config['passwd']=raw_input("Password (required):    ")
    config['tenant']=raw_input("Tenant Name (required): ")

    if config['host'] == None or config['name'] == None or config['passwd'] == None or config['tenant'] == None :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':

    config=input_log_info()
    modir=apic_login_cobra(config['host'], config['name'], config['passwd'])
    result=check_if_tenant_exist(modir, config['tenant'])






