from flask import Blueprint
import requests as re
covid = Blueprint("covid", __name__)


@covid.route("/", methods=['GET'])
def indiaNums():
    r = re.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = r.json()
    return dict(data["data"]["summary"])


@covid.route("/<state>", methods=['GET'])
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
