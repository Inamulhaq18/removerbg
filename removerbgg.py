import datetime
import pandas as pd
import streamlit as st 
import psycopg2
from st_aggrid import AgGrid
import time
import requests
import heroku3
from bgremovepid import bgprocess



# engine = create_engine("postgres://ue0bragorjpsfg:p3401de69df0671d626efa0688fbb4b255afe17a00d95341e8504b5442c3516f3@ec2-52-18-7-194.eu-west-1.compute.amazonaws.com:5432/d1en285kafvdds", echo = False)

# #Session for DB
# Session=sessionmaker(bind=engine)
# session=Session
# Base=declarative_base()


shopify=pd.read_csv("shopifytemp.csv")
shopifycolumns=list(shopify.columns)
conn=psycopg2.connect("postgres://ue0bragorjpsfg:p3401de69df0671d626efa0688fbb4b255afe17a00d95341e8504b5442c3516f3@ec2-52-18-7-194.eu-west-1.compute.amazonaws.com:5432/d1en285kafvdds") 
curr=conn.cursor()

def imageprocessapi(links):
    session = requests.Session()
    session.trust_env = False
    links=links
    url="https://abo5imageapi.herokuapp.com/processBG?rurl="
    url=url+links
    response = session.get(url)
    return(response.content)

# Loading approved data from database
sql = "SELECT * FROM master_product_table"
dat = pd.read_sql_query(sql,conn)
pfa=dat
conn.close()
pfa=pfa[pfa["Product_id"]>650]
pfa=(pfa[pfa['Product_image_P_url']==""])
st.write("RURL")
#pfa=pfa[pfa["Product_approval_status"]==1]
#pfa=pfa[pfa["shopify_status"]==1]
pfa=pfa.sort_values(by="Product_id")
pfa.dropna(subset=["Product_Name_en"])
pfa=pfa.drop_duplicates(subset='Product_Name_en', keep="last")

#pfa=pfa[pfa['Product_Name_en']!=""]
pfa=pfa[pfa['Product_image_R_url']!=""]

#pfa=pfa[pfa['Product_image_P_url']==""]
#Number of items 
number_of_items=(pfa[pfa["Product_live_status"]==1]).shape[1]

shopifycolumnss=pd.DataFrame(columns=shopifycolumns)
list(shopifycolumnss.columns)

pfa=pfa.dropna(subset=['variety'])
#AgGrid(pfa)
noimage=(pfa.shape[0])
st.title("Products to be processed - ")
st.title(noimage)

if st.button("Process Images"):
    remaining=pfa.shape[0]
    #st.write(remaining)
    for index, row in pfa.iterrows():
      parameter=row['Product_image_R_url']
      #st.write(type(parameter))
      try:
        a=bgprocess(parameter)
      except:
        st.write("An exception occurred")
      remaining=remaining-1
      st.write("Remaining :",remaining)
