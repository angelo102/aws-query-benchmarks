'''
Name: Angel Romero 10001044475
	  Md Merajul Islam 1000865420
Course Number: CSE 6331 Cloud Computing
Lab: Assignment 3 Part 1
 
'''

import ConfigParser
import boto
from boto.s3.key import Key
from datetime import datetime

#get settings
config = ConfigParser.ConfigParser()
config.read("settings.ini")
bucket = config.get("SectionOne","bucket")
filepath = config.get("SectionOne","filepath")

#start time
start = datetime.now()
print "initial time:", str(start)

#Upload file to S3 Amazon Service
conn=boto.connect_s3()
bucket=conn.get_bucket(bucket)
key = Key(bucket)
key.key = 'importdata'
key.set_contents_from_filename(filepath)

#end time
final=datetime.now()
print "final time:",  str(final)

print "elapsed Time:",  str(final - start)