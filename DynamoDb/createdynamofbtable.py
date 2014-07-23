import boto.dynamodb

#connect using boto to dynamodb 
conn = boto.dynamodb.connect_to_region('us-west-2')

#create table on DynamoDb
#first create schema

table_schema = conn.create_schema(
	hash_key_name='id',
	hash_key_proto_value=int
	)
#create the new table
table = conn.create_table(
	name='importdata',
	schema=table_schema,
	read_units=10,
	write_units=5
	)
