--update _201904v2 set career = '系统架构师' where career='架构设计师'

select * from _201904v2 where career like '%爬虫%'


update _201904v2 set career='爬虫工程师'  where title like '%爬虫%'
update _201904v2 set career='生物信息工程师'  where title like '%生物信息%'