#!/bin/sh
# 启动进程
cd /root/worksapce/Superman/com/alex/strategy
nohup python all_code_json_mongo.py > all_code.log 2>&1 &
tail -f all_code.log