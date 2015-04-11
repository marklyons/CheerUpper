import json
import urllib2
from application_only_auth import Client
from metamind.api import ClassificationData, ClassificationModel, set_api_key

#twitter
API_KEY = "H5lXt22xepXuRUq2Y9zIFWyTk"
API_SECRET = "aj4PVeRsmRJjvqYPDO2Jk57qeeFkofWA4n3JQisEiCQQtD78JP"
client = Client(API_KEY, API_SECRET)
#meta mind
set_api_key("dEt77byHr0OuQpqmBbn6HycesPndJ77wMpwUKXudDznYZbf70e")
classifier = ClassificationModel(id=88)



# to be filled with all matched/possible statuses
master = {}
sentiments = ["sad", "depressed", "upset", "heartbroken"]
quants = ["", "really ", "very ", "extremely "]
me = ["I am ", "I'm ", "I'm feeling "]

sad_boys = []
for s in sentiments:
	for q in quants:
		for m in me:
			sad_boys.append(m + q + s)
i = 0
j = 0
for s in sad_boys:
	print "query#: " + str(i) + " Using: " + s
	query = urllib2.quote(s).encode("utf8")
	tweets = client.request('https://api.twitter.com/1.1/search/tweets.json?count=50&result_type=recent&q=' + "\"" + query + "\"")
	statuses = tweets["statuses"]
	i += 1
	for status in statuses: #iterating over tweets for specific sentiment
		print "status parse: " + str(j)
		j += 1
		if status["in_reply_to_status_id"] == None:
			curr_status = status["text"].encode('ascii', 'ignore')
			curr_id = status["id"]
			master[curr_status] = curr_id

#filter text
filtered_statuses = {}
for status in master.keys():
	if "#cheermeup" in status.lower():
		filtered_statuses[status] = master[status]
	elif "whenever i'm feeling" not in status.lower() and "when i'm feeling" not in status.lower() and not status.startswith("RT"):
		if "video" not in status.lower() and "@" not in status and "http" not in status.lower():
			if "if i'm feeling" not in status.lower(): 
				filtered_statuses[status] = master[status]

#filter positivity
#my_dataset = ClassificationData(private=True, data_type="text", name="Tweets")

i = 0
final_tweets = {}
for status in filtered_statuses.keys():
	i += 1
	if "#cheermeup" in status.lower():
		i -= 1
		final_tweets[status] = filtered_statuses[status]
	elif (classifier.predict(status, input_type='text'))[0]["label"] != "positive":
		final_tweets[status] = filtered_statuses[status]
	print "Query Meta# " + str(i)

#printing
i = 0
for status in final_tweets:
	i += 1
	print status + "\n"
print i
#final_tweets is a dictionary, the keys will be the most depressing of messages, and their value is the post's id #