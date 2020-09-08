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