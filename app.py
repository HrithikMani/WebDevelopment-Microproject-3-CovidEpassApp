from flask import Flask
from datetime import datetime
import re

import requests as re

app = Flask(__name__)


@app.route("/")
def fun():
    return "hi"


@app.route("/login", methods=['POST'])
def login():
    return "login"


@app.route("/signup", methods=['POST'])
def signup():
    return "Signing up"


# ---------------------------------------------------------------------------------------------

@app.route("/covid/", methods=['GET'])
def indiaNums():
    r = re.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = r.json()
    return dict(data["data"]["summary"])


@app.route("/covid/<state>", methods=['GET'])
def district(state):
    r = re.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = r.json()
    data = data["data"]["regional"]
    result = "None"
    for i in data:
        if(i["loc"] == state):
            result = i
            break
    return result


if __name__ == "__main__":
    app.run()
