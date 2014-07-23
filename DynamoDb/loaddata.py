'''
Name: Angel Romero 10001044475
	  Md Merajul Islam 1000865420
Course Number: CSE 6331 Cloud Computing
Lab: Assignment 3 Part 2
 
'''
import boto.dynamodb
from datetime import datetime

#get start time
start = datetime.now()

#connect using boto to dynamodb 
conn = boto.dynamodb.connect_to_region('us-west-2')

#open Dynamodb table
table = conn.get_table('importdata')

#read csv dataset
fileR = open('importdata.csv', 'r')
#loop through the data
i=1
for line in fileR:
 s=line.split(",")
 #set the item data
 item_data={
	'image_id':s[0],
	'unixtime':s[1],
	'rawtime':s[2],
	'title':s[3],
	'total_votes':s[4],
	'reddit_id':s[5],
	'upvotes':s[6],
	'subreddit':s[7],
	'downvotes':s[8],
	'localtime':s[9],
	'score':s[10],
	'num_comments':s[11],
	'username':s[12],}
 #insert new item with its hash key attribute
 item=table.new_item(hash_key=i, attrs=item_data)
 item.put()
 print i, item_data
 i = i + 1

fileR.close()
#get final time
final=datetime.now()
#print timing details
print "initial time:", str(start)
print "final time:",  str(final)
print "elapsed Time:",  str(final - start)