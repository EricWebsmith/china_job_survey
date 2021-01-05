--career
--delete from jobs where year_month=202101 and monthly_salary>0 and monthly_salary<3000
delete from jobs where year_month=202101 and title like '%赴日%' and not title like '%机会%' 
--delete from jobs where year_month=202101 and monthly_salary>0 and monthly_salary<1000

delete [jobs] where year_month=202101 and title like '%技工%'
delete [jobs] where year_month=202101 and title like '%技术员%'
delete [jobs] where year_month=202101 and city ='杭州' and title like '00%(职位编号：%)'
delete [jobs] where year_month=202101 and province ='异地招聘'
delete [jobs] where year_month=202101 and job_summary like '%应届生%'
delete [jobs] where year_month=202101 and title like '%应届%'
delete [jobs] where year_month=202101 and title like '%校招%'
delete [jobs] where year_month=202101 and title like '%校园招聘%'

update jobs set career='软件工程师' where year_month=202101 and zhinengleibie in ('软件工程师', '高级软件工程师', 'PHP开发工程师', 'Java开发工程师', 'C开发工程师', 'Python开发工程师', '.NET开发工程师', '脚本开发工程师', 'Ruby开发工程师', 'Go开发工程师')
update jobs set career='软件工程师' where year_month=202101 and career='一般程序员'
update jobs set career='Android开发工程师' where year_month=202101 and title like '%Android%' or title like '%安卓%' 

update jobs set career='信号处理' where year_month=202101 and title like '%信号处理%'
update jobs set career='爬虫开发工程师' where year_month=202101 and title like '%爬虫%'
update jobs set career='ADAS' where year_month=202101 and title like '%adas%'
update jobs set career='机器人' where year_month=202101 and title like '%机器人%' or title like '%ROS%'
update jobs set career='GIS' where year_month=202101 and title like '%GIS%'
update jobs set career='CAE' where year_month=202101 and title like '%CAE%'
update jobs set career='光学算法' where year_month=202101 and title like '%光学算法工程师%'
update jobs set career='ETL' where year_month=202101 and title like '%ETL%'
update jobs set career='Unity3D' where year_month=202101 and title like '%Unity3D%'
update jobs set career='遥感' where year_month=202101 and title like '%遥感%'
update jobs set career='规划算法' where year_month=202101 and title like '%规划算法工程师%'
update jobs set career='视觉软件工程师' where year_month=202101 and title like '%三维重建%'
update jobs set career='视觉软件工程师' where year_month=202101 and title like '%视觉软件工程师%'


update jobs set career='大数据' where year_month=202101 and title like '%大数据%'
update jobs set career='CT重建' where year_month=202101 and title like '%CT重建%'
update jobs set career='SLAM' where year_month=202101 and title like '%SLAM%'
update jobs set career='DSP' where year_month=202101 and title like '%DSP%'
update jobs set career='生物信息' where year_month=202101 and title like '%生物信息%'
update jobs set career='编译器开发工程师' where year_month=202101 and title like '%编译器%'
update jobs set career='算法工程师' where year_month=202101 and title like '%算法%' or zhinengleibie='算法工程师'
update jobs set career='自然语言处理（NLP）' where year_month=202101 and title like '%自然语言处理%' or title like '%NLP%'

delete from jobs where year_month=202101 and zhinengleibie='推荐算法工程师' and not title like '%推荐%'
update jobs set career='推荐算法工程师' where year_month=202101 and title like '%推荐算法%'

delete from jobs where year_month=202101 and zhinengleibie='搜索算法工程师' and not title like '%搜索%'
update jobs set career='搜索算法工程师' where year_month=202101 and title like '%搜索算法%' or title like '%Search Algorithm%'
update jobs set career='反作弊算法工程师' where year_month=202101 and title like '%反作弊%'

update jobs set career='图像处理工程师' where year_month=202101 and title like '%图像处理%'
update jobs set career='图像算法工程师' where year_month=202101 and title like '%图像算法%' or zhinengleibie='图像算法工程师'
update jobs set career='人工智能' where year_month=202101 and title like '%AI%' or title like '%人工智能%' or title like '%神经网络%'
update jobs set career='区块链开发' where year_month=202101 and title like '%区块链%' or zhinengleibie='区块链开发'
update jobs set career='CTO' where year_month=202101 and title like '%CTO%' or title like '%首席技术官%'  or title like '%智慧研究院院长%'
update jobs set career='芯片' where year_month=202101 and title like '%芯片%' or title like '%SOC设计%'
update jobs set career='驱动工程师'  where year_month=202101 and title like '%driver%' or title like '%驱动%'
update jobs set career='机器学习' where year_month=202101 and title like '%机器学习%' or zhinengleibie='机器学习工程师'
update jobs set career='深度学习工程师' where year_month=202101 and title like '%深度学习%'
update jobs set career='数据科学家' where year_month=202101 and title like '%Data Scientist%' or  title like '%数据科学家%'


update jobs set career='架构师' where year_month=202101 and title like '%系统架构师%' or title like '%架构师%' or title like '%架构专家%' or title like '%architect%'   or title like '%架构研发%'
update jobs set career='技术主管' where year_month=202101 and title like '%主管%' or title like '%leader%' 

update jobs set career='分布式' where year_month=202101 and career='软件工程师' and title like '%分布式%' 

update jobs set career='敏捷教练' where year_month=202101 and title like '%敏捷教练%' or title like '%agile coach%'  or title like '%Scrum Master%' 

update jobs set career='Cocos2d-x开发工程师' where year_month=202101 and career='软件工程师' and title like '%Cocos2d-x%' 

update jobs set career='MES' where year_month=202101 and career='软件工程师' and title like '%MES%' 

update jobs set career='Hadoop工程师' where year_month=202101 and title like '%Hadoop%' 

update jobs set career='嵌入式软件开发' where year_month=202101 and title like '%嵌入式%' or title like '%FPGA%' 

delete from jobs where year_month=202101 and career='人工智能' and not title like '%人工智能%'


update jobs set ageism=1 where year_month=202101 and job_description like '%岁%'

update jobs set ml_paddlepaddle=1 where year_month=202101 and job_description like '%paddlepaddle%'
update jobs set ml_mahout=1 where year_month=202101 and job_description like '%mahout%'
update jobs set ml_sklearn=1 where year_month=202101 and job_description like '%scikit-learn%' or  job_description like '%scikitlearn%' or  job_description like '%sklearn%'
update jobs set ml_theano=1 where year_month=202101 and job_description like '%theano%'
update jobs set ml_keras=1 where year_month=202101 and job_description like '%keras%'
update jobs set ml_mxnet=1 where year_month=202101 and job_description like '%mxnet%'
update jobs set ml_cntk=1 where year_month=202101 and job_description like '%cntk%'
update jobs set ml_caffe=1 where year_month=202101 and job_description like '%caffe%'
update jobs set ml_tensorflow=1 where year_month=202101 and job_description like '%tensorflow%'
update jobs set ml_pytorch=1 where year_month=202101 and job_description like '%pytorch%'



