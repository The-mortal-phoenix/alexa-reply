import requests
from urllib.parse import quote

def reply(msg:str, name:str, dev:str):
	urlled = quote(msg)
	ownern = quote(dev)
	botd = quote(name)

	url = f"https://api.affiliateplus.xyz/api/chatbot?message={urlled}&botname={botd}&ownername={ownern}&user=1"
	resp = requests.get(url = url)

	jso = resp.json()
	reply = jso['message']

	return reply