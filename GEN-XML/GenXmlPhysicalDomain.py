__author__ = 'Amorim'

import sys


def WriteXmlPhysicalDomain(config) :
    FileXml=open("03-Physical-Domain-test.xml","w")
    TextPD ='''
<polUni>
      <physDomP name="'''+config['name']+'''">
         <infraRsVlanNs tDn="uni/infra/vlanns-QvPC_Pool-static"/>
      </physDomP>
</polUni>
'''
    FileXml.write(TextPD)
    FileXml.close()

def input_info() :
    config={}
    print('Please insert required informations')
    config['name']=raw_input("Physical Domain Name (required) :    ")

    if config['name'] == None  :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['name'] = sys.argv[1]

    except Exception as e:
        print str(e)
        config=input_info()
    WriteXmlPhysicalDomain(config)