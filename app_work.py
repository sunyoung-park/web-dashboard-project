import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def run_work_app():
    st.title("'맞벌이' 신혼부부 비중")

    df5 = pd.read_csv('./data/newlywed_all.csv')

    fig = px.bar(df5, x='시점', y='맞벌이 비율 (B/A*100)', color='맞벌이 비율 (B/A*100)', color_continuous_scale='peach')
    fig.update_yaxes(range=[35, 60])
    st.plotly_chart(fig)

    st.text('')
    st.text('')
    st.text('')

    st.subheader('15~21년 신혼 부부의 맞벌이/외벌이 추이(%)')
    df5['외벌이 비율 ((A-B)/A*100)']=(df5['신혼부부 수 (A)']-df5['맞벌이 부부 수 (B)'])/df5['신혼부부 수 (A)']*100
    df5['외벌이 비율 ((A-B)/A*100)'] =df5['외벌이 비율 ((A-B)/A*100)'].round(2)


    df5554 = df5[['시점','맞벌이 비율 (B/A*100)','외벌이 비율 ((A-B)/A*100)']]

    fig1 = px.line(df5554, x='시점', y=['맞벌이 비율 (B/A*100)','외벌이 비율 ((A-B)/A*100)'],markers=True)

    
    st.plotly_chart(fig1)

