import requests
import base64
from PIL import Image
from io import BytesIO
import base64
import requests
import streamlit as st 
from rembg import remove



def removebgapi(links):
    st.write("inside removebgapi")
    st.write(links)
    st.write("-1")
    a=base64.b64encode(requests.get(links).content)
    st.write("-2")
    imgs=str(a).replace("b'","")
    st.write("-3")
    base64_str = imgs
    st.write("-4")
    buffer = BytesIO()
    st.write("-5")
    imgdata = base64.b64decode(base64_str)
    st.write("-6")
    img = Image.open(BytesIO(imgdata))
    st.write("-7")
    st.write(img.size)
    st.write("-8")
    img.thumbnail((500, 500))
    st.write("-9")
    st.write(img.size)
    st.write("-10")
    st.write(type(img))
    img.save(buffer, format="PNG")
    st.write("-11")
    st.write(type(img))
    imot=remove(img)
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
