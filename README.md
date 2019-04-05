# Stats of Chinese Developers
#统计中国程序员的就业情况

This repo is to look into Chinese Job website and make stats. 
根据招聘网站，统计程序员就业信息。

## Salary 程序员工资
```
data[data.monthly_salary<40000].monthly_salary.hist()
```
[!Salary Distribution](https://github.com/juwikuang/51job_survey_py/blob/master/images/salary_distribution.png?raw=true)

## 996(Overtime) Survey/996调查
996 means working from 9am to 9pm, 6 days a week.
996 Positions have a significant higher salary(25%) than the 996 positions.
996的职位比非996的职位工资高25%。

Overtime in Beijing is much severe than in other cities.
北京的996现象最严重

Companies without 996.
996 白名单（周末双休、朝九晚五的公司）：
https://github.com/juwikuang/51job_survey_py/blob/master/whitelist.txt

996 Balcklist. 996黑名单：
https://github.com/juwikuang/51job_survey_py/blob/master/blacklist.txt

for more, look into the code. especially the jupyter notebooks.
更多信息，查看源代码（主要是jupyter notebook）:

https://github.com/juwikuang/51job_survey_py/blob/master/Survey.ipynb
https://github.com/juwikuang/51job_survey_py/blob/master/996_Survey.ipynb
