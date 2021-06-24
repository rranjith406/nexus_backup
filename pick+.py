# This file will list out all the new objects/version added to the tmosbundlesbackup bucket
for line in open('diff_result.txt'):
    if line.startswith('+') :
       print (line)
