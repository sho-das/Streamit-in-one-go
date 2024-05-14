import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot  as plt
import seaborn as sns

chart = pd.DataFrame(np.random.randn(25,3), columns = ['Line-1','Line-2','Line-3'])

#Charts with random numbers - Line, Bar and Area
st.header("1. Charts with Random Numbers")

st.subheader("1.1 Line Chart")
st.line_chart(chart)

st.subheader("1.2 Bar Chart")
st.bar_chart(chart)

st.subheader("1.3 Area Chart")
st.area_chart(chart)

#Visualization with Matplotlib & Searborn
st.header("2. Visualization with Matplotlib and Seaborn")

st.subheader("2.1 Loading the DataFrame")
df = pd.read_csv("C:\\Users\\LENOVO\\Desktop\\Practice\\Streamlit\\iris.csv")
if df is not None:
    st.dataframe(df)

st.subheader("2.2 Bar Graph with Maptplotlib")
fig = plt.figure(figsize = (15,8))
df['species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.subheader("2.3 Distribution Plot with Seaborn")
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

#Visualization with Multipple graphs
st.header("3. Multiple Graphs")

st.subheader("3.1 Graphs in One Line")
col1, col2 = st.columns(2)

with col1:
    col1.header = "KDE is -ve"
    fig1 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig1)

with col2:
    col2.header = "HIST is -ve"
    fig2 = plt.figure(figsize = (5,5))
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

st.subheader("3.2 Graphs in One Line in different style")
col1, col2 = st.columns(2)

with col1:
    fig1 = plt.figure(figsize = (5,5))
    sns.set_style("darkgrid")
    sns.set_context("poster")
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure(figsize = (5,5))
    sns.set_theme(context = "notebook", style = "darkgrid")
    sns.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig2)

#Exploring Different Graphs
st.header("4. Exploring Different Graphs")

st.subheader("4.1 Scatter Plot")
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader("4.2 Count Plot")
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'petal_length')
st.pyplot(fig)

st.subheader("4.3 Box Plot")
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, y = 'petal_length', x = 'species')
st.pyplot(fig)

st.subheader("4.3 Violin Plot")
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, y = 'petal_length', x = 'species')
st.pyplot(fig)
