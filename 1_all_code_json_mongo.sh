#!/bin/sh
# 启动进程

PATH=/root/anaconda2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
export PATH

cd /root/worksapce/Superman/com/alex/strategy
nohup python all_code_json_mongo.py > all_code.log 2>&1 &
nohup python all_code_json_mongo_slave_1.py > all_code_slave_1.log 2>&1 &
nohup python all_code_json_mongo_slave_2.py > all_code_slave_2.log 2>&1 &
nohup python all_code_json_mongo_slave_3.py > all_code_slave_3.log 2>&1 &
nohup python all_code_json_mongo_slave_4.py > all_code_slave_4.log 2>&1 &