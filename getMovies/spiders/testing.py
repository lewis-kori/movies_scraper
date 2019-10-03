import requests
YOURAPIKEY="3cc9724b88e8270117050243d5142488"
payload = {'api_key': YOURAPIKEY, 'url':
'https://httpbin.org/ip'}

r = requests.get('http://api.scraperapi.com', params=payload)

print(r.text)