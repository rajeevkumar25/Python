import requests
import json

def getExchangeRateDatainINR():
	api_url='http://api.fixer.io/latest?base=INR'
	api_data=requests.get(api_url)
	
	if(api_data.ok):
		for item in api_data.json():
			print(item)


k=getExchangeRateDatainINR()
print(k)
