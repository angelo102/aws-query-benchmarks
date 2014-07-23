import time
import subprocess
import mysql.connector
import ConfigParser
from datetime import datetime

#get settings
config = ConfigParser.ConfigParser()
config.read("settings.ini")
user = config.get("SectionOne","user")
password = config.get("SectionOne","password")
host = config.get("SectionOne","host")
database = config.get("SectionOne","database")
filepath = config.get("SectionOne","filepath")


#get start time
start = datetime.now()
print "initial time:", str(start)

#create table for data import
cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
cursor=cnx.cursor()
query="""
		CREATE TABLE `{0}`
  		(
  		`image_id` int(11) DEFAULT NULL,
  		`unixtime` varchar(45) DEFAULT NULL,
  		`rawtime` varchar(45) DEFAULT NULL,
  		`title` varchar(400) DEFAULT NULL,
  		`total_votes` int(11) DEFAULT NULL,
  		`reddit_id` varchar(45) DEFAULT NULL,
  		`upvotes` int(11) DEFAULT NULL,
  		`subreddit` varchar(45) DEFAULT NULL,
  		`downvotes` int(11) DEFAULT NULL,
  		`localtime` varchar(45) DEFAULT NULL,
  		`score` int(11) DEFAULT NULL,
  		`num_comments` int(11) DEFAULT NULL,
  		`username` varchar(45) DEFAULT NULL
		)
		"""
#get the file name
filename = filepath.split("/")[-1].split(".")[0]
#execute the create command
result=cursor.execute(query.format(filename))
cnx.close()

#run the import process
outp=subprocess.check_call(['mysqlimport',
	'--local',
	'--compress',
	'--user='+user,
	'--password='+password,
	'--host='+host,
	'--fields-terminated-by=,',
	database,
	filepath])

#get final time
final=datetime.now()

print "final time:",  str(final)
print "elapsed Time:",  str(final - start)

print "System Exit Code:", outp
