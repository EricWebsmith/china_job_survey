# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:48:39 2019

@author: eric
"""
from os import path
from bs4 import BeautifulSoup
from glob import glob

city_names=['beijing','shanghai','guangzhou','shenzhen','hangzhou','nanjing','wuhan','chongqing','chengdu','changsha']
city_codes=['530','538','763','765','653','635','736','551','801','749']
data_folder = '../data/'

for city in city_names[0:1]:
    
    files = glob(path.join(data_folder, city,"*.htm"))
    total_positions  = len(files)
    non_996 = 0
    for file in files:
        #print(file)
        content=""
        with open(file, mode='r',encoding='utf-8') as f:
            content=f.read()
            f.close()
        soup=BeautifulSoup(content, "html.parser")
        span_tags=soup.select(".pos-info-tit span")
        benefits = [span_tag.text for span_tag in span_tags]
        if '周末双休' in benefits or '不加班' in benefits or '加班补助' in benefits:
            non_996=non_996+1
    
    print("found {} non-996 positions in {} positions in {}".format(non_996, total_positions, city))

