import os
import boto3

with open(r'pick+_result.txt', 'r') as infile, \
     open(r'tobe_downloaded.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("+", "")
    outfile.write(data)
#    os.system("/home/ubuntu/python_scripts/download_objects.py data")
