#Test
#52 7 * * 1-5 cd /root/worksapce/Superman && sh ./2_b_code_json_mongo_email.sh && sh ./3_tiantian_pool_code_json_mongo_email.sh

#Execute
50 9 * * * cd /root/worksapce/Superman && sh ./3_tiantian_pool_code_json_mongo_email.sh && sh ./4_tiantian_all_pool_code_json_mongo_email.sh
29 10,11 * * * cd /root/worksapce/Superman && sh ./3_tiantian_pool_code_json_mongo_email.sh && sh ./4_tiantian_all_pool_code_json_mongo_email.sh
59 13 * * * cd /root/worksapce/Superman && sh ./3_tiantian_pool_code_json_mongo_email.sh && sh ./4_tiantian_all_pool_code_json_mongo_email.sh
49 14 * * * cd /root/worksapce/Superman && sh ./3_tiantian_pool_code_json_mongo_email.sh && sh ./4_tiantian_all_pool_code_json_mongo_email.sh

#Jian kong
50 9 * * * cd /root/worksapce/Superman && sh ./2_b_code_json_mongo_email.sh
28 10,11 * * * cd /root/worksapce/Superman && sh ./2_b_code_json_mongo_email.sh
58 13 * * * cd /root/worksapce/Superman && sh ./2_b_code_json_mongo_email.sh
48 14 * * * cd /root/worksapce/Superman && sh ./2_b_code_json_mongo_email.sh

#All code
0 11 * * * cd /root/worksapce/Superman && sh ./1_all_code_json_mongo.sh
40 13 * * * cd /root/worksapce/Superman && sh ./1_all_code_json_mongo.sh
25 14 * * * cd /root/worksapce/Superman && sh ./1_all_code_json_mongo.sh

#Zhi shu
58 13 * * * cd /root/worksapce/Superman && sh ./5_zhishu_code_json_mongo_email.sh
28 10,11,13,14 * * * cd /root/worksapce/Superman && sh ./5_zhishu_code_json_mongo_email.sh
48 14 * * * cd /root/worksapce/Superman && sh ./5_zhishu_code_json_mongo_email.s