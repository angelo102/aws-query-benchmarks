
import random
from datetime import datetime
import boto.dynamodb

#get start time
start = datetime.now()

#connect using boto to dynamodb 
conn = boto.dynamodb.connect_to_region('us-west-2')

#open Dynamodb table
table = conn.get_table('importdata2')

#run 50,000 queries random throughout the data
for i in range(50000):
  #get random int ranging in the amount of rows of the data
  n_id = random.randint(1,117007)
  #execute the create command
  result=table.get_item(n_id)
  print i,result

#get final time
final=datetime.now()

print "initial time:", str(start)
print "final time:",  str(final)
print "elapsed Time:",  str(final - start)
