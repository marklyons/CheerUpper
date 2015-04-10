import json
from application_only_auth import Client

API_KEY = "H5lXt22xepXuRUq2Y9zIFWyTk"
API_SECRET = "aj4PVeRsmRJjvqYPDO2Jk57qeeFkofWA4n3JQisEiCQQtD78JP"

client = Client(API_KEY, API_SECRET)

# Sort of just for usage example
tweet = client.request('https://api.twitter.com/1.1/search/tweets.json?q=feeling')
print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':'))

