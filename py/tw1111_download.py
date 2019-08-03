# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:10:20 2019

@author: eric
"""

from os import chdir
from os import mkdir
from os import path
import re

from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import threading

chdir("D:/projects/51job_survey/51job_survey_py/py")

data_folder = '../../data/tw1111_201906/'

url='https://www.1111.com.tw/job-bank/job-index.asp?tt=1&c0=100100,100600,100200,100700,100300,100800,100500,101300,101800,101200,101600,101100,101500,100900,101400,102000,102200,102100,100400,102300,102400,102500&d0=140207,140202,140213,140214,140212,140203&fs=1&si=1&ts=1&ps=30&page=1'
url_no_page='https://www.1111.com.tw/job-bank/job-index.asp?tt=1&c0=100100,100600,100200,100700,100300,100800,100500,101300,101800,101200,101600,101100,101500,100900,101400,102000,102200,102100,100400,102300,102400,102500&d0=140207,140202,140213,140214,140212,140203&fs=1&si=1&ts=1&ps=30&page='

def download_pages(links, folder):
    for link in links:
        try:
            if not '//www.1111.com.tw/job/' in link:
                continue
            #https://www.1111.com.tw/job/85948633/
            

            filename = link.split('?')[0]
            no = filename.replace('//www.1111.com.tw/job/','').replace('/','')
            filename=no+".html"
            destination_file = path.join(folder, filename)
            if not path.isfile(destination_file):
                print(link)
                urlretrieve("https:"+link,path.join(folder, filename))
                #t = threading.Thread(target=urlretrieve, args=("https:"+link, path.join(folder, filename)))
                #t.start()
                #urlretrieve(link, path.join(folder, filename))
                    
        except Exception as e:
            print(str(e))
            pass

headers={
    "Referer":"http://www.yanglee.com/Product/Index.aspx",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }


first_page_url = url

s = requests.Session()
s.headers = headers
first_page = s.get(first_page_url)

first_page.encoding = 'utf-8'
soup = BeautifulSoup(first_page.text,"html.parser")
#page_count_string='共328页，到第'
page_count_string = soup.select_one(".pagedata").text
re_result = re.match(r'第 1 / (\d+) 頁',page_count_string)
total_page = int(re_result.group(1))
links = [tag.attrs['href'] for tag in soup.select(".jbInfoin h3 a")]
download_pages(links, data_folder)

for page_index in range(2,total_page):
    print(page_index)
    list_url = url_no_page+str(page_index)
    print(list_url)
    list_page = s.get(list_url)
    list_page.encoding = 'utf-8'
    soup = BeautifulSoup(list_page.text,"html.parser")
    #with open(path.join(data_folder, f"list_{page_index}.html"), mode='w', encoding='utf-8') as f:
    #    f.write(list_page.text)
    links = [tag.attrs['href'] for tag in soup.select(".jbInfoin h3 a")]
    download_pages(links, data_folder)
