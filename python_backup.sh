#!/bin/bash
python3 list_onlyfolder.py > temp
sudo chmod 777 temp
python3 diff.py > diff_result.txt
sudo chmod 777 diff_result.txt
python3 pick+.py > pick+_result.txt
sudo chmod 777 pick+_result.txt
python3 pick_old.py > tobe_deleted.txt
sudo chmod 777 tobe_deleted.txt
python3 remove+.py
sudo chmod 777 tobe_downloaded.txt
boto3.set_stream_logger('botocore', level='DEBUG')
