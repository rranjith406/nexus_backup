import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('tmosbundlesbackup')

for file in my_bucket.objects():
    print(file.key)
