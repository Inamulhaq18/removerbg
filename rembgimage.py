from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import delete
import pandas as pd
import streamlit as st 
import psycopg2
from st_aggrid import AgGrid


engine = create_engine("postgresql://hkmuctkbhmlhsr:59563300aab6c650f8bbc9cc4153df6a42054b71e9be00dda420f40bbbf791b2@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dd8a5bspvhrk8c", echo = False)

#Session for DB
Session=sessionmaker(bind=engine)
session=Session
Base=declarative_base()


shopify=pd.read_csv("shopifytemp.csv")
shopifycolumns=list(shopify.columns)
conn=psycopg2.connect("postgresql://hkmuctkbhmlhsr:59563300aab6c650f8bbc9cc4153df6a42054b71e9be00dda420f40bbbf791b2@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dd8a5bspvhrk8c") 
curr=conn.cursor()
# Loading approved data from database
sql = "SELECT * FROM master_product_table"
dat = pd.read_sql_query(sql,conn)
pfa=dat
conn.close()
pfa=pfa[pfa["Product_id"]>650]
pfa=pfa[pfa["Product_approval_status"]==1]
pfa=pfa[pfa["shopify_status"]==1]
pfa=pfa.sort_values(by="Product_id")
pfa=pfa.drop_duplicates(subset='Product_Name_en', keep="last")
#Number of items 
number_of_items=(pfa[pfa["Product_live_status"]==1]).shape[1]

pfa.dropna(subset=["Product_Name_en"])
pfa=pfa[pfa['Product_Name_en']!=""]
pfa=pfa[pfa['Product_image_P_url']!=""]

shopifycolumnss=pd.DataFrame(columns=shopifycolumns)
list(shopifycolumnss.columns)

pfa=pfa.dropna(subset=['variety'])
afgrid(pfa)
