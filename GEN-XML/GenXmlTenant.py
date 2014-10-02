__author__ = 'Amorim'


import sys


def WriteXmlTenant(config):
    FileXml=open("01-Tenant-test.xml","w")

    TextTenant = '''
<polUni>
	<fvTenant name="'''+config['fvTenant']+'''">
		<fvCtx name="'''+config['fvCtx']+'''"/>
'''

    FileXml.write(TextTenant)
    print("Please insert Bridge Domain name :")
    for i in range(0, int(config['NumberBD'])):
        BridgeName=raw_input("Bridge Domain Name N"+str(i+1)+" :")
        IpSubnet=raw_input("Subnet : ")
        TextSubnet='''
            <fvBD arpFlood="yes" name="'''+BridgeName+'''">
			    <fvRsCtx tnFvCtxName="'''+config['fvCtx']+'''"/>
			    <fvSubnet ip="'''+IpSubnet+'''"/>
		    </fvBD>'''
        FileXml.write(TextSubnet)
        TextAPBegin='''
            <fvAp name="'''+config['fvAp']+'''">
        '''
    FileXml.write(TextAPBegin)

    for j in range(0,int(config['NumberBD'])) :
        EPGName=raw_input('EPG Name : ')
        BridgeName=raw_input('Bridge Domain Name N'+str(j+1)+' : ')
        VlanName=raw_input('Vlan Name : ')

        TextApp='''
        		<fvAEPg name="'''+EPGName+'''">
				    <fvRsBd tnFvBDName="'''+BridgeName+'''"/>
				    <fvRsPathAtt encap="'''+VlanName+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-101/pathep-[eth1/3]"/>
				    <fvRsPathAtt encap="'''+VlanName+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-102/pathep-[eth1/3]"/>
				    <fvRsPathAtt encap="'''+VlanName+'''" instrImedcy="immediate" tDn="topology/pod-1/paths-103/pathep-[eth1/3]"/>
			    </fvAEPg>
        '''
        FileXml.write(TextApp)
    TextEnd='''
    		</fvAp>
	</fvTenant>
</polUni>
    '''
    FileXml.write(TextEnd)
    FileXml.close()


def input_info() :
    config={}
    print('Please insert required informations')
    config['fvTenant']=raw_input("fvTenant Name (required) :    ")
    config['fvCtx']= raw_input("fvCtx Name (required) :         ")
    config['NumberBD']=raw_input("Number Bridge Domain (required) : ")
    config['To']=raw_input("range to (required) :       ")
    config['From']=raw_input("Range from (required) :   ")
    config['fvAp']=raw_input("fvAp Name (required) :    ")

    if config['fvTenant'] == None or config['fvCtx'] == None or config['NumberBD'] == None or config['To'] == None or config['From'] == None or config['fvAp'] == None :
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['fvTenant'] = sys.argv[1]
        config['fvCtx'] = sys.argv[2]
        config['NumberBD'] = sys.argv[3]
        config['To']=sys.argv[4]
        config['From']=sys.argv[5]
        config['fvAp']=sys.argv[6]

    except Exception as e:
        print str(e)
        config=input_info()
    WriteXmlTenant(config)