--career
delete from [jobs].[dbo].[_202005] where city ='杭州' and title like '00%(职位编号：%)'
delete from [jobs].[dbo].[_202001] where province ='异地招聘'
delete from [jobs].[dbo].[_202001] where job_summary like '%应届生%'
delete from [jobs].[dbo].[_202001] where title like '%应届%'


update _202005 set career='软件工程师' where zhinengleibie in ('软件工程师', '高级软件工程师', 'PHP开发工程师', 'Java开发工程师', 'C开发工程师', 'Python开发工程师', '.NET开发工程师', '脚本开发工程师', 'Ruby开发工程师', 'Go开发工程师')
update _202005 set career='软件工程师' where career='一般程序员'
update _202005 set career='Android开发工程师' where title like '%Android%' or title like '%安卓%' 

update _202005 set career='信号处理' where title like '%信号处理%'
update _202005 set career='爬虫开发工程师' where title like '%爬虫%'
update _202005 set career='ADAS' where title like '%adas%'
update _202005 set career='机器人' where title like '%机器人%' or title like '%ROS%'
update _202005 set career='GIS' where title like '%GIS%'
update _202005 set career='CAE' where title like '%CAE%'
update _202005 set career='光学算法' where title like '%光学算法工程师%'
update _202005 set career='ETL' where title like '%ETL%'
update _202005 set career='Unity3D' where title like '%Unity3D%'
update _202005 set career='遥感' where title like '%遥感%'
update _202005 set career='规划算法' where title like '%规划算法工程师%'
update _202005 set career='视觉软件工程师' where title like '%三维重建%'
update _202005 set career='视觉软件工程师' where title like '%视觉软件工程师%'


update _202005 set career='大数据' where title like '%大数据%'
update _202005 set career='CT重建' where title like '%CT重建%'
update _202005 set career='SLAM' where title like '%SLAM%'
update _202005 set career='DSP' where title like '%DSP%'
update _202005 set career='生物信息' where title like '%生物信息%'
update _202005 set career='编译器开发工程师' where title like '%编译器%'
update _202005 set career='算法工程师' where title like '%算法%' or zhinengleibie='算法工程师'
update _202005 set career='自然语言处理（NLP）' where title like '%自然语言处理%' or title like '%NLP%'

delete from _202005 where zhinengleibie='推荐算法工程师' and not title like '%推荐%'
update _202005 set career='推荐算法工程师' where title like '%推荐算法%'

delete from _202005 where zhinengleibie='搜索算法工程师' and not title like '%搜索%'
update _202005 set career='搜索算法工程师' where title like '%搜索算法%' or title like '%Search Algorithm%'
update _202005 set career='反作弊算法工程师' where title like '%反作弊%'

update _202005 set career='图像处理工程师' where title like '%图像处理%'
update _202005 set career='图像算法工程师' where title like '%图像算法%' or zhinengleibie='图像算法工程师'
update _202005 set career='人工智能' where title like '%AI%' or title like '%人工智能%' or title like '%神经网络%'
update _202005 set career='区块链开发' where title like '%区块链%' or zhinengleibie='区块链开发'
update _202005 set career='CTO' where title like '%CTO%' or title like '%首席技术官%'  or title like '%智慧研究院院长%'
update _202005 set career='芯片' where title like '%芯片%' or title like '%SOC设计%'
update _202005 set career='驱动工程师'  where title like '%driver%' or title like '%驱动%'
update _202005 set career='机器学习' where title like '%机器学习%' or zhinengleibie='机器学习工程师'
update _202005 set career='深度学习工程师' where title like '%深度学习%'
update _202005 set career='数据科学家' where title like '%Data Scientist%' or  title like '%数据科学家%'


update _202005 set career='架构师' where title like '%系统架构师%' or title like '%架构师%' or title like '%架构专家%' or title like '%architect%'   or title like '%架构研发%'
update _202005 set career='技术主管' where title like '%主管%' or title like '%leader%' 

update _202005 set career='分布式' where career='软件工程师' and title like '%分布式%' 

update _202005 set career='敏捷教练' where title like '%敏捷教练%' or title like '%agile coach%'  or title like '%Scrum Master%' 

update _202005 set career='Cocos2d-x开发工程师' where career='软件工程师' and title like '%Cocos2d-x%' 

update _202005 set career='MES' where career='软件工程师' and title like '%MES%' 

update _202005 set career='Hadoop工程师' where title like '%Hadoop%' 

update _202005 set career='嵌入式软件开发' where title like '%嵌入式%' or title like '%FPGA%' 

delete from _202005 where career='人工智能' and not title like '%人工智能%'


update _202005 set ageism=1 where job_description like '%岁%'

update _202005 set ml_paddlepaddle=1 where job_description like '%paddlepaddle%'
update _202005 set ml_mahout=1 where job_description like '%mahout%'
update _202005 set ml_sklearn=1 where job_description like '%scikit-learn%' or  job_description like '%scikitlearn%' or  job_description like '%sklearn%'
update _202005 set ml_theano=1 where job_description like '%theano%'
update _202005 set ml_keras=1 where job_description like '%keras%'
update _202005 set ml_mxnet=1 where job_description like '%mxnet%'
update _202005 set ml_cntk=1 where job_description like '%cntk%'
update _202005 set ml_caffe=1 where job_description like '%caffe%'
update _202005 set ml_tensorflow=1 where job_description like '%tensorflow%'
update _202005 set ml_pytorch=1 where job_description like '%pytorch%'



