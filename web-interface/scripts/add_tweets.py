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
	final_string = base_string + sentiment + ":( \""
	query = urllib2.quote(final_string).encode("utf8")

	tweets = client.request('https://api.twitter.com/1.1/search/tweets.json?count=100&result_type=recent&q=' + query)
	statuses = tweets["statuses"]
<<<<<<< HEAD
	for status in statuses:
		print status.keys()
		curr_status = status["text"].encode('ascii', 'ignore')

		#logic for deciding whether it is good or not
		if(True):
			final_statuses.append(curr_status)
			curr_status + "\n"
=======
	for status in statuses: #iterating over tweets for specific sentiment
		if status["in_reply_to_status_id"] == None:
			curr_status = status["text"].encode('ascii', 'ignore')
			final_statuses.append(curr_status)
>>>>>>> 42f1bc8531eb405f62727564bba2d7f13e43436b

filtered_statuses = []
for status in final_statuses:
	if "#cheermeup" in status.lower():
		filtered_statuses.append(status)
	elif "whenever i'm feeling" not in status.lower() and "when i'm feeling" not in status.lower() and not status.startswith("RT"):
		if "video" not in status.lower() and "@" not in status and "http" not in status.lower():
			if "if i'm feeling" not in status.lower(): 
				filtered_statuses.append(status)

#printing
for status in filtered_statuses:
	print status + "\n"


