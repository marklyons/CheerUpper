import json
import urllib2
from application_only_auth import Client

API_KEY = "H5lXt22xepXuRUq2Y9zIFWyTk"
API_SECRET = "aj4PVeRsmRJjvqYPDO2Jk57qeeFkofWA4n3JQisEiCQQtD78JP"

client = Client(API_KEY, API_SECRET)

final_statuses = [] # to be filled with all matched/possible statuses
sentiments = ["sad", "depressed", "down", "really sad", "upset", "heartbroken"]

base_string = "\"I'm feeling "
for sentiment in sentiments:
	final_string = base_string + sentiment + "\""
	print final_string
	query = urllib2.quote(final_string).encode("utf8")

	tweets = client.request('https://api.twitter.com/1.1/search/tweets.json?count=5&q=' + query)
	statuses = tweets["statuses"]
	for status in statuses:
		print status.keys()
		curr_status = status["text"].encode('ascii', 'ignore')

		#logic for deciding whether it is good or not
		if(True):
			final_statuses.append(curr_status)
			curr_status + "\n"



