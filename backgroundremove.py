import requests
import base64
from PIL import Image
from io import BytesIO
import base64
import requests
import urllib.request
import streamlit as st 
from rembg import remove



def removebgapi(links):
    st.write(links)
    urllib.request.urlretrieve(links,"gfg.png")
    img = Image.open("gfg.png")
    st.image(img)
    st.write("inside removebgapi")
    st.write("-8")
    img.thumbnail((500, 500))
    st.write("-9")
    st.write(img.size)
    st.write("-10")
    st.write(type(img))
    st.write("-11")
    imot=remove(img)
    st.image(imot)
    st.write("done:D")
#     img_b64 = base64.b64encode(buffer.getvalue())
#     st.write("-12")
#     imgs=img_b64
#     st.write("-13")
#     imgs=str(imgs).replace("b'","")
#     st.write("-14")
#     payloaddata={"data": ["data:image/jpeg;base64,"+imgs,10,"alpha matting"]}
#     st.write("-15")
#     r = requests.post(url='https://syedinamulhaq-remove-bg.hf.space/+/api/predict/', json=payloaddata)
#     st.write("-16")
#     st.write(r)
#     opimg=str(r.json()["data"][0]).replace("data:image/png;base64,","")
#     st.write("-17")
#     st.write("opimg")
#     st.write("-18")
#     imot = Image.open(BytesIO(base64.b64decode(opimg)))
    st.write("-19")
    return(imot)
