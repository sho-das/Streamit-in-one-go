import streamlit as st
import pandas as pd

#Uploading and Loading a CSV
st.subheader("Uploading a CSV File:")
temp = st.file_uploader("Upload a csv file", type = ['csv','xlsx'])

st.subheader("Uploading a CSV File:")
if temp is not None:
    df = pd.read_csv(temp)
    #Printing dataframe
    st.markdown('##### Scrollable Table/ Dataframe')
    st.dataframe(df.head())
    #Printing table
    st.markdown('##### UnScrollable Table/ Table format')
    st.table(df.head())

#Uploading an Image, Audio and Video file
st.subheader("Image File:")
x = "Choose already uploaded path"
y = "Upload your own image"
temp = st.radio('Uploading the image file:',(y,x))
if temp == x:
    st.markdown('##### Already Uploaded Image on Server')
    img_file = "C:\\Users\\LENOVO\\Desktop\\Practice\\Streamlit\\img.jpg"
    if img_file is not None:
        st.image(img_file)
if temp == y:
    img_file = st.file_uploader("Upload the image :", type = ['png','jpg','jpeg'])
    if img_file is not None:
        st.image(img_file)

st.subheader("Audio File:")
aud_file = st.file_uploader("Upload the audio file:",type = 'mp3')
if aud_file is not None:
    st.audio(aud_file,start_time = 10)

st.subheader("Video File:")
vid_file = st.file_uploader("Upload the Video :", type = ['mp4','mkv'])
if vid_file is not None:
    st.audio(vid_file,start_time = 0)
