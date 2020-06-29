from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/remote', methods = ["POST"])
def consoleReport():
 
    print("Received: " + request.data)
    return ''
 
app.run(host='0.0.0.0', port= 50505)
