from django.shortcuts import render

def home(request):
	import requests
	import json
	API_KEY = "c372b5f5d7d17814dc34b99ccf63bc07a31334c3dea7a518ac04d663eb1956de" # this contains our API Key

	# FETCH CRYPTO PRICE DATA
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD" +"&api_key=" +API_KEY)
	price = json.loads(price_request.content) # read our json
	# FETCH CRYPTO NEWS
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN" +"&api_key=" +API_KEY)
	news = json.loads(news_request.content) # read our json
	return render(request,'home.html', {'news' : news, 'price':price })
