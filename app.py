import streamlit as st
import joblib
import numpy as np

# Load the model and data using joblib
pipe = joblib.load('pipe.jbl')
df = joblib.load('df.jbl')



st.title("Laptop Predictor")

# brand
company = st.selectbox('Brand',df['Manufacturer'].unique())

# type of laptop
type = st.selectbox('Type',df['Category'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['CPU_bra'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['GPU_br'].unique())

os = st.selectbox('OS',df['Operating System'].unique())
os_ver = st.selectbox('Os_Version', ['X', '7', '11', 'Other'])

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os,os_ver])

    query = query.reshape(1,13)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))