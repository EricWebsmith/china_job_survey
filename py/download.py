# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:10:20 2019

@author: eric
"""

from os import mkdir
from os import path
import re

from urllib.request import urlretrieve
from requests import get
from bs4 import BeautifulSoup
import threading
from config import year, month, zhinengleibies


data_folder = f'../../data/51jobs_{year}{month:02}/'

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
    }



def main():
    #city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan','chongqing','chengdu','changsha','fuzhou','hefei','ningbo','zhengzhou','tianjin','qingdao','jinan','kuming','shenyang','xian','dongguan','dalian','harbin','changchun']
    #city_codes=['010000','020000','030200','040000','080200','070200','180200','060000','090200','190200','110200','150200','080300','170200','050000','120300','120200','250200','230200','200200','030800','230300','220200','240200']
    
    provinces = {}
    provinces['北京'] = '010000'
    provinces['上海'] = '020000'
    provinces['广东'] = '030000'
    provinces['深圳'] = '040000'
    provinces['天津'] = '050000'
    provinces['重庆'] = '060000'
    provinces['江苏'] = '070000'
    provinces['浙江'] = '080000'
    provinces['四川'] = '090000'
    provinces['海南'] = '100000'
    provinces['福建'] = '110000'
    provinces['山东'] = '120000'
    provinces['江西'] = '130000'
    provinces['广西'] = '140000'
    provinces['安徽'] = '150000'
    provinces['河北'] = '160000'
    provinces['河南'] = '170000'
    provinces['湖北'] = '180000'
    provinces['湖南'] = '190000'
    provinces['陕西'] = '200000'
    provinces['山西'] = '210000'
    provinces['黑龙江'] = '220000'
    provinces['辽宁'] = '230000'
    provinces['吉林'] = '240000'
    provinces['云南'] = '250000'
    provinces['贵州'] = '260000'
    provinces['甘肃'] = '270000'
    provinces['内蒙古'] = '280000'
    provinces['宁夏'] = '290000'
    provinces['西藏'] = '300000'
    provinces['新疆'] = '310000'
    provinces['青海'] = '320000'


    #make sure this folder is created
    
    def download_pages(links, folder):
        for link in links:
            try:
                if not link.startswith("https://jobs.51job.com/"):
                    continue
                filename = path.split(link)[-1]
                filename = filename.split('?')[0]
                destination_file = path.join(folder, filename)
                if not path.isfile(destination_file):
                    #print(link)
                    t = threading.Thread(target=urlretrieve, args=(link, path.join(folder, filename)))
                    t.start()
                    #urlretrieve(link, path.join(folder, filename))
                    
            except Exception as e:
                print(str(e))
                pass
            
    #0100是软件，2500是互联网

    
    #categories['']=''
    #categories['']=''
    for category_key, category_name in zhinengleibies.items():
        job_category_folder = path.join(data_folder, category_name)
        if not path.isdir(job_category_folder):
            mkdir(job_category_folder)
        for province_name, province_code in provinces.items():
            #create forlder
            province_folder = path.join(job_category_folder, province_name)
            if not path.isdir(province_folder):
                mkdir(province_folder)
            #links -
            #first page
            first_page_url = f'https://search.51job.com/list/{province_code},000000,{category_key},00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            #print(first_page_url)
            first_page = urlretrieve(first_page_url)
            #first_page.encoding = 'gb2312'
            soup = BeautifulSoup(open(first_page[0], encoding='gbk'),"html.parser")
            #page_count_string='共328页，到第'
            page_count_string = soup.select_one(".p_in .td").text
            re_result = re.match(r'共(\d+)页，到第',page_count_string)
            total_page = int(re_result.group(1))
            print(f'{province_name} has {total_page} pages for {category_name}')
            



            for page_index in range(1,total_page):
                #'https://sou.zhaopin.com/?jl=530&sf=0&st=0&jt=23,160000,045'
                list_url = 'https://search.51job.com/list/{0},000000,{1},00,9,99,%2B,2,{2}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(province_code, category_key, page_index)
                try:
                    list_page = urlretrieve(list_url)
                    #list_page.encoding = 'gb2312'
                    #soup = BeautifulSoup(list_page.text,"html.parser")
                    soup = BeautifulSoup(open(list_page[0], encoding='gbk'),"html.parser")
                    #get list page
                    links = [tag.attrs['href'] for tag in soup.select(".t1 a")]
                    download_pages(links, province_folder)
                except Exception as err:
                    print(err)
                    print(list_url)

if __name__ == '__main__':
    main()



#beijing page 1 %25=%
#https://search.51job.com/list/010000,000000,0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#shanghai page 1 %25=%
#https://search.51job.com/list/020000,000000,0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#guangzhou page 1
#https://search.51job.com/list/030200,000000,0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#shenzhen page 1
#https://search.51job.com/list/040000,000000,0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#hangzhou page 1
#https://search.51job.com/list/080200,000000,0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=

#beijing page 2 %2B=+
#https://search.51job.com/list/010000,000000,0100,00,9,99,%2B,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#https://search.51job.com/list/010000,000000,0100,00,9,99,%2B,2,3.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=

#beijiang page 1
#https://search.51job.com/list/010000,000000,0100,00,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=


