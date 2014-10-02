__author__ = 'Amorim'

import sys

def  WriteXmlAppEPG(config):

    FileXml=open("06-Application-Profile-EPG-test.xml","w")
    TextBD ='''
<polUni>
	<fvTenant name="'''+config['tenant']+'''">
        <fvAp name="'''+config['app']+'''">
			<fvAEPg name="'''+config['epg']+'''">
				<fvRsBd tnFvBDName="'''+config['bridge']+'''"/>
				<fvRsPathAtt encap="'''+config['vlan']+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/3]"/>
				<fvRsPathAtt encap="'''+config['vlan']+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-102/pathep-[eth1/3]"/>
				<fvRsPathAtt encap="'''+config['vlan']+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-103/pathep-[eth1/3]"/>
			</fvAEPg>
		</fvAp>
	</fvTenant>
</polUni>
'''
    FileXml.write(TextBD)
    FileXml.close()

def input_info() :
    config={}
    print('Please insert required informations')
    config['tenant']=raw_input("Tenant Name (required) :")
    config['app'] = raw_input("Application Profile Name (required) :")
    config['epg'] = raw_input("EPG Name (required) :")
    config['vlan'] = raw_input("Vlan Name (required) :")
    config['bridge'] = raw_input("Bridge Domain (required) :")

    if config['tenant'] == None or config['app'] == None or config['epg'] == None or config['vlan'] == None or config['bridge'] == None :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['tenant'] = sys.argv[1]
        config['app'] = sys.argv[2]
        config['epg'] = sys.argv[3]
        config['vlan'] = sys.argv[4]
        config['bridge'] = sys.argv[5]

    except Exception as e:
        print str(e)
        config=input_info()
    WriteXmlAppEPG(config)