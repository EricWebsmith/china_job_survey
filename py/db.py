# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:46:54 2019

@author: eric
"""

from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

def get_conn():
    params = quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                     "SERVER=localhost;"
                                     "DATABASE=it_jobs;"
                                     "Trusted_Connection=yes;")
    
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    conn=engine.connect()
    return conn
    
def get_data(sqlOrTableName, connection, params=None):
    sql = ""
    if len(sqlOrTableName.split(' '))==1: #if it is a table name
        sql = "select * from {}".format(sqlOrTableName)
    else:
        sql=sqlOrTableName
    bookExtensionTable = pd.read_sql(sql,con=connection, params=params)
    return bookExtensionTable

