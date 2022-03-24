from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
config_object["APPINFO"] = {
    "Symptom_version": "1.0.1",
    "Illness_version": "1.0.1"
}

config_object["APIINFO"] = {
    "JSON_URL": "https://illnesses-and-symptoms.herokuapp.com/"
}

config_object["SERVERCONFIG"] = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "medicalproject"
}

config_object["USERINFO"] = {
    "username": "",
    "role": ""
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)