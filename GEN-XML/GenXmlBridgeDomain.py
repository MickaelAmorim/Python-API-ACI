__author__ = 'Amorim'

import sys


def WriteXmlPhysicalDomain(config) :
    FileXml=open("05-Bridge-Domain-test.xml","w")
    TextBD ='''
<polUni>
	<fvTenant name="'''+config['tenant']+'''">
		<fvCtx name="'''+config['Namectx']+'''"/>
		<fvBD arpFlood="yes" name="'''+config['bridge']+'''">
			<fvRsCtx tnFvCtxName="'''+config['Namectx']+'''"/>
			<fvSubnet ip="'''+config['subnet']+'''"/>
		</fvBD>
	</fvTenant>
</polUni>
'''
    FileXml.write(TextBD)
    FileXml.close()

def input_info() :
    config={}
    print('Please insert required informations')
    config['tenant']=raw_input("Tenant Name (required) :")
    config['bridge'] = raw_input("Bridge Domain Name (required) :")
    config['Namectx'] = raw_input("Private Network Name (required) :")
    config['subnet'] = raw_input("Subnet (required) :")

    if config['tenant'] == None or config['bridge'] == None or config['Namectx'] == None or config['subnet'] == None :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['tenant'] = sys.argv[1]
        config['bridge'] = sys.argv[2]
        config['Namectx'] = sys.argv[3]
        config['subnet'] = sys.argv[4]

    except Exception as e:
        print str(e)
        config=input_info()
    WriteXmlPhysicalDomain(config)