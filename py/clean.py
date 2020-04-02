# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:52:57 2020

@author: eric
"""

import config

for table in config.table_list:
    company_titles="('"+"','".join(config.company_blacklist)+"')"
    sql=f'delete from {table} where company_title in {company_titles}'
    print(sql)
    
    
for table in config.table_list:

    for key in config.title_key_blacklist:
        sql=f"delete from {table} where title like '%{key}%'"
        print(sql)
        
title_end_blacklist=['审核']
        
for table in config.table_list:
    sql=f"delete from {table} where title like '%审核'"
    print(sql)
    
ids=['105141736', '89941978','107192348']

for table in config.table_list:
    sql=f"delete from {table} where job_id='107192348'"
    print(sql)