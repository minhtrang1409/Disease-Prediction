import urllib.request
import json
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

API_info = config_object["APIINFO"]

url = urllib.request.urlopen(API_info["JSON_URL"] + "version")
data = json.loads(url.read().decode('utf-8-sig'))

Version_info = config_object["APPINFO"]

def VersionCheck():
    for item in data['version']:
        if item['name'] == "Symptom":
            if item['version_number'] != Version_info["symptom_version"]:
                url_symptoms = urllib.request.urlopen(API_info["JSON_URL"] + "symptoms")
                content = json.loads(url_symptoms.read().decode('utf-8-sig'))
                f = open('Data/symptoms.json', 'w')
                json.dump(content, f, indent=4)

                Version_info["symptom_version"] = item['version_number']
                with open('config.ini', 'w') as conf:
                    config_object.write(conf)
        elif item['name'] == "Illness":
            if item['version_number'] != Version_info["illness_version"]:
                url_illnesses = urllib.request.urlopen(API_info["JSON_URL"] + "illnesses")
                content = json.loads(url_illnesses.read().decode('utf-8-sig'))
                f = open('Data/illnesses.json', 'w')
                json.dump(content, f, indent=4)

                Version_info["illness_version"] = item['version_number']
                with open('config.ini', 'w') as conf:
                    config_object.write(conf)