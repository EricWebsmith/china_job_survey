--update _51jobs set career_software_engineer=0 where career_algorithm=1 or career_architect=1
--��Ϊ����ԪΪ��λ
--update _51jobs set monthly_salary=monthly_salary/10000


--R����ͳ�� R���� "R Studio" R��� '%��R��%''%,R,%'
--update _51jobs set pl_r=1 where job_description like '%��R��%' 
--or job_description like '%��R��%' 
--or job_description like '%,R,%'
--or  job_description like '%R����%' 
--or  job_description like '%R Studio%' 
--or  job_description like '%R���%' 
--or  job_description like '%R����%' 
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
--Assembly language ���
--update _51jobs set pl_assembly=1  where job_description like '%Assembly language%' or  job_description like '%���%' 
--(1147 rows affected)
--Linux Linux CentOS Ubuntu  redhat


