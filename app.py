from flask import Flask, request
import json

app = Flask(__name__)

@app.post("/upgrdetime")
def create_store():
    request_data = request.get_json()
    print(request_data)
    f = open("demofile2.json", "a")
    f.write(json.dumps(request_data))
    f.close()
    return  "OK"