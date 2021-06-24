# This is to list only folder names in the bucket
import boto3

client = boto3.client('s3')
bucket = 'tmosbundlesbackup'
folders = set()
for prefix in client.list_objects(Bucket=bucket, Delimiter='/')['CommonPrefixes']:
       folders.add(prefix['Prefix'][:-1])
    

#print(folders)
for e in folders:
    print(e)

