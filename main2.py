import requests
import json
import conf

url="https://192.168.0.166"
recurso_api="/rest/ip/address"
a=1
respuesta = requests.get(url+"/rest/ip/address/*3",auth=(conf.user,conf.clave),verify=False)
print(respuesta.json())
print(json.dumps(respuesta.json(),indent=4))

respuesta2 = requests.get(url+"/rest/interface/ether1",auth=(conf.user,conf.clave),verify=False)
print(json.dumps(respuesta2.json(), indent=4))

# Extrayendo IP:
# print("IP: ",respuesta.json()["actual-interface"]+" || "+respuesta.json()["address"])