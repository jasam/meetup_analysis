from flask import Flask, jsonify
from urllib.request import Request, urlopen
import json

app = Flask(__name__) 


@app.route('/dataScientists')
def dataScientistsFunction():
    scientists = []
    data_scientists = {}
    url = "https://api.import.io/store/connector/_magic?url=http%3A%2F%2Fwww.meetup.com%2Fes-ES%2FBig-Data-Science-Bogota%2Fmembers%2F&format=JSON&js=false&_apikey=fd51ad66a13d44e1b94f624a191aa2073756fd91206e78e97b26a0898bc3ba7d6ae5bb415ca07421e4eb9dfda36ab684e1b106e7daa3fb9ae49b9b4352e4069ef8e6bc739b4b46b0438f251e1a1986fc"
    html = urlopen(url).read()
    data = json.loads(html.decode())
    for item in data["tables"]:
        for result in item["results"]:
            data_scientists["name"] = result["memname_link/_text"]
            try:
                data_scientists["registration_date"] = result["resetlisttext_value"]
            except KeyError:
                data_scientists["registration_date"] = ""
            try:
                data_scientists["role"] = result["resetlistblock_value"]
            except KeyError:
                data_scientists["role"] = ""
            
            scientists.append(data_scientists.copy())

    return jsonify(results=scientists)
    
@app.route('/readHello')
def getRequestHello():
	return "Hi, I got your GET Request!"   
  
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	


