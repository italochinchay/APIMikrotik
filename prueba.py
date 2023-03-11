ip_address=["192.168.1.10","192.168.1.11","192.168.1.12"]
comandos = ["sh version","sh running-config","sh ip interface brief"]

print("N°   IP")
i=1
for ip,comando in zip(ip_address,comandos):
    print(str(i)+"   "+ip)
    print("   comando:    "+comando)
    i=i+1
