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

def main(data_folder):

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
                    print(link)
                    t = threading.Thread(target=urlretrieve, args=(link, path.join(folder, filename)))
                    t.start()
                    #urlretrieve(link, path.join(folder, filename))
                    
            except Exception as e:
                print(str(e))
                pass
            
    #0100是软件，2500是互联网
    company_sizes=['01','02','03','04','05','06','07']
    #categories['']=''
    #categories['']=''
    for province_name, province_code in provinces.items():
        for company_size in company_sizes:
            #create forlder
            province_folder = path.join(data_folder, province_name)
            if not path.isdir(province_folder):
                mkdir(province_folder)
            #links -
            #first page
            first_page_url = 'https://search.51job.com/list/{0},000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize={1}&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(province_code, company_size)
            first_page = get(first_page_url)
            first_page.encoding = 'gb2312'
            soup = BeautifulSoup(first_page.text,"html.parser")
            #page_count_string='共328页，到第'
            page_count_string = soup.select_one(".p_in .td").text
            re_result = re.match(r'共(\d+)页，到第',page_count_string)
            total_page = int(re_result.group(1))
            print("{0} has {1} pages".format(province_name, total_page))
            links = [tag.attrs['href'] for tag in soup.select(".t1 a") if tag.attrs['href'].startswith("https://jobs.51job.com/")]
            download_pages(links, province_folder)

            for page_index in range(2,total_page):
                #'https://sou.zhaopin.com/?jl=530&sf=0&st=0&jt=23,160000,045'
                list_url = 'https://search.51job.com/list/{0},000000,0000,00,9,99,%2B,2,{2}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize={1}&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(province_code, company_size, page_index)
                list_page = get(list_url)
                list_page.encoding = 'gb2312'
                soup = BeautifulSoup(list_page.text,"html.parser")
                #get list page
                els_tags = soup.select('.el')

                links = [tag.attrs['href'] for tag in soup.select(".t1 a")]
                download_pages(links, province_folder)

    
if __name__ == '__main__':
    data_folder = '../data/51jobs_all_20190511/'
    main(data_folder)



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


