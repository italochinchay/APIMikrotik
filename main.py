import requests
import json
import conf

url="https://192.168.5.67"
recurso_api="/rest/ip/address"

repuesta = requests.get(url+recurso_api,auth=(conf.user,conf.clave),verify=False)
print(repuesta.json())

