# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:49:42 2019

@author: eric
"""
import numpy as np
import pandas as pd
import weighted
import db
from config import year, month


conn=db.get_conn()

#month=1
#city stats
cities = """
('北京','上海','深圳','杭州','广州','南京','苏州','成都','东莞','西安','武汉','天津','长沙',
'宁波','福州','大连','重庆','青岛','济南','合肥','长春','昆明','郑州','沈阳','哈尔滨','厦门')
"""

sql=f"""select SUM(monthly_salary * headcount)/SUM(headcount) as salary, MAX(city) as city
 from jobs where year_month={year}{month:02} and monthly_salary>0 and monthly_salary<80000 and city in {cities}
 group by city
"""

result=conn.execute(sql).fetchall()

conn.execute(f"delete from City_Stats where year_month='{year}{month:02}'")

sql_insert=""

for salary, city in result:
    sql_insert+="insert into City_Stats(year_month, City, Salary) "
    sql_insert+=f" values('{year}{month:02}', '{city}', {salary});\n"

conn.execute(sql_insert)



#MonthlyStats
def get_summary(data, career):
    
    salaries = data.monthly_salary.values
    headcounts = data.headcount.values
    head_count=np.sum(headcounts)
    salary_average=int(np.average(salaries, weights=headcounts))
    q = weighted.weighted_quantile(salaries,[0.025,0.5,0.975],headcounts)
    print(f"{year}年{month}月全国招收{career}{head_count}人。{year}年{month}月全国{career}平均工资{salary_average:.0f}元，工资中位数{q[1]:.0f}元，其中95%的人的工资介于{q[0]:.0f}元到{q[2]:.0f}元。\r\n")
    return head_count, salary_average, q[1]
    
data=pd.read_sql(sql=f"select * from jobs where year_month= {year}{month:02} and monthly_salary>0 and monthly_salary<80000", con=conn)
headcount, mean, median=get_summary(data, '程序员')
conn.execute(f"delete from general_Stats where year_month='{year}{month:02}'")
sql="insert into general_Stats(year_month, Salary_Mean, Salary_Median, JD_Count, Head_Count)"
sql=sql+f" values('{year}{month:02}',{mean},{median},{data.shape[0]},{headcount})"
conn.execute(sql)

conn.close()