from multiprocessing import Process

import numpy as np
import os

import glob

from config import year, month, company_blacklist, title_key_blacklist, zhinengleibies
year_month=f'{year}{month:02}'

provinces=['北京','上海','广东','深圳','天津','重庆','江苏','浙江','四川','海南','福建','山东','江西','广西','安徽','河北','河南','湖北','湖南','陕西','山西','黑龙江','辽宁','吉林','云南','贵州','甘肃','内蒙古','宁夏','西藏','新疆','青海']
data_folder = '../../data/51jobs_{}/'.format(year_month)
back_folder = '../../data/51jobs_{}_b/'.format(year_month)

d = {}

counts = []
for zhinengleibie in list(zhinengleibies.values())[::-1]:
    count=0
    for province in provinces:
        files=glob.glob(f'{data_folder}{zhinengleibie}/{province}/*.*')
        count+=len(files)
    d[zhinengleibie]=count
    counts.append(count)
    #forglob(data_folder+"*")

orders = np.argsort(counts)

zhineng_splitters=[]
zhineng_splitters=[]

n_splitters = 4

for splitter_index in range(4):
    zhineng_splitters.append([])

for i in range(len(orders)):
    for splitter_index in range(4):
        if i % n_splitters == splitter_index:
            zhineng_splitters[splitter_index].append(znlbs[orders[i]])

znlbs=zhinengleibies.values()
znlbs = list(znlbs)


