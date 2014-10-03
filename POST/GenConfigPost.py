__author__ = 'Amorim'

import sys


def WriteConfigRequest(config):
    FileXml=open("request-test.cfg","w")



    FileXml.close()


def input_info() :
    config={}
    print('Please insert required informations')
    config['host']=raw_input("Host Name (required) :    ")
    config['name']= raw_input("Login (required) :         ")
    config['passwd']=raw_input("Password (required) : ")
    config['test']['type'] =raw_input("Type File (required) : ")
    config['test']['path'] =raw_input("Path (required) : ")
    config['test']['file'] =raw_input("File Name (required) : ")
    config['test']['wait'] =raw_input("Wait (required) : ")

    if config['host'] == None or config['name'] == None or config['passwd'] == None or config['test']['type'] == None or config['test']['path'] == None or config['test']['file'] == None or config['test']['wait'] == None:
        print("Error parameter insertion")
        sys.exit(0)
    return config

if __name__ == '__main__':
    config={}
    try:
        config['host'] = sys.argv[1]
        config['name'] = sys.argv[2]
        config['passwd'] = sys.argv[3]
        config['test']['type'] = sys.argv[4]
        config['test']['path'] = sys.argv[5]
        config['test']['file'] = sys.argv[6]
        config['test']['wait'] = sys.argv[7]
    except Exception as e:
        print str(e)
        config=input_info()
    WriteConfigRequest(config)
