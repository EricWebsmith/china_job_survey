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




def main():
    city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan','chongqing','chengdu','changsha','fuzhou','hefei','ningbo','zhengzhou','tianjin','qingdao','jinan','kuming','shenyang','xian','dongguan','dalian','harbin','changchun']
    city_codes=['010000','020000','030200','040000','080200','070200','180200','060000','090200','190200','110200','150200','080300','170200','050000','120300','120200','250200','230200','200200','030800','230300','220200','240200']
    #make sure this folder is created
    data_folder = '../data/51jobs/'
    

    def download_pages(links, folder):
        for link in links:
            try:
                if not link.startswith("https://jobs.51job.com/"):
                    continue
                filename=path.split(link)[-1]
                filename=filename.split('?')[0]
                destination_file=path.join(folder, filename)
                if not path.isfile(destination_file):
                    print(link)
                    t = threading.Thread(target=urlretrieve, args=(link, path.join(folder, filename)))
                    t.start()
                    #urlretrieve(link, path.join(folder, filename))
                    
            except Exception as e:
                print(str(e))
                pass
            
    #0100是软件，2500是互联网
    for job_category in ['2500','0100']:
        job_category_folder=path.join(data_folder, job_category)
        if not path.isdir(job_category_folder):
            mkdir(job_category_folder)
        for city_index in range(len(city_names)):
            #create forlder
            city_folder = path.join(job_category_folder, city_names[city_index])
            if not path.isdir(city_folder):
                mkdir(city_folder)
            #links - 
            #first page
            first_page_url='https://search.51job.com/list/{0},000000,{1},00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(city_codes[city_index], job_category)
            first_page=get(first_page_url)
            first_page.encoding='gb2312'
            soup=BeautifulSoup(first_page.text,"html.parser")
            #page_count_string='共328页，到第'
            page_count_string=soup.select_one(".p_in .td").text
            re_result=re.match(r'共(\d+)页，到第',page_count_string)
            total_page = int(re_result.group(1))
            print("{0} has {1} pages".format(city_names[city_index], total_page))
            links=[tag.attrs['href'] for tag in soup.select(".t1 a") if tag.attrs['href'].startswith("https://jobs.51job.com/")]
            download_pages(links, city_folder)
            
    
            
            for page_index in range(2,total_page):
                #'https://sou.zhaopin.com/?jl=530&sf=0&st=0&jt=23,160000,045'
                list_url='https://search.51job.com/list/{0},000000,{1},00,9,99,%2B,2,{2}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(city_codes[city_index], job_category, page_index)
                list_page=get(list_url)
                list_page.encoding='gb2312'
                soup=BeautifulSoup(list_page.text,"html.parser")
                #get list page
                links=[tag.attrs['href'] for tag in soup.select(".t1 a")]
                download_pages(links, city_folder)
    
if __name__=='__main__':
    main()