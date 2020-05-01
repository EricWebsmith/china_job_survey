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
#from icu996companies import icu996companies, non996companies
import pandas as pd
from db import get_conn

from config import year, month, company_blacklist, title_key_blacklist
year_month=f'{year}{month:02}'

class Job():
    #basic info
    job_id=""
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
    
    #职能类别 软件工程师 算法工程师 系统架构设计师
    zhinengleibie=''

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
    
    
    province=''
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

def file2job(file, zhinengleibie, province):
    job=Job()
    job.zhinengleibie=zhinengleibie

    if province=='深圳':
        job.province='广东'
    else:
        job.province=province

    job.job_id=path.split(file)[-1].replace(".html","")
    
    if job.job_id in ['110455749','77612262','107681687']:
        return None
    
    #page title


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
    title_tag=soup.select_one('title')
    if not title_tag:
        return None
    job.page_title=title_tag.text
    if '异地招聘' in job.page_title:
        return None
    #职业 start
    #首先判断职业，如果职业不是程序员，直接pass
    zhineng_tag=soup.find('span',{'class':'label'},text='职能类别：')
    if not zhineng_tag:
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
                headcount_string='5'
            job.headcount=int(headcount_string)
    
        if info.endswith('发布'):
    
            #date
            date_string="2020-"+info.replace("发布",'')
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
    

        
    job.get_programming_languages(job_description_lower) \
        .get_databases(job_description_lower) \
        .get_big_data_stats(job_description_lower) \
        .get_machine_learning_stats(job_description_lower) 
    

    #如果招聘信息本身都是英语写的，那么肯定要求英语
    if is_article_english(job_description_lower):
        job.english=True

    
    #<span class="bname">公司信息</span>
    company_info_tag=soup.find('span',text='公司信息')
    if company_info_tag:
        job.company_description=company_info_tag.parent.find_next('div').text.replace('\xa0',' ').strip()
    company_title_tag=soup.select_one('.com_name')
    if not company_title_tag:
        company_title_tag=soup.select_one('.catn')
    job.company_title=company_title_tag.text.strip()
    #['民营公司', '150-500人', '服装/纺织/皮革']
    company_tags=[p.text.strip() for p in soup.select('.com_tag .at')]
    
    if len(company_tags)>0:
        job.get_company_type(company_tags[0])
    if job.company_type=='':
        company_link=company_title_tag.attrs['href']
        company_tags=get_company_tags(company_link)
        for tag in company_tags:
            if job.get_company_type(tag).check_company_type():
                break 

    if job.company_type=='':
        return None
    
    job.get_company_size(company_tags[1])
    if not job.check_company_size():
        company_link=company_title_tag.attrs['href']
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
    
    #black named companies
    if job.company_title in company_blacklist:
        return None
#    if not job.check_industry():
#        raise Exception("no industry")
        
    
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
    
    exists=conn.execute("select count(1) from _{} where job_id='{}'".format(year_month, job_id)).fetchall()[0][0]
    if exists:
        try_rename(file)
        return
    print(file)
    job=file2job(file, zhinengleibie, province)
    if not job:
        try_rename(file)
        return
    
    data=pd.DataFrame(columns=get_featurenames(job))
    l=object2list(job)
    data.loc[job.job_id]=l
    data.to_sql("_"+year_month,conn,if_exists="append", index=False)

    conn.close()
    try_rename(file)   

def city2db(data_folder,zhinengleibie, province):
    city_folder=path.join(data_folder,zhinengleibie, province)
    files = glob(path.join(city_folder,"*.html"))
    for file in files:
        file2db(file, zhinengleibie, province) 

def main():
    provinces=['北京','上海','广东','深圳','天津','重庆','江苏','浙江','四川','海南','福建','山东','江西','广西','安徽','河北','河南','湖北','湖南','陕西','山西','黑龙江','辽宁','吉林','云南','贵州','甘肃','内蒙古','宁夏','西藏','新疆','青海']
    data_folder = '../../data/51jobs_{}/'.format(year_month)
    back_folder = '../../data/51jobs_{}_b/'.format(year_month)
    zhinengleibies=['高级软件工程师', '软件工程师','算法工程师','机器学习工程师','深度学习工程师','图像算法工程师','图像处理工程师','语音识别工程师','图像识别工程师','机器视觉工程师','自然语言处理（NLP）','系统架构设计师','互联网软件开发工程师','手机应用开发工程师','网站架构设计师']
    for zhinengleibie in zhinengleibies:
        category_back_folder=path.join(back_folder, zhinengleibie)
        if not path.isdir(category_back_folder):
            os.mkdir(category_back_folder)
        for province in provinces:
            city_back_folder=path.join(category_back_folder, province)
            if not path.isdir(city_back_folder):
                os.mkdir(city_back_folder)

            city2db(data_folder, zhinengleibie, province)
            #t=threading.Thread(target=city2db, args=(path.join(data_folder,job_category, city), city)) 
            #t.start()

if __name__=='__main__':
    #global year_month

    main()
