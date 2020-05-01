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


--update _201904 set city='zhengzhou' where city_zhengzhou=1

--update _201904 set career='algorithm' where career_algorithm=1
--update _201904 set career='architect' where career_architect=1
--update _201904 set career='software' where career_software_engineer=1
--update _201904 set career='spider' where career_spider=1



