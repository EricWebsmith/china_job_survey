# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:10:20 2019

@author: eric
"""
import sys
from os import mkdir
from os import path
import re

from urllib.request import urlretrieve,urlopen
from urllib.error import HTTPError
from requests import get
from bs4 import BeautifulSoup
import threading
from config import year, month#, zhinengleibies, provinces
import config

import gc
from contextlib import closing

import threading

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()
chromeOptions.headless = True
chrome=webdriver.chrome.webdriver.WebDriver(options=chromeOptions)


data_folder = f'../../data/51jobs_{year}{month:02}/'

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
    }

def new_urlopen(url): # request without memory leak
    res = None
    with closing(urlopen(url)) as resp:
        res = resp.read()
    return res

def main(reverse=False):
    #city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan','chongqing','chengdu','changsha','fuzhou','hefei','ningbo','zhengzhou','tianjin','qingdao','jinan','kuming','shenyang','xian','dongguan','dalian','harbin','changchun']
    #city_codes=['010000','020000','030200','040000','080200','070200','180200','060000','090200','190200','110200','150200','080300','170200','050000','120300','120200','250200','230200','200200','030800','230300','220200','240200']
    my_provinces = config.provinces.items()
    my_zhinengleibies = config.zhinengleibies.items()
    if reverse:
        my_provinces = list(config.provinces.items())[::-1]
        my_zhinengleibies = list(config.zhinengleibies.items())[::-1]

    #make sure this folder is created

    def download_thread(link, destination_file):
        try:
            #image_url = "https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png"
            response = urlopen(link)
            #bytes = response.read()

            with open(destination_file, "wb") as f:
                f.write(response.read())
                f.close()

        except HTTPError as hErr:
            if hErr.code == 404:
                print(f"404 {link}")
            else:
                print(str(hErr))
        except Exception as err:
            print(str(err))
    
    def download_pages_thread(links, folder):
        for link in links:
            #print(link)
            if link is None:
                continue
            if not link.startswith("https://jobs.51job.com/"):
                continue
            if link.startswith("https://jobs.51job.com/all/co"):
                continue
            if len(link)<30:
                continue
            print(link)
            filename = path.split(link)[-1]
            filename = filename.split('?')[0]
            destination_file = path.join(folder, filename)
            if path.exists(destination_file):
                continue

            download_thread(link, destination_file)

    # def download_pages(links, folder):
    #     for link in links:
    #         if not link.startswith("https://jobs.51job.com/"):
    #             continue
    #         filename = path.split(link)[-1]
    #         filename = filename.split('?')[0]
    #         destination_file = path.join(folder, filename)
    #         #urlretrieve(link, destination_file)
    #         if not path.isfile(destination_file):
    #             t = threading.Thread(target=download_thread, args=(link, destination_file))
    #             t.start()

    for category_key, category_name in my_zhinengleibies:
        job_category_folder = path.join(data_folder, category_name)
        if not path.isdir(job_category_folder):
            mkdir(job_category_folder)
        for province_name, province_code in my_provinces:
            #create forlder
            province_folder = path.join(job_category_folder, province_name)
            if not path.isdir(province_folder):
                mkdir(province_folder)
            #links -
            #first page
            first_page_url = f'https://search.51job.com/list/{province_code},000000,{category_key},00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
            print(first_page_url)
            chrome.get(first_page_url)
            time.sleep(10)
            p_in=chrome.find_element_by_class_name("p_in")
            p_in_td=p_in.find_element_by_class_name("td")
            page_count_string = p_in_td.text
            print(page_count_string)
            if page_count_string == '':
                print(f'{province_name} 没有 {category_name}')
                continue
            #print(first_page_url)
            #first_page = urlretrieve(first_page_url)
            #first_page.encoding = 'gb2312'
            #soup = BeautifulSoup(urlopen(first_page_url).read().decode('gbk'),"html.parser")
            #text = soup.text
            #page_count_string='共328页，到第'
            #page_count_string = soup.select_one(".p_in .td").text
            re_result = re.match(r'共\s(\d+)\s页',page_count_string)
            total_page = int(re_result.group(1))
            print(f'{province_name} has {total_page} pages for {category_name}')
            
            for page_index in range(0,total_page):
                #'https://sou.zhaopin.com/?jl=530&sf=0&st=0&jt=23,160000,045'
                list_url = f'https://search.51job.com/list/{province_code},000000,{category_key},00,9,99,%2B,2,{page_index+1}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
                try:
                    #list_page = urlretrieve(list_url)
                    #list_page.encoding = 'gb2312'
                    #soup = BeautifulSoup(list_page.text,"html.parser")
                    chrome.get(list_url)
                    time.sleep(10)
                    link_tags=chrome.find_elements_by_tag_name("a")
                    links = []
                    print(f"link tags {len(link_tags)}")
                    link_count = 0
                    try:
                        for link_tag in link_tags:
                            #href = WebDriverWait(chrome, 20).until(EC.visibility_of_element_located(link_tag)).get_attribute("href")
                            #attribute_value = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.ID, "org"))).get_attribute("attribute_name")
                            href = link_tag.get_attribute("href")
                            links.append(href)
                            link_count+=1
                            #print(link_count)
                        print(link_count)
                        print(f"links {len(links)}")
                    except:
                        pass
                    # with urlopen(list_url) as f:
                    #     soup = BeautifulSoup(f.read().decode('gbk'),"html.parser")
                        
                    #     f.close()

                    #get list page
                    #links = [tag.attrs['href'] for tag in soup.select(".t1 a")]
                    #del f
                    #del soup
                    
                    download_pages_thread(links, province_folder)
                    # t_list = []
                    # t = threading.Thread(target=download_pages_thread, args=(links, province_folder))
                    # t_list.append(t)
                    # t.start()

                    # for t in t_list:
                    #     t.join()
                    

                    # del t_list
                    
                    gc.collect()

                except Exception as err:
                    print(err)
                    print(list_url)

if __name__ == '__main__':
    if len(sys.argv)>1:
        print("you are using reverse.")
        main(reverse=True)
    else:
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


#beijing blockchain
#https://search.51job.com/list/010000,000000,0128,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
#https://search.51job.com/list/010000,000000,0128,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=