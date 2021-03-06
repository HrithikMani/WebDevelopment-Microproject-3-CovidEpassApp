from flask import Blueprint
import requests as re
covid = Blueprint("covid", __name__)
'''
{
  "active": 626192, 
  "deaths": 119538, 
  "recovered": 7198877, 
  "source": "covid19india.org", 
  "total": 7945975
}
'''
@covid.route("/", methods=['GET'])
def indiaNums():
    r = re.get("https://api.rootnet.in/covid19-in/stats/latest")
    data = r.json()
    res = {}
    res["total"] = data["data"]["summary"]["total"]
    res["recovered"] = data["data"]["summary"]["discharged"]
    res["deaths"] = data["data"]["summary"]["deaths"]
    res["active"] = data["data"]["unofficial-summary"][0]["active"]
    return res


@covid.route("state/<state>", methods=['GET'])
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
@covid.route("/region", methods=['GET'])
def region():
    r=re.get("https://api.rootnet.in/covid19-in/stats/latest")
    data=r.json()
    d={"data":(data["data"]["regional"])}

    return d



@covid.route("/cases", methods=['GET'])
def cases():
    r=re.get("https://api.rootnet.in/covid19-in/stats/history")
    data=r.json()
    res = []
    for i in range(len(data['data'])):
        tot = data['data'][i]["summary"]["total"]
        day = data['data'][i]["day"]
        res.append([day,tot])

    d={"data":res}

    return d


@covid.route("/deaths", methods=['GET'])
def deaths():
    r=re.get("https://api.rootnet.in/covid19-in/stats/history")
    data=r.json()
    res = []
    for i in range(len(data['data'])):
        tot = data['data'][i]["summary"]["deaths"]
        day = data['data'][i]["day"]
        res.append([day,tot])

    d={"data":res}

    return d
