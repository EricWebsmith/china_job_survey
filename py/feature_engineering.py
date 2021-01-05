# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:12:04 2019

@author: eric
"""
import os
from os import path
from datetime import datetime
import re

from bs4 import BeautifulSoup
from glob import glob
import inspect
from common import is_article_english,object2list, get_featurenames
#from icu996companies import icu996companies, non996companies
import pandas as pd
from db import get_conn

from config import year, month, company_blacklist, title_key_blacklist, zhinengleibies

#month=1

year_month=f'{year}{month:02}'

class Job():
    #basic info
    job_id=""
    year_month=year_month
    title=""
    page_title=''
    
    job_summary=''
    
    #经验 no 1_3 3_5 5_10 10+
    experience=''

    #学历， 初中以下，高中，专科，本科，硕士，博士
    edu=''
    
    headcount=0
    
    publish_date=datetime.today()
    #如果招聘信息本身都是周末发布的，这个公司应该是周末上班的。既996
    published_on_weekend=False  
    
    monthly_salary=0
    salary_string=''
    
    #职能类别 软件工程师 算法工程师 系统架构设计师
    zhinengleibie=''
    career=''

    #手机开发
    phone_app=False
    phone_android=False
    phone_iso=False
    
    #tags
    #五险一金
    job_tags=''
    tag_five_insurance=False
    #股票期权
    tag_stock=False
    #弹性工作
    tag_flexible=False
    #做六休一
    tag_rest_one_day=False
    #做五休二 周末双休 朝九晚五
    tag_rest_two_days=False
    #不加班
    tag_no_overtime=False
    #
    #tag_9_5=False
    #母婴室
    tag_baby_care=False
    
    #job_description
    job_description=""
    
    #features from job description
    #岁
    ageism=False
    
    #languages
    pl_python=False
    pl_java=False
    pl_javascript=False
    pl_c_sharp=False
    pl_php=False
    #c++
    pl_cpp=False
    pl_objective_c=False
    pl_swift=False
    pl_matlab=False
    pl_typescript=False
    pl_ruby=False
    pl_vba=False
    pl_scala=False
    pl_kotlin=False
    pl_visual_basic=False
    pl_go=False
    pl_perl=False
    pl_r=False
    pl_rust=False
    pl_lua=False
    pl_julia=False
    pl_haskell=False
    pl_delphi=False

    
    #database
    db_Oracle=False
    db_MySQL=False
    #aka mssql ms sql
    db_SQL_Server=False
    db_PostgreSQL=False
    db_MongoDB=False
    db_Firebase=False
    db_Elasticsearch=False
    db_Splunk=False
    db_Redis=False
    db_Apache_Hive=False
    db_SQLite=False
    db_DB2=False
    db_SAP_HANA=False
    db_MariaDB=False
    db_Teradata=False
    db_FileMaker=False
    db_DynamoDB=False
    db_Solr=False
    db_Firebird=False
    db_Sybase=False
    db_Hbase=False
    db_Neo4j=False
    db_Ingres=False
    db_Memcached=False
    db_CouchBase=False
    db_Informix=False
    db_Netezza=False
    db_CouchDB=False
    db_Riak=False
    db_dBase=False

    bd_hadoop=False
    bd_spark=False
    bd_hive=False
    bd_mapReduce=False

    bd_kafka=False
    bd_hbase=False
    bd_storm=False

    bd_pig=False
    bd_mahout=False
    bd_impala=False
    bd_yarn=False
    bd_alluxio=False
    bd_flink=False
    bd_presto=False
    bd_heron=False

    def __init__(self, year_month):
        self.year_month=year_month
    
    def get_big_data_stats(self, job_description_lower):
        self.bd_hadoop='hadoop' in job_description_lower
        if 'hdfs' in job_description_lower:
            self.bd_hadoop=True
        self.bd_spark='spark' in job_description_lower
        self.bd_hive='hive' in job_description_lower
        self.bd_mapReduce='mapReduce' in job_description_lower
        self.bd_kafka='kafka' in job_description_lower
        self.bd_hbase='hbase' in job_description_lower
        self.bd_storm='storm' in job_description_lower
        self.bd_pig='pig' in job_description_lower
        self.bd_mahout='mahout' in job_description_lower
        self.bd_impala='impala' in job_description_lower
        self.bd_yarn='yarn' in job_description_lower
        self.bd_alluxio='alluxio' in job_description_lower
        self.bd_flink='flink' in job_description_lower
        self.bd_presto='presto' in job_description_lower
        self.bd_heron='heron' in job_description_lower
        return self
    
    province=''
    city=''
    #languages
    lang_english=False
    lang_japanese=False
    #company_info
    company_id=''
    

    
    _996_no=False
    _996_yes=False
    
    def get_tags(self, tags):
        self.tag_five_insurance=('五险一金' in tags)
        self.tag_baby_care=('母婴室' in tags)
        self.tag_flexible=('弹性工作' in tags)
        self.tag_no_overtime=('不加班' in tags)
        self.tag_rest_one_day=('做六休一' in tags)
        self.tag_rest_two_days=('做五休二' in tags or '周末双休' in tags or '朝九晚五' in tags)
        self.tag_stock=('股票期权' in tags)
        return self
    
    def get_salary(self, salary_string):
        #零时工，不统计
        if salary_string.endswith('元/小时'):
            self.monthly_salary=-1
        elif salary_string.endswith('万/月'):
            salary_string=salary_string.replace("万/月","")
            salary_min_max=salary_string.split('-')
            self.monthly_salary=(float(salary_min_max[0])+float(salary_min_max[1]))/2*10000
        elif salary_string.endswith('千/月'):
            salary_string=salary_string.replace("千/月","")
            salary_min_max=salary_string.split('-')
            self.monthly_salary=(float(salary_min_max[0])+float(salary_min_max[1]))/2*1000
        elif salary_string.endswith('万/年'):
            salary_string=salary_string.replace("万/年","")
            salary_min_max=salary_string.split('-')
            self.monthly_salary=(float(salary_min_max[0])+float(salary_min_max[1]))/2/12*10000
        elif salary_string.endswith('万/年'):
            salary_string=salary_string.replace("万/年","")
            salary_min_max=salary_string.split('-')
            self.monthly_salary=(float(salary_min_max[0])+float(salary_min_max[1]))/2/12*10000
        elif salary_string.endswith('万以上/月'):
            self.monthly_salary=float(salary_string.replace("万以上/月",""))*10000                    
        elif salary_string.endswith('万以上/年'):
            self.monthly_salary=float(salary_string.replace("万以上/年",""))/12*10000
        return self
    
    def check_edu(self):
        return not self.edu==''

    def get_edu(self, tag):
        if (tag in ['初中及以下','高中','大专','本科','硕士','博士']):
            self.edu=tag
        return self
        
    def check_working_experience(self):
        return not self.experience==''
        
    def get_working_experience(self, tag):
        if (tag=='无工作经验'):
            self.experience='no'
            return self
        if (tag=='10年以上经验'):
            self.experience='10+'
            return self
        if not self.check_working_experience():
            re_result = re.match(r'(\d+)-(\d+)年经验',tag)
            if re_result:
                we=(float(re_result.group(1))+float(re_result.group(2)))/2.0
                if we<3:
                    self.experience='1_3'
                elif we<5:
                    self.experience='3_5'
                elif we<10:
                    self.experience='5_10'
                else:
                    self.experience='10+'
                
                return self

            re_result = re.match(r'(\d+)年经验',tag)
            if re_result:
                we=float(re_result.group(1))
                if we<3:
                    self.experience='1_3'
                elif we<5:
                    self.experience='3_5'
                elif we<10:
                    self.experience='5_10'
                else:
                    self.experience='10+'
        return self


        
    def get_programming_languages(self, job_description_lower):
        self.pl_python='python' in job_description_lower
        self.pl_java='java' in job_description_lower.replace('javascript','')
        self.pl_javascript='javascript' in job_description_lower
        self.pl_c_sharp='c#' in job_description_lower or '.net' in job_description_lower
        self.pl_php='php' in job_description_lower

        self.pl_objective_c='objective c' in job_description_lower
        self.pl_swift='swift' in job_description_lower
        self.pl_matlab='matlab' in job_description_lower
        self.pl_typescript='typescript' in job_description_lower
        self.pl_ruby='ruby' in job_description_lower
        self.pl_vba='vba' in job_description_lower
        self.pl_scala='scala' in job_description_lower
        self.pl_kotlin='kotlin' in job_description_lower
        self.pl_visual_basic='visual basic' in job_description_lower
        self.pl_go='go' in job_description_lower
        self.pl_perl='perl' in job_description_lower
        self.pl_rust='rust' in job_description_lower
        self.pl_lua='lua' in job_description_lower
        self.pl_julia='julia' in job_description_lower
        self.pl_haskell='haskell' in job_description_lower
        self.pl_delphi='delphi' in job_description_lower
        
        #c++
        self.pl_cpp='c++' in job_description_lower
        if 'c语言' in job_description_lower:
            self.pl_cpp=True
        if re.search(r'[^a-z]c[^a-z]',job_description_lower):
            self.pl_cpp=True
            
        #r语言
        if 'r语言' in job_description_lower:
            self.pl_r=True
        if re.search(r'[^a-z]r[^a-z]',job_description_lower):
            self.pl_r=True
            
        return self

    
    def get_databases(self, job_description_lower):
        #database
        self.db_Oracle='oracle' in job_description_lower
        self.db_MySQL='mysql' in job_description_lower
        #aka mssql ms sql
        self.db_SQL_Server='sql server' in job_description_lower \
            or 'mssql' in job_description_lower \
            or 'ms sql' in job_description_lower 
        self.db_PostgreSQL='postgresql' in job_description_lower
        self.db_MongoDB='mongodb' in job_description_lower
        self.db_Firebase='firebase' in job_description_lower
        self.db_Elasticsearch='elasticsearch' in job_description_lower
        self.db_Splunk='splunk' in job_description_lower
        self.db_Redis='redis' in job_description_lower
        self.db_Apache_Hive='apache hive' in job_description_lower
        self.db_SQLite='sqlite' in job_description_lower
        self.db_DB2='db2' in job_description_lower
        self.db_SAP_HANA='sap hana' in job_description_lower
        self.db_MariaDB='mariadb' in job_description_lower
        self.db_Teradata='teradata' in job_description_lower
        self.db_FileMaker='filemaker' in job_description_lower
        self.db_DynamoDB='dynamodb' in job_description_lower
        self.db_Solr='solr' in job_description_lower
        self.db_Firebird='firebird' in job_description_lower
        self.db_Sybase='sybase' in job_description_lower
        self.db_Hbase='hbase' in job_description_lower
        self.db_Neo4j='neo4j' in job_description_lower
        self.db_Ingres='ingres' in job_description_lower
        self.db_Memcached='memcached' in job_description_lower
        self.db_CouchBase='couchbase' in job_description_lower
        self.db_Informix='informix' in job_description_lower
        self.db_Netezza='netezza' in job_description_lower
        self.db_CouchDB='couchdb' in job_description_lower
        self.db_Riak='riak' in job_description_lower
        self.db_dBase='dbase' in job_description_lower
        return self

            
    def check_all(self, raise_exception=False):
#        if not self.check_company_size():
#            raise Exception("check_company_size")
        if raise_exception:
            if self.experience=='':
                raise Exception("check_working_experience")


def printObject(o):
    print(inspect.getmembers(o))


def file2job(file, zhinengleibie, province):
    job=Job(year_month)
    job.zhinengleibie=zhinengleibie

    if province=='深圳':
        job.province='广东'
    else:
        job.province=province

    job.job_id=path.split(file)[-1].replace(".html","")
    
    content=""
    try:
        with open(file, mode='r',encoding='gbk') as f:
            content=f.read()
            f.close()
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
        return None

    
    soup=BeautifulSoup(content, "html.parser")
    title_tag=soup.select_one('title')
    if not title_tag:
        return None
    job.page_title=title_tag.text
    if '异地招聘' in job.page_title:
        #job.province='异地招聘'
        #job.city='异地招聘'
        return
    #职业 start
    #首先判断职业，如果职业不是程序员，直接pass


    job.career=zhinengleibie

    #职业 end
    
    #20-40万/年
    #'1-1.5万/月'
    #10万以上/月
    #100万以上/年
    #3-4.5千/月
    #17元/小时
    salary_tag=soup.select_one('.cn strong')
    if not salary_tag:
        return None
    salary_string=salary_tag.text
    #零时工，不统计
    job.salary_string = salary_string
    job.get_salary(salary_string)
    if job.monthly_salary==-1:
        return None
        
    
    job.title=soup.find("h1").text.strip()

    if any(key in job.title for key in title_key_blacklist):
        return None

    #'深圳-福田区|5-7年经验|本科|招1人|04-01发布'
    job.job_summary=soup.select_one(".msg").text.replace('\xa0','').replace(' ','').strip()
    #print(basic_info)
    infos=job.job_summary.split('|')
    #first location
    job.city=infos[0].split('-')[0]
    #remove the first one - location
    infos=infos[1:]
    for info in infos:
        if '经验' in info and not job.check_working_experience():
            job.get_working_experience(info)
    
        #学历
        if not job.check_edu():
            job.get_edu(info)
        
        #人数
        if '招' in info and '人' in info:
            headcount_string=info.replace('招','').replace('人','')            
            if headcount_string=='若干':
                job.headcount=5
            else:
                job.headcount=int(headcount_string)
    
        if info.endswith('发布'):
    
            #date
            date_string="2020-"+info.replace("发布",'')
            job.publish_date=datetime.strptime(date_string, '%Y-%m-%d')
            weekday=job.publish_date.weekday()
            job.published_on_weekend=weekday>4

        #language
        if '英语' in info or '英文' in info:
            job.lang_english=True
        if '日语' in info or '日文' in info:
            job.lang_japanese=True
        
    #tags
    tags=[tag.text for tag in soup.select('.sp4')]
    job.job_tags=','.join(tags)
    job.get_tags(tags)
    
    h2_span=soup.select_one('h2 span')
    job.job_description=h2_span.parent.find_next('div').text.strip()
    job_description_lower=job.job_description.lower()
    job_description_lower=job.title+" "+job_description_lower

    job.get_programming_languages(job_description_lower) \
        .get_databases(job_description_lower) \
        .get_big_data_stats(job_description_lower) 
    
    #english and japanese
    if '英语' in job_description_lower or '英文' in job_description_lower:
        job.lang_english=True
    #如果招聘信息本身都是英语写的，那么肯定要求英语
    if is_article_english(job_description_lower):
        job.lang_english=True
    if '日语' in job_description_lower or '日文' in job_description_lower:
        job.lang_japanese=True
    
    #手机程序员并不单独归类，而是用smart_phone属性表示
    #手机应用开发工程师    
    if 'iso' in job_description_lower or 'iphone' in job_description_lower:
        job.phone_iso=True
        job.phone_app=True
    if 'android' in job_description_lower:
        job.phone_android=True
        job.phone_app=True

    company_title_tag=soup.select_one('.com_name')
    if not company_title_tag:
        company_title_tag=soup.select_one('.catn')
    company_title=company_title_tag.text.strip()
    #black named companies
    if company_title in company_blacklist:
        return None
    company_link=company_title_tag.attrs['href']
    job.company_id=re.match(r'.*(co\d*).html', company_link).group(1)
        
    #996
    #朝九晚五，周末双休 双休 不加班
    if '朝九晚五' in job.job_description \
        or '朝九晚六' in job.job_description \
        or '双休' in job.job_description \
        or '不加班' in job.job_description:
        job._996_no=True
    if '朝九晚九' in job.job_description:
        job._996_yes=True
    if job.tag_rest_two_days:
        job._996_no=True
    if job.published_on_weekend:
        job._996_yes=True
    
    return job

def try_rename(file):
    #return
    new_file=file.replace(f"51jobs_{year_month}",f"51jobs_{year_month}_b")
    if path.isfile(new_file):
        os.remove(file)
    else:
        os.rename(file, new_file) 

def file2db(file, zhinengleibie, province):
    conn=get_conn()
        
    filename=path.split(file)[-1]
    job_id=filename.replace(".html","")           
    
    exists=conn.execute(f"select count(1) from jobs where job_id='{job_id}' and year_month={year_month}").fetchall()[0][0]
    if exists:
        try_rename(file)
        return

    #print(file)
    job=file2job(file, zhinengleibie, province)
    if not job:
        try_rename(file)
        return
    
    data=pd.DataFrame(columns=get_featurenames(job))
    l=object2list(job)
    data.loc[job.job_id]=l
    data.to_sql("jobs", conn, if_exists="append", index=False)

    conn.close()
    try_rename(file)   

def city2db(data_folder,zhinengleibie, province):
    city_folder=path.join(data_folder,zhinengleibie, province)
    files = glob(path.join(city_folder,"*.html"))
    for file in files:
        file2db(file, zhinengleibie, province) 

def process_folder(zhinengleibie):
    print(f"{zhinengleibie} starting...")
    provinces=['北京','上海','广东','深圳','天津','重庆','江苏','浙江','四川','海南','福建','山东','江西','广西','安徽','河北','河南','湖北','湖南','陕西','山西','黑龙江','辽宁','吉林','云南','贵州','甘肃','内蒙古','宁夏','西藏','新疆','青海']
    data_folder = '../../data/51jobs_{}/'.format(year_month)
    back_folder = '../../data/51jobs_{}_b/'.format(year_month)
    category_back_folder=path.join(back_folder, zhinengleibie)
    if not path.isdir(category_back_folder):
        os.mkdir(category_back_folder)
    for province in provinces:
        city_back_folder=path.join(category_back_folder, province)
        if not path.isdir(city_back_folder):
            os.mkdir(city_back_folder)

        city2db(data_folder, zhinengleibie, province)
    print(f"{zhinengleibie} succeeded.")

def main():
    from concurrent.futures.process import ProcessPoolExecutor
    data_folder = '../../data/51jobs_{}/'.format(year_month)
    categoris=[d for d in  os.listdir(data_folder) if  path.isdir(f'{data_folder}{d}')]
    with ProcessPoolExecutor() as executor:
        executor.map(process_folder, categoris)
    #provinces=['北京','上海','广东','深圳','天津','重庆','江苏','浙江','四川','海南','福建','山东','江西','广西','安徽','河北','河南','湖北','湖南','陕西','山西','黑龙江','辽宁','吉林','云南','贵州','甘肃','内蒙古','宁夏','西藏','新疆','青海']
    #data_folder = '../../data/51jobs_{}/'.format(year_month)
    #back_folder = '../../data/51jobs_{}_b/'.format(year_month)
    # for _, dirs, _ in os.walk(data_folder):
    #     for dir in dirs:
    #         print(dir)
    #         #process_folder(year_month, dir)

def main2():
    from concurrent.futures.process import ProcessPoolExecutor
    data_folder = '../../data/51jobs_{}/'.format(year_month)
    categoris=[d for d in  os.listdir(data_folder) if  path.isdir(f'{data_folder}{d}')]

    #provinces=['北京','上海','广东','深圳','天津','重庆','江苏','浙江','四川','海南','福建','山东','江西','广西','安徽','河北','河南','湖北','湖南','陕西','山西','黑龙江','辽宁','吉林','云南','贵州','甘肃','内蒙古','宁夏','西藏','新疆','青海']
    #data_folder = '../../data/51jobs_{}/'.format(year_month)
    #back_folder = '../../data/51jobs_{}_b/'.format(year_month)


    for cat in categoris:    
        process_folder(cat)

if __name__=='__main__':
    #global year_month

    main()
