from backgroundremove import removebgapi
import json
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from abo5s3 import save_uploadedfile
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import mimetypes
import s3fs
import os
import datetime
import psycopg2
import gc


os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIARLFEN3ZYTWBVYNX7'
os.environ["AWS_SECRET_ACCESS_KEY"] = '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'


s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIARLFEN3ZYTWBVYNX7',
    aws_secret_access_key='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'
)


Purl=[]

s3_url="https://abo5.s3.eu-central-1.amazonaws.com/"
print(Purl)
print(Purl)

#function to remove BG from images and return image format to be uploaded in s3 
def addwhitebg(img):
            img1 = Image.open(r"bgimage.png")
            #BG Removal
            img2 = img
            og=img.copy()

            img2 = img2.crop(img2.getbbox())

            maxsize=int(max(img2.size)*1.5)
            img1=(img1.resize((maxsize,maxsize),Image.ANTIALIAS))
            img_w, img_h = img2.size
            bg_w, bg_h = img1.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
            img1.paste(img2, offset, mask = img2)
            img1=img1.resize((1000,1000),Image.ANTIALIAS)
            img1.save("converted.png", format="png")
            return(img1)

def pushtos3(img):
    #name for the image
     img.save("temp.png")
     name="R"+str(datetime.datetime.now())
     name=name.replace(".","")
     name=name.replace(":","")
     name=name.replace(" ","")
     name=name+"."+"png"
     #push the image to s3
     s3.Bucket('abo5').upload_file(Filename="temp.png", Key=name)
     print("pushtos3")
     return(s3_url+name)



def pushdbupdate(Rurls,purl):
    conn=psycopg2.connect("postgres://ue0bragorjpsfg:p3401de69df0671d626efa0688fbb4b255afe17a00d95341e8504b5442c3516f3@ec2-52-18-7-194.eu-west-1.compute.amazonaws.com:5432/d1en285kafvdds") 
    curr=conn.cursor()
    sql_select_query = """UPDATE master_product_table SET "Product_image_P_url" = %s WHERE "Product_image_R_url" = %s"""
    print("__Purl__")
    purl=",".join(purl)
    curr.execute(sql_select_query, (purl,Rurls,))
    conn.commit()
    conn.close()
    print("pushdb completed")



def bgremove(urls):
    print(urls)
    Purl=[]
    for url in urls:
        st.write("1")
        img=removebgapi(url)
        st.write("2")
        img=addwhitebg(img)
        st.write("3")
        img=img.rotate(-90)
        st.write("4")
        link=pushtos3(img)
        st.write("5")
        Purl.append(link)
    print("bgremove completed")
    return(Purl)   
        #add white BG

def bgprocess(rurl):
    st.write("Inside bgprocess")
    st.write(rurl)
    print("rurl  :")
    print(rurl)
    print("_________rurl__________")
    print(rurl)
    Rurls=rurl
    print("_________Rurl__________")
    print(Rurls)
    urls=Rurls.split(", ")
    #st.write(type(urls))
    Purl=bgremove(urls)
    st.write("got Purl")
    print("_________PURL_________")
    print(Purl)
    pushdbupdate(Rurls,Purl)
    gc.collect()
    
    print("completed operation")
    return("done")
