# this file is to list out the existing objects in the tmosbundlesbackup bucket
for line in open('diff_result.txt'):
    if line.startswith(' ') :
        print (line)
    

