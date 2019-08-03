--update _51jobs set career_software_engineer=0 where career_algorithm=1 or career_architect=1
--改为以万元为单位
--update _51jobs set monthly_salary=monthly_salary/10000


--R语言统计 R语言 "R Studio" R编程 '%，R，%''%,R,%'
--update _51jobs set pl_r=1 where job_description like '%、R、%' 
--or job_description like '%，R，%' 
--or job_description like '%,R,%'
--or  job_description like '%R语言%' 
--or  job_description like '%R Studio%' 
--or  job_description like '%R编程%' 
--or  job_description like '%R语言%' 
--vb.net
--update _51jobs set pl_visual_basic_net=1  where job_description like '%vb.net%' 
--or job_description like '%visual basic.net%' 
--select COUNT(1) from _51jobs where  job_description like '%vb.net%'
--select COUNT(1) from _51jobs where  job_description like '%Vb.net%'
--Groovy

--update _51jobs set pl_groovy=1  where job_description like '%groovy%'
--87
--
--update _51jobs set pl_scala=1  where job_description like '%scala%'
--(1639 rows affected)
--Assembly language 汇编
--update _51jobs set pl_assembly=1  where job_description like '%Assembly language%' or  job_description like '%汇编%' 
--(1147 rows affected)
--Linux Linux CentOS Ubuntu  redhat

--select * from _201904 where title like '%爬虫%'
--ALTER TABLE _201904 ADD career_spider bit DEFAULT 0 NOT NULL;
--update _201904 set career_spider=1  where title like '%爬虫%'
--update _201904 set career_software_engineer=0  where career_spider=1

--update _201904 set city='beijing' where city_beijing=1
--update _201904 set city='changchun' where city_changchun=1
--update _201904 set city='changsha' where city_changsha=1
--update _201904 set city='chengdu' where city_chengdu=1
--update _201904 set city='chongqing' where city_chongqing=1
--update _201904 set city='dalian' where city_dalian=1
--update _201904 set city='dongguan' where city_dongguan=1
--update _201904 set city='fuzhou' where city_fuzhou=1
--update _201904 set city='guangzhou' where city_guangzhou=1
--update _201904 set city='hangzhou' where city_hangzhou=1
--update _201904 set city='harbin' where city_harbin=1
--update _201904 set city='hefei' where city_hefei=1
--update _201904 set city='jinan' where city_jinan=1
--update _201904 set city='kunming' where city_kuming=1
--update _201904 set city='nanjing' where city_nanjing=1
--update _201904 set city='ningbo' where city_ningbo=1
--update _201904 set city='qingdao' where city_qingdao=1
--update _201904 set city='shanghai' where city_shanghai=1
--update _201904 set city='shenyang' where city_shenyang=1
--update _201904 set city='shenzhen' where city_shenzhen=1
--update _201904 set city='tianjin' where city_tianjin=1
--update _201904 set city='wuhan' where city_wuhan=1
--update _201904 set city='xian' where city_xian=1
--update _201904 set city='zhengzhou' where city_zhengzhou=1

--update _201904 set career='algorithm' where career_algorithm=1
--update _201904 set career='architect' where career_architect=1
--update _201904 set career='software' where career_software_engineer=1
--update _201904 set career='spider' where career_spider=1



