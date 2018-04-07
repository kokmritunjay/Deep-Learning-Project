import tweepy
import csv 
import re
import json
import time
from itertools import izip_longest
## Authentication key for using tweepy API ##
consumer_key="VccJhqJ73R467yIjNrzs48hJh"
consumer_secret="fEpcvcPx33QofnDmCIIl4bnljtTZz2Kr1jKK7WGvznsEc1h3OO"
access_token="731378512129466368-qjPZEXIYfIouvJOySFAWBJOLzBJwYpw"
access_secret="gePcxQNKRManF3Iay1TwVYbiKoWYXhNfLPefi9RItNyxV"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# FUNCTION TO REMOVE THE PUNCTUATION PRESENT IN THE TWEET TEXT ##########
def removepunc(s):
        #URLless_string =
        re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+","", s)
        punctuations = """-[]{}""\,<>./?$%^&*_~"""
        no_punct = ""
        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char
        return no_punct

def wordcount(word_list, a_string):
    return set(word_list).intersection(a_string.split())

fo=open("/home/shalini.pcs16/btp/new.txt","a")
foi=open("/home/shalini.pcs16/btp/images.txt","a")

def function(j):
    for tweet in tweepy.Cursor(api.search,
                           q=j,
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
        fo.write(str(tweet.id_str))##### store tweet id
	fo.write(",")
        fo.write(str(tweet.created_at))###### time stamp at which tweet is created at
	fo.write(",")

        a=removepunc(str(tweet.text.encode("utf-8")))   ###### store the tweet text
        text=" ".join(a.split())

	

        fo.write(text)
	fo.write(",")

        fo.write(str(tweet.favorite_count))  ####### no of favorite count of the tweet
	fo.write(",")

        fo.write(str(tweet.retweet_count))    ### re-tweet count of the tweet
	fo.write(",")

        fo.write(str(tweet.user.screen_name))     ###### user name who have done that tweet
	fo.write(",")

        fo.write(str(tweet.user.friends_count))  ##### users friends count
	fo.write(",")

        fo.write(str(tweet.user.followers_count)) 
	fo.write(",")

	if 'media' in tweet.entities:
		#print "media found"
            	for image in  tweet.entities['media']:
                	fo.write(image['media_url'])
			fo.write(",")
			foi.write(image['media_url'])
			foi.write("\n")

        else: 
		fo.write(str("no media"))
		fo.write(",")


	strht=""
	if 'hashtags' in tweet.entities:
            	for ht in tweet.entities['hashtags']:
			strht=strht+ht['text'].encode("utf-8")+" "
		if strht:
			fo.write(strht)
			fo.write(",")

		if not strht:
			fo.write("no hashtags")
			fo.write(",")

		if "follow" in strht or "mustfollow" in strht or "teamfollowback" in strht or "ff" in strht :
			fo.write("true")
			fo.write(",")

		else:
			fo.write("false")
			fo.write(",")

        
	
	stru=""
	if 'urls' in tweet.entities:
            	for url in  tweet.entities['urls']:
                	stru=stru+url['url']+" "
		if stru:
			fo.write(stru)
			fo.write(",")

        	if not stru: 
			fo.write(str("no urls"))
			fo.write(",")


	strum=""
	if 'user_mentions' in tweet.entities:
            	for user in  tweet.entities['user_mentions']:
                	strum=strum+(user['screen_name'])+" "	
		if strum:
			fo.write(strum)
			fo.write(",")

		if not strum:
			fo.write(str("no user_mentions"))
			fo.write(",")

	fo.write(str(len(wordcount(keyword_list,text))))
	fo.write("\n")


              
keyword_list=["al-Qaeda","taliban",'Lashkar-E-Taiba', 'acuteness', 'agitation', 'anarchism', 'anarchy', 'annihilate', 'asphyxiate', 'assassinate', 'assault', 'atom bomb', 'attack', 'bestiality', 'bloodshed', 'blowup', 'bomb', 'bombshell', 'brawl', 'brutality', 'brute force', 'bustle', 'chaos', 'charge', 'clamor', 'clash', 'coercion', 'complication', 'compulsion', 'confusion', 'constraint', 'convulsion', 'crime', 'criminal', 'crucify', 'cruelty', 'destructiveness', 'destryo', 'device', 'discombobulation', 'discord', 'disorder', 'disorganization', 'dispatch', 'distemper', 'disturbance', 'dither', 'do away with', 'do in', 'drown', 'dump', 'duress', 'electrocute', 'entanglement', 'eradicate', 'erase', 'execute', 'explosive', 'exterminate', 'extirpate', 'ferocity', 'fervor', 'fierceness', 'fight', 'fighting', 'finish', 'flap', 'foul play', 'fracas', 'frenzy', 'fury', 'fuss', 'garrote', 'get', 'grenade', 'guillotine', 'gun', 'hang', 'harshness', 'hit', 'horror', 'hubbub', 'hullabaloo', 'hydrogen bomb', 'imbroglio', 'immolate', 'insurgency', 'insurrection', 'isis', 'islam', 'jihad', 'jihadi', 'kill', 'lawlessness', 'liquidate', 'lynch', 'massacre', 'mayhem', 'mine', 'misrule', 'missile', 'mob rule', 'molotov cocktail', 'murder', 'murderousness', 'muslim', 'neutralize', 'nuclear bomb', 'obliterate', 'off', 'onslaught', 'passion', 'poison', 'polish off', 'power', 'projectile', 'put away', 'put to death', 'quarrel', 'raging', 'rampage', 'rebellion', 'reign of terror', 'revolution', 'riot', 'rioting', 'rocket', 'roughness', 'rub out', 'ruckus', 'rumble', 'rumpus', 'sacrifice', 'savagery', 'severity', 'sharpness', 'shell', 'slaughter', 'slay', 'smother', 'snuff', 'static', 'storm', 'storminess', 'strangle', 'strike', 'struggle', 'suffocate', 'suicide', 'terror', 'terrorism', 'threat', 'ticker', 'tizzy', 'torpedo', 'trouble', 'tumult', 'turbulence', 'turmoil', 'unrest', 'unruliness', 'uproar', 'vehemence', 'violence', 'violent', 'waste', 'wildness', 'wipe out', 'x-out', 'zap']

print("searching for tweets")
for i in keyword_list:
    function(i)     ######### CALL THE FUNCTION function() AND STORE ALL THE REQUIRED INFORMATION
    #print(".")
    
    
