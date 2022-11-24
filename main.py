import requests
import json

def loadintojson(text):
    loadedjson = json.loads(text)
    return loadedjson

def get(url):
    r = requests.get(url)
    return r

def returnrequesttext(response, convert_to_json: bool):
    r = response
    rt = r.text
    return rt

def getalphabet():
    get("")