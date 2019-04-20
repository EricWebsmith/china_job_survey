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
    
    #职能类别 软件工程师 算法工程师 系统架构设计师
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
    expert_expert=False
    expert_blockchain=False
    expert_adas=False
    expert_embed=False
    expert_gis=False
    
    city=''
    #languages
    english=False
    japanese=False
    #company_info
    company_title=""
    
    company_description=""
    #外资(欧美)
    #外资(非欧美)
    #合资
    #国企
    #民营公司
    #外企代表处
    #政府机关
    #事业单位
    #非营利组织
    #上市公司
    #创业公司
    company_type=''



    #少于50人
    #50-150人
    #150-500人
    #500-1000人
    #1000-5000人
    #5000-10000人
    #10000人以上
    company_size=''

    #计算机/互联网/通信/电子
    #会计/金融/银行/保险
    #贸易/消费/制造/营运
    #制药/医疗
    #广告/媒体
    #房地产/建筑
    #专业服务/教育/培训
    #服务业
    #物流/运输
    #能源/原材料
    #政府/非营利组织/其他
    industry=''
    

    
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

    def check_company_size(self):
        return not self.company_size==''
        
    def get_company_size(self, tag):
        if (tag=='少于50人'):
            self.company_size='50-'
        elif (tag=='50-150人'):
            self.company_size='50-150'
        elif (tag=='150-500人'):
            self.company_size='150-500'
        elif (tag=='500-1000人'):
            self.company_size='500-1000'
        elif (tag=='1000-5000人'):
            self.company_size='1000-5000'
        elif (tag=='5000-10000人'):
            self.company_size='5000-10000'
        elif (tag=='10000人以上'):
            self.company_size='10000+'
        return self
        
    def get_company_type(self, tag):
        if tag in ['外资（欧美）','外资（非欧美）','合资','国企','民营公司','外企代表处','政府机关','事业单位','非营利组织','上市公司''创业公司']:
            self.company_type=tag
        return self

    def check_company_type(self):
        return not self.company_type==''
        
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
        return not self.industry==''

    def get_industry(self, industry_tag):
        if industry_tag in ['计算机软件','计算机硬件','计算机服务(系统、数据服务、维修)','通信/电信/网络设备','通信/电信运营、增值服务','互联网/电子商务','网络游戏','电子技术/半导体/集成电路','仪器仪表/工业自动化']:
            self.industry='computer'
        #会计/金融/银行/保险
        if industry_tag in ['会计/审计','金融/投资/证券','银行','保险','信托/担保/拍卖/典当']:
            self.industry='finance'
        #贸易/消费/制造/营运
        if industry_tag in ['贸易/进出口','批发/零售','快速消费品(食品、饮料、化妆品)','服装/纺织/皮革','家具/家电/玩具/礼品','奢侈品/收藏品/工艺品/珠宝','办公用品及设备','机械/设备/重工','汽车及零配件']:
            self.industry='trade'
        #制药/医疗
        if industry_tag in ['制药/生物工程','医疗/护理/卫生','医疗设备/器械']:
            self.industry='medical'
        #广告/媒体
        if industry_tag in ['广告','公关/市场推广/会展','影视/媒体/艺术/文化传播','文字媒体/出版','印刷/包装/造纸']:
            self.industry='ads'
        #房地产/建筑
        if industry_tag in ['房地产','建筑/建材/工程','家居/室内设计/装潢','物业管理/商业中心']:
            self.industry='realestate'
        #专业服务/教育/培训
        if industry_tag in ['中介服务','专业服务(咨询、人力资源、财会)','外包服务','检测，认证','法律','教育/培训/院校','学术/科研','租赁服务']:
            self.industry='edu'
        #服务业
        if industry_tag in ['餐饮业','酒店/旅游','娱乐/休闲/体育','美容/保健','生活服务']:
            self.industry='service'
        #物流/运输
        if industry_tag in ['交通/运输/物流','航天/航空']:
            self.industry='logistic'
        #能源/原材料
        if industry_tag in ['石油/化工/矿产/地质','采掘业/冶炼','电气/电力/水利','新能源','原材料和加工']:
            self.industry='energy'
        #政府/非营利组织/其他
        if industry_tag in ['政府/公共事业','非营利组织','环保','农/林/牧/渔','多元化业务集团公司']:
            self.industry='gov'
        return self
            
    def check_all(self, raise_exception=False):
#        if not self.check_company_size():
#            raise Exception("check_company_size")
        if raise_exception:
            if self.company_type=='':
                raise Exception("check_company_type")
            if self.industry=='':
                raise Exception("check_industry")
            if self.experience=='':
                raise Exception("check_working_experience")


def in_996_list(company_title):
    return any(icu996 in company_title for icu996 in icu996companies)

def in__996_no_list(company_title):
    return any(non996 in company_title for non996 in non996companies)

def printObject(o):
    print(inspect.getmembers(o))

def get_company_tags(company_link):
    response=get(company_link)
    response.encoding='gbk'
    soup=BeautifulSoup(response.text, 'html.parser')
    ltype_tag=soup.select_one('.ltype')
    if not ltype_tag:
        return []
    info_string=ltype_tag.text
    return [info.strip() for info in info_string.split('|')]

