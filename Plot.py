import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.header("1. Altair Scatter Plot")
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a', y='b',
                        size ='c', tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

st.header("2. Interactive Charts")
st.subheader("2.1 Line Chart")
df = pd.read_csv("C:\\Users\\LENOVO\\Desktop\\Practice\\Streamlit\\lang_data.csv")
lang_list = df.columns.tolist()
user_choice = st.multiselect("Choose your programming language:",lang_list)
new_df = df[user_choice]
st.line_chart(new_df)

st.subheader("2.2 Area Chart")
st.area_chart(new_df)

st.header("3. Data Visualization with Plotly")
st.subheader("3.1 Displaying the Dataset")
df = pd.read_csv("C:\\Users\\LENOVO\\Desktop\\Practice\\Streamlit\\tips.csv")
st.dataframe(df.head())

st.subheader("3.2 Pie Chart")
fig = px.pie(df,values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.subheader("3.2 Pie Chart with Variation in Color Sequence")
fig = px.pie(df,values = 'total_bill', names = 'day', opacity = .7,
            color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader('3.4 Histogram')
x1 = np.random.randn(200) - 1
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1
hist_data = [x1,x2,x3]
group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.25,.5])
st.plotly_chart(fig)
