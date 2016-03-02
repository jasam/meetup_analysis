from flask import Flask, jsonify
from urllib.request import Request, urlopen
import json

app = Flask(__name__) 

@app.route('/dataScientists')
def dataScientistsFunction():
    scientists = []
    data_scientists = {}
    qx_data_scientist = 1063
    quantity_pages = qx_data_scientist / 20
    url = "https://api.import.io/store/connector/_magic?url=http%3A%2F%2Fwww.meetup.com%2FBig-Data-Science-Bogota%2Fmembers%2F%3Foffset%3D{}%26sort%3Djoin_date%26desc%3D1&format=JSON&js=false&_apikey=fd51ad66a13d44e1b94f624a191aa2073756fd91206e78e97b26a0898bc3ba7d6ae5bb415ca07421e4eb9dfda36ab684e1b106e7daa3fb9ae49b9b4352e4069ef8e6bc739b4b46b0438f251e1a1986fc"
    member_number = 0
    for i in range(0, int(quantity_pages) + 1):
        offset = i * 20 
        html = urlopen(url.format(offset)).read()
        data = json.loads(html.decode())
        for item in data["tables"]:
            for result in item["results"]:
                try:
                    data_scientists["name"] = result["memname_link/_text"]
                except KeyError:
                	data_scientists["name"] = ""
                try:
                    data_scientists["registration_date"] = result["joined_date/_source"]
                except KeyError:
                    data_scientists["registration_date"] = ""
                try:
                    data_scientists["role"] = result["resetlistblock_value"]
                except KeyError:
                    data_scientists["role"] = ""
                    
                member_number = member_number + 1
                data_scientists["member_number"] =  member_number

                scientists.append(data_scientists.copy())

    return jsonify(results=scientists)
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	


