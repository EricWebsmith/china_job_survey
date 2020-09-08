import os

pwd=os.getcwd()
year_month=pwd.split('\\')[-1]

year=int(year_month[:4])
month=int(year_month[4:])
