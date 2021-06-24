import boto3
import sys
s3 = boto3.resource('s3')
bucket = s3.Bucket('tmosbundlesbackup')
obj = bucket.Object(sys.argv[1])

with open('/home/ubuntu/python_scripts/tmos25/New_verion/', 'wb') as data:
    obj.download_fileobj(data)