def file2job(file, city):
    job=Job()
    job.city=city
    job.job_id=path.split(file)[-1].replace(".html","")
    
    if job.job_id in ['110455749','77612262','107681687']:
        return None
    
    #print(file)
    content=""
    try:
        with open(file, mode='r',encoding='gbk') as f:
            content=f.read()
            f.close()
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
        return None

    
    soup=BeautifulSoup(content, "html.parser")
    
    #职业 start
    #首先判断职业，如果职业不是程序员，直接pass
    #career=soup.find('span',{'class':'label'},text='职能类别：').find_next('a').text.strip()
    zhineng_tag=soup.find('span',{'class':'label'},text='职能类别：')
    if not zhineng_tag:
        return None
    careers=[a_tag.text.strip() for a_tag in zhineng_tag.parent.find_all('a')]
    for career in careers:
        if (career in ['软件工程师','高级软件工程师','ERP技术开发','互联网软件开发工程师','多媒体/游戏开发工程师','手机应用开发工程师','WEB前端工程师','脚本开发工程师','语音/视频/图形开发工程师']):
            job.career='一般程序员'
        if career=='算法工程师':
            job.career='算法工程师'
        if career in ['系统架构设计师','网站架构设计师']:
            job.career='系统架构师'

    if '爬虫' in job.title:
        job.career='爬虫工程师'

    if '生物信息' in job.title:
        job.career='生物信息工程师'

    if job.career=='':
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

    if any(key in job.title for key in ['测试','前端','信息工程师','运维','经理','嵌入式','讲师','老师','负责人','合伙人','计算机技术员','主任','总监','cto','需求工程师','需求分析','系统集成工程师','系统工程师','系统分析师','计算机辅助设计','DBA','实施','售前','售后','数据库']):
        return None
    
    job_title_lower=job.title.lower()
    if '专家' in job_title_lower:    
        expert_expert=False
    if 'blockchain' in job_title_lower or '区块链' in job_title_lower:
        expert_blockchain=False
    if 'adas' in job_title_lower:
        expert_adas=False
    if '嵌入式' in job_title_lower:
        expert_embed=False
    if 'gis' in job_title_lower:
        expert_gis=False


    #'深圳-福田区|5-7年经验|本科|招1人|04-01发布'
    job.job_summary=soup.select_one(".msg").text.replace('\xa0','').replace(' ','').strip()
    #print(basic_info)
    infos=job.job_summary.split('|')
    
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
                headcount_string='5'
            job.headcount=int(headcount_string)
    
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
    job.job_tags=','.join(tags)
    job.get_tags(tags)
    
    h2_span=soup.select_one('h2 span')
    job.job_description=h2_span.parent.find_next('div').text.strip()
    job_description_lower=job.job_description.lower()
    job_description_lower=job.title+" "+job_description_lower
    
    #年龄歧视
    job.ageism='岁' in job.job_description
    

    #继续判断是不是架构师
    #if '架构师' in job_description_lower:
    #    job.career='系统架构师'
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
        job.career='算法工程师'        

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
    if job.company_type=='':
        company_link=soup.select_one('.com_name').attrs['href']
        company_tags=get_company_tags(company_link)
        for tag in company_tags:
            if job.get_company_type(tag).check_company_type():
                break 

    if job.company_type=='':
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
        job.industry='computer'
    if job.company_title=='软件与服务中心':
        job.industry='trade'
    if job.company_title== '中核集团技术经济总院':
        job.industry='energy'
    
#    if not job.check_industry():
#        raise Exception("no industry")
        
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
    if in_996_list(job.company_title):
        job._996_yes=True
    if in__996_no_list(job.company_title):
        job._996_no=True
    if job.published_on_weekend:
        job._996_yes=True
    
    return job

def try_rename(file):
    new_file=file.replace("51jobs","51jobs_b")
    if path.isfile(new_file):
        os.remove(file)
    else:
        os.rename(file, new_file) 

def file2db(file, city):
    conn=get_conn()

        
    filename=path.split(file)[-1]
    job_id=filename.replace(".html","")           
    
    exists=conn.execute("select count(1) from _201904v2 where job_id='{0}'".format(job_id)).fetchall()[0][0]
    if exists:
        try_rename(file)
        return
    print(file)
    job=file2job(file, city)
    if not job:
        try_rename(file)
        return
    
    data=pd.DataFrame(columns=get_featurenames(job))
    l=object2list(job)
    data.loc[job.job_id]=l
    data.to_sql("_201904v2",conn,if_exists="append", index=False)

    conn.close()
    try_rename(file)   

def city2db(city_folder, city):
    files = glob(path.join(city_folder,"*.html"))
    for file in files:
        file2db(file, city) 
    
def main():
    city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing', \
                'wuhan','chongqing','chengdu','changsha','fuzhou','hefei','ningbo',\
                'zhengzhou','tianjin','qingdao','jinan','kunming','shenyang','xian',\
                'dongguan','dalian','harbin','changchun']
    #city_names=['shanghai']
    data_folder = '../data/51jobs/'
    back_folder = '../data/51jobs_b/'
    for job_category in ['0100','2500']:
        category_back_folder=path.join(back_folder, job_category)
        if not path.isdir(category_back_folder):
            os.mkdir(category_back_folder)
        for city in city_names:
            city_back_folder=path.join(category_back_folder, city)
            if not path.isdir(city_back_folder):
                os.mkdir(city_back_folder)
            city2db(path.join(data_folder,job_category, city), city)
            #t=threading.Thread(target=city2db, args=(path.join(data_folder,job_category, city), city)) 
            #t.start()
                
if __name__=='__main__':
    main()