
import time
import subprocess
import mysql.connector
import ConfigParser
import random
from datetime import datetime

#get settings
config = ConfigParser.ConfigParser()
config.read("settings.ini")
user = config.get("SectionOne","user")
password = config.get("SectionOne","password")
host = config.get("SectionOne","host")
database = config.get("SectionOne","database")

#get start time
start = datetime.now()

#create table for data import
cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
cursor=cnx.cursor()

#run 50,000 queries random throughout the data
for i in range(100):
  #get random int ranging in the amount of rows of the data
  row = random.randint(0,117007)
  query="select * from importdata limit {0},1"
  #execute the query command
  cursor.execute(query.format(row))
  print i, cursor.fetchall()

cnx.close()

#get final time
final=datetime.now()

print "initial time:", str(start)
print "final time:",  str(final)
print "elapsed Time:",  str(final - start)
