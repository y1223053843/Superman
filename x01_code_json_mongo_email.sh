#!/bin/sh
# 启动进程
PATH=/root/anaconda2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
export PATH
cd /root/worksapce/Superman/com/alex/strategy
nohup python x01_code_json_mongo_email.py > gold_code.log 2>&1 &