import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('tmosbundlesbackup')
obj = bucket.Object(sys.argv[1])

with open('tmos24/firstInstall.zip', 'wb') as data:
    obj.download_fileobj(data)
