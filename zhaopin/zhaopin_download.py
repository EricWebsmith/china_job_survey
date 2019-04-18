# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:10:20 2019

@author: eric
"""

from os import mkdir
from os import path
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


def main():
    city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan','chongqing','chengdu','changsha']
    city_codes=['530','538','763','765','653','635','736','551','801','749']
    data_folder = '../data/'
    
    software_engineer={"value":"160000","parent":"23","label":"软件/互联网开发/系统集成","children":[{"value":"044","parent":"160000","label":"高级软件工程师","children":[]},{"value":"045","parent":"160000","label":"软件工程师","children":[]},{"value":"079","parent":"160000","label":"软件研发工程师","children":[]},{"value":"665","parent":"160000","label":"需求工程师","children":[]},{"value":"667","parent":"160000","label":"系统架构设计师","children":[]},{"value":"668","parent":"160000","label":"系统分析员","children":[]},{"value":"047","parent":"160000","label":"数据库开发工程师","children":[]},{"value":"048","parent":"160000","label":"ERP技术/开发应用","children":[]},{"value":"053","parent":"160000","label":"互联网软件工程师","children":[]},{"value":"679","parent":"160000","label":"手机软件开发工程师","children":[]},{"value":"687","parent":"160000","label":"嵌入式软件开发","children":[]},{"value":"863","parent":"160000","label":"移动互联网开发","children":[]},{"value":"864","parent":"160000","label":"WEB前端开发","children":[]},{"value":"317","parent":"160000","label":"语音/视频/图形开发","children":[]},{"value":"669","parent":"160000","label":"用户界面（UI）设计","children":[]},{"value":"861","parent":"160000","label":"用户体验（UE/UX）设计","children":[]},{"value":"054","parent":"160000","label":"网页设计/制作/美工","children":[]},{"value":"057","parent":"160000","label":"游戏设计/开发","children":[]},{"value":"671","parent":"160000","label":"游戏策划","children":[]},{"value":"672","parent":"160000","label":"游戏界面设计","children":[]},{"value":"666","parent":"160000","label":"系统集成工程师","children":[]},{"value":"2034","parent":"160000","label":"算法工程师","children":[]},{"value":"2035","parent":"160000","label":"仿真应用工程师","children":[]},{"value":"2036","parent":"160000","label":"计算机辅助设计师","children":[]},{"value":"2037","parent":"160000","label":"网站架构设计师","children":[]},{"value":"2038","parent":"160000","label":"IOS开发工程师","children":[]},{"value":"2039","parent":"160000","label":"Android开发工程师","children":[]},{"value":"2040","parent":"160000","label":"Java开发工程师","children":[]},{"value":"2041","parent":"160000","label":"PHP开发工程师","children":[]},{"value":"2042","parent":"160000","label":"C语言开发工程师","children":[]},{"value":"2043","parent":"160000","label":"脚本开发工程师","children":[]},{"value":"060","parent":"160000","label":"其他","children":[]}]}
    
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    
    driver = webdriver.Firefox(options=firefox_options)
    wait = WebDriverWait(driver, 10)
    
    
    def get_links():
        links=[]
        contentpile = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'contentpile')))[0]
        #等待0.2秒，否则contentpile对象的子对象还没有加载。
        sleep(0.2)
        #when no jobs are found, this class will be shown
        if len(contentpile.find_elements_by_class_name('contentpile__jobcontent__notext'))>0:
            return links
        #when jobs are found, this class will be shown
        listContent = wait.until(EC.presence_of_all_elements_located((By.ID, 'listContent')))[0]
        a_tags=listContent.find_elements_by_tag_name("a")
        for a_tag in a_tags:
                link = a_tag.get_attribute("href")
                if 'jobs.zhaopin.com' in link:
                    links.append(link)
        return links

    #download job pages
    def download_pages(links, folder):
        for link in links:        
            filename = path.split(link)[-1]
            filename = filename.split('?')[0]
            destination_file=path.join(folder, filename)
            if path.isfile(destination_file):
                continue
            driver.get(link)

            with open(destination_file, mode='w',encoding='utf-8') as f:
#                content = driver.page_source
#                #修改charset，否则很多软件打开文件会出现乱码。
#                content = content.replace('text/html; charset=gb2312','text/html; charset=utf-8')
                f.write(driver.page_source)
                f.flush()
                f.close()
    
    for city_index in range(7,10):
        city_folder = path.join(data_folder, city_names[city_index])
        if not path.isdir(city_folder):
            mkdir(city_folder)
        for page_index in range(1,13):
            #'https://sou.zhaopin.com/?jl=530&sf=0&st=0&jt=23,160000,045'
            list_url='https://sou.zhaopin.com/?p={0}&jl={1}&sf=0&st=0&jt=23,160000,045'.format(page_index, city_codes[city_index])
            print(list_url)
            driver.get(list_url)
            links=get_links()
            download_pages(links, city_folder)


    
if __name__=='__main__':
    main()