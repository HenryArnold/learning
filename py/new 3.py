import json
from urllib.request import urlopen

def getCountry(ipAddress):
	response = urlopen("http://ip.taobao.com/service/getIpInfo.php?ip="+ipAddress).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson.get("contry")
	
print(getCountry("50.78.253.58"))