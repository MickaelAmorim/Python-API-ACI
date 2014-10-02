__author__ = 'Amorim'

import sys

def WriteXmlPool(config) :
    FileXml=open("02-Pool-test.xml","w")

    TextEdit='''
<polUni>
   <infraInfra dn="uni/infra">
      <fvnsVlanInstP allocMode="'''+config['alloMode']+'''" name="'''+config['name']+'''">
         <fvnsEncapBlk from="'''+config['From']+'''" to="'''+config['To']+'''"/>
      </fvnsVlanInstP>
   </infraInfra>
</polUni>
    '''
    FileXml.write(TextEdit)
    FileXml.close()

def input_info() :
    config={}
    print('Please insert required informations')
    config['alloMode']=raw_input("alloMode Name (required) :    ")
    config['name']= raw_input("Pool Name (required) :         ")
    config['From']=raw_input("From Vlan (required) : ")
    config['To']=raw_input("To Vlan (required) :       ")

    if config['alloMode'] == None or config['name'] == None or config['From'] == None or config['To'] == None  :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['alloMode'] = sys.argv[1]
        config['name'] = sys.argv[2]
        config['From'] = sys.argv[3]
        config['To']=sys.argv[4]

    except Exception as e:
        print str(e)
        config=input_info()
    WriteXmlPool(config)