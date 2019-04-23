from django.shortcuts import render

def home(request):
	import requests
	import json
	API_KEY = "c372b5f5d7d17814dc34b99ccf63bc07a31334c3dea7a518ac04d663eb1956de" # this contains our API Key

	# FETCH CRYPTO PRICE DATA
	api_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR" +"&api_key=" +API_KEY)
	api = json.loads(api_request.content) # read our json
	# FETCH CRYPTO NEWS
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN" +"&api_key=" +API_KEY)
	api = json.loads(api_request.content) # read our json
	return render(request,'home.html', {'api' : api})
