# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:49:42 2019

@author: eric
"""
import db
from config import year, month

conn=db.get_conn()


#city stats
cities = """
('北京','上海','深圳','杭州','广州','南京','苏州','成都','东莞','西安','武汉','天津','长沙',
'宁波','福州','大连','重庆','青岛','济南','合肥','长春','昆明','郑州','沈阳','哈尔滨','厦门')
"""

sql=f"""select SUM(monthly_salary * headcount)/SUM(headcount) as salary, MAX(city) as city
 from _{year}{month:02} where monthly_salary>0 and monthly_salary<80000 and city in {cities}
 group by city
"""

result=conn.execute(sql).fetchall()

conn.execute(f"delete from CityStats where Month='{year}{month:02}'")

sql_insert=""

for salary, city in result:
    sql_insert+="insert into CityStats(Month, City, Salary) "
    sql_insert+=f" values('{year}{month:02}', '{city}', {salary});\n"

conn.execute(sql_insert)

conn.close()