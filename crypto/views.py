from django.shortcuts import render

def home(request):
	import requests
	import json
	API_KEY = "c372b5f5d7d17814dc34b99ccf63bc07a31334c3dea7a518ac04d663eb1956de" # this contains our API Key
	api_request = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR" +"&api_key=" +API_KEY)
	api = json.loads(api_request.content) # read our json
	return render(request,'home.html', {'api' : api})
