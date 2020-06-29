from flask import Flask, request
import json
 
flask = Flask(__name__)
APP_NAME = "remote"
PORT = 50505
 
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
    
    return ''
    
def printJson(data):
    print("JSON Object: " + json.dumps(data))
    
    for key in data.keys():
        print(key + ": " + data[key])
        
    return ''
 
flask.run(host='0.0.0.0', port= PORT)
