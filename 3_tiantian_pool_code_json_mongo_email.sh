#!/bin/sh
# 启动进程
cd /root/worksapce/Superman/com/alex/strategy
nohup python tiantian_pool_code_json_mongo_email.py > tiantian_code.log 2>&1 &
tail -f tiantian_code.log