import boto3
import sys

s3 = boto3.resource('s3')
bucket = s3.Bucket('tmosbundlesbackup')
for obj in bucket.objects.filter(Prefix=sys.argv[1]):
    s3.Object(bucket.name,obj.key).delete()
