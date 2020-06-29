from flask import Flask, request
import json
 
app = Flask(__name__)
 
@app.route('/remote', methods = ["POST"])
def parseRemoteJson():

    if (not request.is_json):
        print("Invalid JSON")
        return ''
    
    data = request.json;    
    printReceivedJson(data)
    
    return ''
    
def printReceivedJson(data):
    dict = {"application": "", "device": "", "commandType": "", "command": ""}
    
    for key in dict.keys():
        if(data.has_key(key)):
            dict[key] = data[key]
    
    print("JSON Object: " + json.dumps(data))
    
    for key in dict.keys():
        print(key + ": " + dict[key])
        
    return ''
 
app.run(host='0.0.0.0', port= 50505)