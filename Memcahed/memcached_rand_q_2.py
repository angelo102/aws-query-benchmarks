
import memcache
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
memcluster = config.get("SectionOne","memcachecluster")

#get start time
start = datetime.now()

#connect and initialize cursor
cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
cursor=cnx.cursor()

#connect to memcachecluster
memc = memcache.Client([memcluster])

#run 50,000 queries random throughout the data
for i in range(25000):
  #get random int ranging in only 1% of the data
  n = random.randint(1,1170)
  #get result from memcached
  result = memc.get(str(n))
  if not result:
  	query="select * from importdata limit {0},1"
  	#execute the query command
  	cursor.execute(query.format(n))
  	rows = cursor.fetchall()
  	memc.set(str(n),rows)
  	print i, "from mysql: ", rows
  else:
  	print i, "from memcache: ", result

#run second 50% by querying 100% of the data
for i in range(25000):
  #get random int ranging in the amount of rows of the data
  n = random.randint(1,117007)
  #get result from memcached
  result = memc.get(str(n))
  if not result:
    query="select * from importdata limit {0},1"
    #execute the query command
    cursor.execute(query.format(n))
    rows = cursor.fetchall()
    memc.set(str(n),rows)
    print i+25000,"from mysql: ", rows
  else:
    print i+25000,"from memcache: ", result

cnx.close()

#get final time
final=datetime.now()

print "initial time:", str(start)
print "final time:",  str(final)
print "elapsed Time:",  str(final - start)
