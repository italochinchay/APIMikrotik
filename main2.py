import requests
import json
import conf

url="https://192.168.5.67"
recurso_api="/rest/ip/address"
a=1
respuesta = requests.get(url+recurso_api,auth=(conf.user,conf.clave),verify=False)
print(respuesta.json())

# Extrayendo IP:
print("IP: ",respuesta.json()[0]["actual-interface"]+" || "+respuesta.json()[0]["address"])