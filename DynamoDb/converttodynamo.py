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
#output file for JSON like output file
fileW = open('dynamodata.json','w')
#loop through the data
i=1
for line in fileR:
 s=line.split(",")
 #set the item data
 dynamo_dataformat=(
	"image_id\x03{\"s\":\""+s[0]+"\"}"+
	"\x02unixtime\x03{\"s\":\""+s[1]+"\"}"+
	"\x02rawtime\x03{\"s\":\""+s[2]+"\"}"+
	"\x02title\x03{\"s\":\""+s[3]+"\"}"+
	"\x02total_votes\x03{\"s\":\""+s[4]+"\"}"+
	"\x02reddit_id\x03{\"s\":\""+s[5]+"\"}"+
	"\x02upvotes\x03{\"s\":\""+s[6]+"\"}"+
	"\x02subreddit\x03{\"s\":\""+s[7]+"\"}"+
	"\x02downvotes\x03{\"s\":\""+s[8]+"\"}"+
	"\x02localtime\x03{\"s\":\""+s[9]+"\"}"+
	"\x02score\x03{\"s\":\""+s[10]+"\"}"+
	"\x02num_comments\x03{\"s\":\""+s[11]+"\"}"+
	"\x02username\x03{\"s\":\""+s[11]+"\"}"+
	"\x02id\x03{\"n\":\""+str(i)+"\"}"+
	"\n") #line feed ascii
 #write output to n)e file
 #print "".join(dynamo_dataformat)
 print dynamo_dataformat
 fileW.write(dynamo_dataformat)
 i = i + 1

fileR.close()
fileW.close()
#get final time
final=datetime.now()
#print timing details
print "initial time:", str(start)
print "final time:",  str(final)
print "elapsed Time:",  str(final - start)

#Sample export format
#localtime{"s":"1330612767"}unixtime{"s":"1330587567"}reddit_id{"s":"qdhjk"}
#score{"s":"361"}downvotes{"s":"469"}total_votes{"s":"1299"}
#rawtime{"s":"2012-03-01T14:39:27.772001-07:00"}upvotes{"s":"830"}image_id{"s":"2970"}
#subreddit{"s":"funny"}id{"n":"70569"}num_comments{"s":"33"}title{"s":"TITLE HERE WITHOUT COMMAS"}username{"s":"b0red\r\n"}