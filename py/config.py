# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 00:45:34 2019

@author: eric
"""

year=2020
month=5

table_list=['_201904','_201905','_201906','_201907','_201908','_201909','_201910','_201911','_201912', '_202001','_202002','_202003','_202004']
title_key_blacklist=['安全工程师','seo','测试','信息工程师','运维','经理','嵌入式','讲师','教师','老师','负责人','合伙人','计算机技术员','主任','总监','cto','需求工程师','需求分析','系统集成工程师','系统工程师','系统分析师','计算机辅助设计','DBA','实施','售前','售后','数据库','实习','数据标注员','管培生','2020届大专班','推广员','销售代表']
company_blacklist=['四川长虹网络科技有限责任公司', '软件与服务中心', '东华医为科技有限公司', '成都迈思信息技术有限公司', '广州国盛网络科技有限公司', '深圳市达铭丰科技有限公司', '北软互联（北京）科技有限公司', '南京瑞玥科技有限公司', '深圳极联信息技术股份有限公司','浙江八方电信有限公司诚聘', '深圳市捷兴电子商务有限公司', '西电济南变压器股份有限公司']

zhinengleibies={}
#后端
zhinengleibies['0106']='高级软件工程师'
zhinengleibies['0107']='软件工程师'
zhinengleibies['0120']='PHP开发工程师'
zhinengleibies['0121']='Java开发工程师'
zhinengleibies['0122']='C开发工程师'
zhinengleibies['0123']='系统分析员'
zhinengleibies['0124']='Python开发工程师'
zhinengleibies['0126']='.NET开发工程师'
zhinengleibies['0127']='系统工程师'
zhinengleibies['0128']='区块链开发'
zhinengleibies['0129']='Hadoop工程师'
zhinengleibies['0130']='大数据开发工程师'
zhinengleibies['0131']='爬虫开发工程师'
zhinengleibies['0132']='脚本开发工程师'
#zhinengleibies['0137']='系统集成工程师'  
zhinengleibies['0143']='系统架构设计师'
zhinengleibies['0151']='Ruby开发工程师'
zhinengleibies['0152']='Go开发工程师'
#前端    
zhinengleibies['7201']='Web前端开发'
zhinengleibies['7202']='HTML5开发工程师'
zhinengleibies['7203']='前端开发'    
#人工智能
zhinengleibies['7301']='机器学习工程师'
zhinengleibies['7302']='深度学习工程师'
zhinengleibies['7303']='图像算法工程师'
zhinengleibies['7304']='图像处理工程师'
zhinengleibies['7305']='图像识别工程师'
zhinengleibies['7306']='语音识别工程师'
zhinengleibies['7307']='机器视觉工程师'
zhinengleibies['7308']='自然语言处理（NLP）'
zhinengleibies['7309']='算法工程师'
zhinengleibies['7310']='推荐算法工程师'
zhinengleibies['7311']='搜索算法工程师'
zhinengleibies['7312']='人工智能'
#设计
zhinengleibies['7405']='网站架构设计师'
#手机
zhinengleibies['7701']='Android开发工程师'
zhinengleibies['7702']='iOS开发工程师'
zhinengleibies['7703']='移动开发工程师'
zhinengleibies['7704']='移动开发工程师'
zhinengleibies['7705']='小程序开发工程师'
#游戏
zhinengleibies['7809']='游戏开发工程师'
zhinengleibies['7810']='Cocos2d-x开发工程师'
zhinengleibies['7811']='Unity3d开发工程师'
zhinengleibies['7812']='游戏客户端开发工程师'
zhinengleibies['7813']='游戏服务端开发工程师'
#嵌入式
zhinengleibies['2910']='嵌入式软件开发'