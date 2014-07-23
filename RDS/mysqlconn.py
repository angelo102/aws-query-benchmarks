import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootroot',
                              host='dbinstance2.cykrspa9y2be.us-west-2.rds.amazonaws.com',
                              database='cse6331')

print cnx

cursor=cnx.cursor()

query="""
	CREATE TABLE `table2` (
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

result=cursor.execute(query)

#rows = cursor.fetchall();

#print rows

#cursor.close()
cnx.close()
