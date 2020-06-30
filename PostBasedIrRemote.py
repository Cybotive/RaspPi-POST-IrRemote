from flask import Flask, request
import json
import os
 
flask = Flask(__name__)
APP_NAME = "remote"
PORT = 50505

device_codes = {
    "source_box": {"remote_name": "YN-02_SourceBox", "source": {"1": "SOURCE_1", "2": "SOURCE_2", "3": "SOURCE_3", "4": "SOURCE_4", "5": "SOURCE_5"}}
}
 
@flask.route('/remote', methods = ["POST"])
def parseRemoteJson():
    variables = {"app_name": "", "device": "", "action_type": "", "action": ""}

    if (not request.is_json):
        print("Invalid JSON")
        return ''
    
    data = request.json
    
    for key in variables.keys():
        if(key in data):
            variables[key] = data[key]
            
    if (variables["app_name"] != APP_NAME):
        print("Request Unhandled")
        return ''
    
    #Uncomment Below During Development
    printJson(variables)
    
    sendIrCommand(variables)
    
    return ''
    
def printJson(data):
    print("JSON Object: " + json.dumps(data))
    
    for key in data.keys():
        print(key + ": " + data[key])
        
    return ''

def sendIrCommand(cmdJson):
    try:
        device = cmdJson["device"]
        action_type = cmdJson["action_type"]
        action = cmdJson["action"]
        
        codeDict = device_codes[device]
        remote_name = codeDict["remote_name"]
        command = codeDict[action_type][action]
        
        system_command = "irsend SEND_ONCE {0} {1}".format(remote_name, command)
        
        print("Sending Command: " + system_command)
        os.system(system_command)
        
        return True
    except KeyError as e:
        print("Unknown Command")
    
    return False
 
flask.run(host='0.0.0.0', port= PORT)
