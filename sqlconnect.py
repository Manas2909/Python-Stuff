# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:22:37 2019

@author: Manas
"""
import pandas as pd
import mysql.connector,sys
conn= mysql.connector.connect(host='localhost',user='root',password='root',port=3306)
c=conn.cursor()
def create_table():
    c.execute("create table if not exists movie_genres(genres varchar(100))")
    
create_table()
c.execute("insert into movie_genres('comedy')")
conn.commit
dataf=pd.read_sql("select * from movie_genres",conn)
