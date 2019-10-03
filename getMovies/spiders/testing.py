import requests
YOURAPIKEY="get_yours_😂😂"
payload = {'api_key': YOURAPIKEY, 'url':
'https://httpbin.org/ip'}

r = requests.get('http://api.scraperapi.com', params=payload)

print(r.text)