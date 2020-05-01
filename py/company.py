# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:26:35 2020

@author: eric
"""

from requests import get
from bs4 import BeautifulSoup

class Company():

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

def get_company_tags(company_link):
    response=get(company_link)
    response.encoding='gbk'
    soup=BeautifulSoup(response.text, 'html.parser')
    ltype_tag=soup.select_one('.ltype')
    if not ltype_tag:
        return []
    info_string=ltype_tag.text
    return [info.strip() for info in info_string.split('|')]

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

    #<span class="bname">公司信息</span>
    company_info_tag=soup.find('span',text='公司信息')
    if company_info_tag:
        job.company_description=company_info_tag.parent.find_next('div').text.replace('\xa0',' ').strip()

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