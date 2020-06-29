from flask import Flask, request
import json
 
flask = Flask(__name__)
APP_NAME = "remote"
PORT = 50505
 
@flask.route('/remote', methods = ["POST"])
def parseRemoteJson():

    if (not request.is_json):
        print("Invalid JSON")
        return ''
    
    data = request.json;    
    printReceivedJson(data)
    
    return ''
    
def printReceivedJson(data):
    dict = {"app_name": "", "device": "", "actionType": "", "action": ""}
    
    for key in dict.keys():
        if(data.has_key(key)):
            dict[key] = data[key]
            
    if (dict["app_name"] != APP_NAME):
        print("Request Unhandled")
        return ''
    
    print("JSON Object: " + json.dumps(data))
    
    for key in dict.keys():
        print(key + ": " + dict[key])
        
    return ''
 
flask.run(host='0.0.0.0', port= PORT)