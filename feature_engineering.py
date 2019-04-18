# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:12:04 2019

@author: eric
"""
import os
from os import path
from datetime import datetime
import re
from requests import get
from bs4 import BeautifulSoup
from glob import glob
import inspect
from common import is_article_english,object2list, get_featurenames
from icu996companies import icu996companies, non996companies
import pandas as pd
from db import get_conn
import threading


class Job():
    #basic info
    job_id=""
    title=""
    #无经验
    experience_no=False
    #1-3年
    experience_1_3=False
    #3-5年
    experience_3_5=False
    #5-10年
    experience_5_10=False
    #10年以上
    experience_10=False

    
    #学历， one hot
    edu_middle_school=False
    edu_high_school=False
    edu_associate=False
    edu_bachelor=False
    edu_master=False
    edu_phd=False
    
    publish_date=datetime.today()
    #如果招聘信息本身都是周末发布的，这个公司应该是周末上班的。既996
    published_on_weekend=False  
    
    monthly_salary=0
    
    #职能类别 one-hot-encoding
    #软件工程师
    career_software_engineer=False

    #算法工程师
    career_algorithm=False

    #系统架构设计师
    career_architect=False

    
    #手机开发
    phone_app=False
    phone_android=False
    phone_iso=False
    
    #tags
    #五险一金
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
    pl_scrala=False
    pl_kotlin=False
    pl_visual_basic=False
    pl_go=False
    pl_perl=False
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
    #city
    #['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan',
    #'chongqing','chengdu','changsha','fuzhou','hefei','ningbo','zhengzhou',
    #'tianjin','qingdao','jinan','kuming','shenyang','xian','dongguan','dalian','harbin','changchun']
    city_beijing=False
    city_beijing=False
    city_shanghai=False
    city_guangzhou=False
    city_shenzhen=False
    city_hangzhou=False
    city_nanjing=False
    city_wuhan=False
    city_chongqing=False
    city_chengdu=False
    city_changsha=False
    city_fuzhou=False
    city_hefei=False
    city_ningbo=False
    city_zhengzhou=False
    city_tianjin=False
    city_qingdao=False
    city_jinan=False
    city_kuming=False
    city_shenyang=False
    city_xian=False
    city_dongguan=False
    city_dalian=False
    city_harbin=False
    city_changchun=False
    #languages
    english=False
    japanese=False
    #company_info
    company_title=""
    
    company_description=""
    #外资(欧美)
    company_type_us_eu=False
    #外资(非欧美)
    company_type_foreign=False
    #合资
    company_tpye_jv=False
    #国企
    company_type_state=False
    #民营公司
    company_type_private=False
    #外企代表处
    company_type_foreign_rep=False
    #政府机关
    company_type_foreign_gov=False
    #事业单位
    company_type_public_institution=False
    #非营利组织
    company_type_non_profit=False
    #上市公司
    company_type_listed=False
    #创业公司
    company_type_startup=False

    #少于50人
    company_size_50=False
    #50-150人
    company_size_50_150=False
    #150-500人
    company_size_150_500=False
    #500-1000人
    company_size_500_1000=False
    #1000-5000人
    company_size_1000_5000=False
    #5000-10000人
    company_size_5000_10000=False
    #10000人以上
    company_size_10000=False
    
    #计算机/互联网/通信/电子
    industry_computer=False
    #会计/金融/银行/保险
    industry_finance=False
    #贸易/消费/制造/营运
    industry_trade=False
    #制药/医疗
    industry_medical=False
    #广告/媒体
    industry_ads=False
    #房地产/建筑
    industry_realestate=False
    #专业服务/教育/培训
    industry_edu=False
    #服务业
    industry_service=False
    #物流/运输
    industry_logistic=False
    #能源/原材料
    industry_energy=False
    #政府/非营利组织/其他
    industry_gov=False
    
    non_996=False
    icu_996=False
    
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
        return self.edu_middle_school or \
        self.edu_high_school or \
        self.edu_associate or \
        self.edu_bachelor or \
        self.edu_master or \
        self.edu_phd

    def get_edu(self, tag):
        self.edu_middle_school=(tag=='初中及以下')
        self.edu_high_school=(tag=='高中')
        self.edu_associate=(tag=='大专')
        self.edu_bachelor=(tag=='本科')
        self.edu_master=(tag=='硕士')
        self.edu_phd=(tag=='博士')
        return self
        
    def check_working_experience(self):
        return self.experience_no or \
        self.experience_1_3 or \
        self.experience_3_5 or \
        self.experience_5_10 or \
        self.experience_10
        
    def get_working_experience(self, tag):
        self.experience_no=(tag=='无工作经验')
        self.experience_1_3=(tag=='1-3年经验')
        self.experience_3_5=(tag=='3-5年经验')
        self.experience_5_10=(tag=='5-10年经验')
        self.experience_10=(tag=='10年以上经验')
        if not self.check_working_experience():
            re_result = re.match(r'(\d+)-(\d+)年经验',tag)
            if re_result:
                we=float(re_result.group(1))+float(re_result.group(2))
                we=we/2.0
                if we<3:
                    self.experience_1_3=True
                elif we<5:
                    self.experience_3_5=True
                elif we<10:
                    self.experience_5_10=True
                else:
                    self.experience_10=True
            re_result = re.match(r'(\d+)年经验',tag)
            if re_result:
                we=float(re_result.group(1))
                if we<3:
                    self.experience_1_3=True
                elif we<5:
                    self.experience_3_5=True
                elif we<10:
                    self.experience_5_10=True
                else:
                    self.experience_10=True
        return self

    def check_company_size(self):
        return (self.company_size_50 or \
        self.company_size_50_150 or \
        self.company_size_150_500 or \
        self.company_size_500_1000 or \
        self.company_size_1000_5000 or \
        self.company_size_5000_10000 or \
        self.company_size_10000)
        
    def get_company_size(self, tag):
        self.company_size_50=(tag=='少于50人')
        self.company_size_50_150=(tag=='50-150人')
        self.company_size_150_500=(tag=='150-500人')
        self.company_size_500_1000=(tag=='500-1000人')
        self.company_size_1000_5000=(tag=='1000-5000人')
        self.company_size_5000_10000=(tag=='5000-10000人')
        self.company_size_10000=(tag=='10000人以上')
        return self
        
    def check_company_type(self):
        return self.company_type_us_eu or \
        self.company_type_foreign or \
        self.company_tpye_jv or \
        self.company_type_state or \
        self.company_type_private or \
        self.company_type_foreign_rep or \
        self.company_type_foreign_gov or \
        self.company_type_public_institution or \
        self.company_type_non_profit or \
        self.company_type_listed or \
        self.company_type_startup
        
    def get_company_type(self, tag):
        self.company_type_us_eu=(tag=='外资（欧美）')
        self.company_type_foreign=(tag=='外资（非欧美）')
        self.company_tpye_jv=(tag=='合资')
        self.company_type_state=(tag=='国企')
        self.company_type_private=(tag=='民营公司')
        self.company_type_foreign_rep=(tag=='外企代表处')
        self.company_type_foreign_gov=(tag=='政府机关')
        self.company_type_public_institution=(tag=='事业单位')
        self.company_type_non_profit=(tag=='非营利组织')
        self.company_type_listed=(tag=='上市公司')
        self.company_type_startup=(tag=='创业公司')
        return self
        
    def get_programming_languages(self, job_description_lower):
        self.pl_python='python' in job_description_lower
        self.pl_java='java' in job_description_lower.replace('javascript','')
        self.pl_javascript='javascript' in job_description_lower
        self.pl_c_sharp='c#' in job_description_lower or '.net' in job_description_lower
        self.pl_php='php' in job_description_lower
        #c++
        self.pl_cpp='c++' in job_description_lower
        self.pl_objective_c='objective c' in job_description_lower
        self.pl_swift='swift' in job_description_lower
        self.pl_matlab='matlab' in job_description_lower
        self.pl_typescript='typescript' in job_description_lower
        self.pl_ruby='ruby' in job_description_lower
        self.pl_vba='vba' in job_description_lower
        self.pl_scrala='scrala' in job_description_lower
        self.pl_kotlin='kotlin' in job_description_lower
        self.pl_visual_basic='visual basic' in job_description_lower
        self.pl_go='go' in job_description_lower
        self.pl_perl='perl' in job_description_lower
        self.pl_rust='rust' in job_description_lower
        self.pl_lua='lua' in job_description_lower
        self.pl_julia='julia' in job_description_lower
        self.pl_haskell='haskell' in job_description_lower
        self.pl_delphi='delphi' in job_description_lower
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

    def check_industry(self):
        return (self.industry_computer or self.industry_finance or self.industry_trade or self.industry_medical \
        or self.industry_ads or self.industry_realestate or self.industry_edu or self.industry_service \
        or self.industry_logistic or self.industry_energy or self.industry_gov)

    def get_industry(self, industry_tag):
        if industry_tag in ['计算机软件','计算机硬件','计算机服务(系统、数据服务、维修)','通信/电信/网络设备','通信/电信运营、增值服务','互联网/电子商务','网络游戏','电子技术/半导体/集成电路','仪器仪表/工业自动化']:
            self.industry_computer=True
        #会计/金融/银行/保险
        if industry_tag in ['会计/审计','金融/投资/证券','银行','保险','信托/担保/拍卖/典当']:
            self.industry_finance=True
        #贸易/消费/制造/营运
        if industry_tag in ['贸易/进出口','批发/零售','快速消费品(食品、饮料、化妆品)','服装/纺织/皮革','家具/家电/玩具/礼品','奢侈品/收藏品/工艺品/珠宝','办公用品及设备','机械/设备/重工','汽车及零配件']:
            self.industry_trade=True
        #制药/医疗
        if industry_tag in ['制药/生物工程','医疗/护理/卫生','医疗设备/器械']:
            self.industry_medical=True
        #广告/媒体
        if industry_tag in ['广告','公关/市场推广/会展','影视/媒体/艺术/文化传播','文字媒体/出版','印刷/包装/造纸']:
            self.industry_ads=True
        #房地产/建筑
        if industry_tag in ['房地产','建筑/建材/工程','家居/室内设计/装潢','物业管理/商业中心']:
            self.industry_realestate=True
        #专业服务/教育/培训
        if industry_tag in ['中介服务','专业服务(咨询、人力资源、财会)','外包服务','检测，认证','法律','教育/培训/院校','学术/科研','租赁服务']:
            self.industry_edu=True
        #服务业
        if industry_tag in ['餐饮业','酒店/旅游','娱乐/休闲/体育','美容/保健','生活服务']:
            self.industry_service=True
        #物流/运输
        if industry_tag in ['交通/运输/物流','航天/航空']:
            self.industry_logistic=True
        #能源/原材料
        if industry_tag in ['石油/化工/矿产/地质','采掘业/冶炼','电气/电力/水利','新能源','原材料和加工']:
            self.industry_energy=True
        #政府/非营利组织/其他
        if industry_tag in ['政府/公共事业','非营利组织','环保','农/林/牧/渔','多元化业务集团公司']:
            self.industry_gov=True
        return self
            
    def check_all(self, raise_exception=False):
#        if not self.check_company_size():
#            raise Exception("check_company_size")
        if raise_exception:
            if not self.check_company_type():
                raise Exception("check_company_type")
            if not self.check_industry():
                raise Exception("check_industry")
            if not self.check_working_experience():
                raise Exception("check_working_experience")
        return self.check_company_type() and self.check_industry() \
            and self.check_working_experience() and self.check_edu() \
            and self.check_company_size()

def in_996_list(company_title):
    return any(icu996 in company_title for icu996 in icu996companies)

def in_non_996_list(company_title):
    return any(non996 in company_title for non996 in non996companies)

def printObject(o):
    print(inspect.getmembers(o))

def get_company_tags(company_link):
    response=get(company_link)
    response.encoding='gbk'
    soup=BeautifulSoup(response.text, 'html.parser')
    info_string=soup.select_one('.ltype').text
    return [info.strip() for info in info_string.split('|')]

def file2job(file, city):
    job=Job()
    setattr(job,"city_"+city,True)
    job.job_id=path.split(file)[-1].replace(".html","")
    #print(file)
    content=""
    with open(file, mode='r',encoding='gbk') as f:
        content=f.read()
        f.close()
    os.rename(file, file.replace("51jobs","51jobs_back"))
    soup=BeautifulSoup(content, "html.parser")
    
    #职业 start
    #首先判断职业，如果职业不是程序员，直接pass
    #career=soup.find('span',{'class':'label'},text='职能类别：').find_next('a').text.strip()
    careers=[a_tag.text.strip() for a_tag in soup.find('span',{'class':'label'},text='职能类别：').parent.find_all('a')]
    for career in careers:
        if (career in ['软件工程师','高级软件工程师','ERP技术开发','互联网软件开发工程师','多媒体/游戏开发工程师','手机应用开发工程师','WEB前端工程师','脚本开发工程师','语音/视频/图形开发工程师']):
            job.career_software_engineer=True
        if career=='算法工程师':
            job.career_algorithm=True
        if career in ['系统架构设计师','网站架构设计师']:
            job.career_architect=True

    is_developer=job.career_software_engineer or job.career_algorithm or job.career_architect
    if not is_developer:
        return None
    
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
    job.get_salary(salary_string)
    if job.monthly_salary==-1:
        return None
        
    
    job.title=soup.find("h1").text.strip()
    #'深圳-福田区|5-7年经验|本科|招1人|04-01发布'
    basic_info=soup.select_one(".msg").text.replace('\xa0','').replace(' ','').strip()
    #print(basic_info)
    infos=basic_info.split('|')
    
    #remove the first one - location
    infos=infos[1:]
    for info in infos:
        if '经验' in info and not job.check_working_experience():
            job.get_working_experience(info)
    
        #学历
        if not job.check_edu():
            job.get_edu(info)

    
        if info.endswith('发布'):
    
            #date
            date_string="2019-"+info.replace("发布",'')
            job.publish_date=datetime.strptime(date_string, '%Y-%m-%d')
            weekday=job.publish_date.weekday()
            job.published_on_weekend=weekday>4


        #language
        if '英语' in info or '英文' in info:
            job.english=True
        if '日语' in info or '日文' in info:
            job.japanese=True
        
    #tags
    tags=[tag.text for tag in soup.select('.sp4')]
    job.get_tags(tags)
    
    h2_span=soup.select_one('h2 span')
    job.job_description=h2_span.parent.find_next('div').text.strip()
    job_description_lower=job.job_description.lower()
    job_description_lower=job.title+" "+job_description_lower
    
    #年龄歧视
    job.ageism='岁' in job.job_description
    

    #继续判断是不是架构师
    if '架构师' in job_description_lower:
        job.career_algorithm=True
    #继续判断是不是算法工程师
    if 'tensorflow' in job_description_lower \
        or 'keras' in job_description_lower \
        or 'caffe' in job_description_lower \
        or 'pytorch' in job_description_lower \
        or '机器学习' in job_description_lower \
        or 'nlp' in job_description_lower \
        or '自然语言处理' in job_description_lower \
        or '算法工程师' in job_description_lower \
        or 'sklearn' in job_description_lower \
        or '深度学习' in job_description_lower \
        or '图像识别' in job_description_lower:
        job.career_algorithm=True
        
    
    if job.career_algorithm or job.career_architect:
        job.career_software_engineer=True
        

    job.get_programming_languages(job_description_lower).get_databases(job_description_lower)
    
    #english and japanese
    if '英语' in job_description_lower or '英文' in job_description_lower:
        job.english=True
    #如果招聘信息本身都是英语写的，那么肯定要求英语
    if is_article_english(job_description_lower):
        job.english=True
    if '日语' in job_description_lower or '日文' in job_description_lower:
        job.japanese=True
    
    #手机程序员并不单独归类，而是用smart_phone属性表示
    #手机应用开发工程师
    if '手机应用开发工程师' in careers:
        job.phone_app=True
    
    if 'iso' in job_description_lower or 'iphone' in job_description_lower:
        job.phone_iso=True
        job.phone_app=True
    if 'android' in job_description_lower:
        job.phone_android=True
        job.phone_app=True

    
    #<span class="bname">公司信息</span>
    job.company_description=soup.find('span',text='公司信息').parent.find_next('div').text.replace('\xa0',' ').strip()
    job.company_title=soup.select_one('.com_name').text.strip()
    #['民营公司', '150-500人', '服装/纺织/皮革']
    company_tags=[p.text.strip() for p in soup.select('.com_tag .at')]
    
    
    job.get_company_type(company_tags[0])
    if not job.check_company_type():
        company_link=soup.select_one('.com_name').attrs['href']
        company_tags=get_company_tags(company_link)
        for tag in company_tags:
            if job.get_company_type(tag).check_company_type():
                break 

    if not job.check_company_type():
        return None
    
    job.get_company_size(company_tags[1])
    if not job.check_company_size():
        company_link=soup.select_one('.com_name').attrs['href']
        company_tags=get_company_tags(company_link)
        for tag in company_tags:
            if job.get_company_size(tag).check_company_size():
                break
            
    #计算机/互联网/通信/电子
    industry_tags=[p.text.strip() for p in soup.select('.com_tag .at a') if not p.text=='']
    
    
    if len(industry_tags)==0:
        company_link=soup.select_one('.com_name').attrs['href']
        industry_tags=get_company_tags(company_link)
    
    for industry_tag in industry_tags:
        job.get_industry(industry_tag)
    
    if job.company_title in ['系统集成有限责任公司','博彦科技股份有限公司']:
        job.industry_computer=True
    if job.company_title=='软件与服务中心':
        job.industry_trade=True
    if job.company_title== '中核集团技术经济总院':
           job.industry_energy=True
    
#    if not job.check_industry():
#        raise Exception("no industry")
        
    #996
    #朝九晚五，周末双休 双休 不加班
    if '朝九晚五' in job.job_description \
        or '朝九晚六' in job.job_description \
        or '双休' in job.job_description \
        or '不加班' in job.job_description:
        job.non_996=True
    if '朝九晚九' in job.job_description:
        job.icu_996=True
    if job.tag_rest_two_days:
        job.non_996=True
    if in_996_list(job.company_title):
        job.icu_996=True
    if in_non_996_list(job.company_title):
        job.non_996=True
    if job.published_on_weekend:
        job.icu_996=True
    
    return job

def file2db(file, city):
    conn=get_conn()
    try:
        
        filename=path.split(file)[-1]
        job_id=filename.replace(".html","")           
    
        exists=conn.execute("select count(1) from _51jobs where job_id='{0}'".format(job_id)).fetchall()[0][0]
        if exists:
            os.rename(file, file.replace("51jobs","51jobs_back"))
            return
        print(file)
        job=file2job(file, city)
        if not job:
            return
#        if not job.check_all():
#            return
    
        data=pd.DataFrame(columns=get_featurenames(job))
        l=object2list(job)
        data.loc[job.job_id]=l
        data.to_sql("_51jobs",conn,if_exists="append", index=False)
    except Exception:
        pass
    finally:
        conn.close()
    
def city2db(city_folder, city):
    files = glob(path.join(city_folder,"*.html"))
    for file in files:
        file2db(file, city) 
    
def main():
    city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing', \
                'wuhan','chongqing','chengdu','changsha','fuzhou','hefei','ningbo',\
                'zhengzhou','tianjin','qingdao','jinan','kuming','shenyang','xian',\
                'dongguan','dalian','harbin','changchun']
    #city_names=['shanghai']
    data_folder = '../data/51jobs/'
    back_folder = '../data/51jobs_back/'
    for job_category in ['0100','2500']:
        category_back_folder=path.join(back_folder, job_category)
        if not path.isdir(category_back_folder):
            os.mkdir(category_back_folder)
        for city in city_names:
            city_back_folder=path.join(category_back_folder, city)
            if not path.isdir(city_back_folder):
                os.mkdir(city_back_folder)
            t=threading.Thread(target=city2db, args=(path.join(data_folder,job_category, city), city)) 
            t.start()
                
if __name__=='__main__':
    main()