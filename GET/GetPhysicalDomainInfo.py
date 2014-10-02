__author__ = 'Amorim'


from util import *
import sys
import requests
import json
from pprint import pprint

def RecupPhysicalDomainValues(data) :
    result=[]
    data=convert(data)
    imdata=data['imdata']
    for t in imdata :
        Stab=t['fvnsEncapBlk']
        for u in Stab :
            result.append(Stab['attributes']['name'])

    for j in imdata :
        StabBis=k['fvnsEncapBlk']
        for k in StabBis :
            result.append(StabBis['attributes']['name'])

    result.sort()
    return result

def GetPhDo(config, cookies):

    url='https://'+config['host']+'/api/node/mo/uni/infra.json?query-target=subtree&target-subtree-class=fvnsVlanInstP&target-subtree-class=fvnsEncapBlk&query-target=subtree'
    print '++++++++ REQUEST GET ++++++++'
    print url
    print '------------------------------'

    r = requests.get(url,cookies=cookies, verify=False)
    print r.status_code

    print '++++++++ RESPONSE GET ++++++++'
    pprint (convert(r.json()))
    print '-------------------------------'

    #return RecupPhysicalDomainValues(r.json())

def input_log_info() :
    config={}
    print('Please insert required informations')
    config['host']=raw_input("Host Name (required) :    ")
    config['name']=raw_input("User Name (required):     ")
    config['passwd']=raw_input("Password (required):    ")

    if config['host'] == None or config['name'] == None or config['passwd'] == None :
        print("Error parameter insertion")
        sys.exit(0)

    return config

if __name__ == '__main__':
    config={}
    try:
        config['host'] = sys.argv[1]
        config['name'] = sys.argv[2]
        config['passwd'] = sys.argv[3]

    except Exception as e:
        print str(e)
        config=input_log_info()

    cookies=LoginApicRequest(config)
    GetPhDo(config, cookies)