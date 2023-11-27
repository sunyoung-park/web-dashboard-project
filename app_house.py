import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def run_house_app():    
    st.title("신혼부부 '주택 소유' 비중")


    
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ 우리나라 총 신혼부부 주택 소유 비중(%)')

    df3 = pd.read_csv('./data/house_newlyweds.csv')

    df3['주택 소유'] = df3['주택 소유'].str.replace('X','0')
    df3['주택 소유']=df3['주택 소유'].astype(int)
    df3_sum = df3[['주택 미소유','주택 소유']].sum(axis=1)
    df3['주택 보유율'] = (df3['주택 소유']/df3_sum*100).round(2)

    df30 =df3.loc[df3['신혼부부 특성별(1)']=='전국',['시점','주택 보유율']]
    df30['주택 보유율']=df30['주택 보유율'].round(2)

    fig = px.bar(df30, x='시점', y='주택 보유율', color='주택 보유율', color_continuous_scale='peach', text_auto=True)
    fig.update_yaxes(range=[40, 45])
    st.plotly_chart(fig)





    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ 15년도와 21년도 신혼부부 주택 소유 비중 비교(%)')

    df34 = df3.loc[(df3['시점']==2021) & (df3['신혼부부 특성별(1)']=='혼인연차별'),['신혼부부 특성별(2)','주택 보유율']]
    df34['주택 보유율']=df34['주택 보유율'].round(2)
    df34=df34.rename(columns={'주택 보유율':'21년 주택 보유율'}).reset_index()

    df35 = df3.loc[(df3['시점']==2015) & (df3['신혼부부 특성별(1)']=='혼인연차별'),['신혼부부 특성별(2)','주택 보유율']]
    df35['주택 보유율']=df35['주택 보유율'].round(2)
    df35=df35.rename(columns={'주택 보유율':'15년 주택 보유율'}).reset_index()

    df35['21년 주택 보유율']=df34['21년 주택 보유율']

    fig1 = go.Figure(data =[
    go.Bar(name = '15년 주택 보유율', x=df35['신혼부부 특성별(2)'],
    y=df35['15년 주택 보유율'], marker_color='#ecddfe'),
    go.Bar(name = '21년 주택 보유율', x=df35['신혼부부 특성별(2)'],
    y=df35['21년 주택 보유율'], marker_color='#ff5500')
    ])

    for i, bar in enumerate(fig1.data):
        for j, val in enumerate(bar.y):
            fig1.add_annotation(
                x=bar.x[j],
                y=val,
                text=str(val),
                showarrow=False,
                font=dict(color='black', size=14),  # 레이블 폰트 스타일 설정
                xshift=0,  # x축으로 이동
                yshift=8,  # y축으로 이동
                align='center'  # 중앙 정렬
    )
        
    fig1.update_layout(barmode='group')

    fig1.update_yaxes(range=[30, 55])
    st.plotly_chart(fig1)




    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ 21년도 신혼부부 주택소유별 평균 소득 비중 현황\n(주택소유 여부에 따른 소득 차이)')

    df4 = pd.read_csv('./data/newlywed_house_salary.csv')
    df4_2 = df4.loc[(df4['시점']==2021),["신혼부부 특성별(2)","데이터"]]
    df4_2=df4_2.rename(columns={'신혼부부 특성별(2)':'주택 소유 여부','데이터':'소득 평균(만원)'})


    fig2 = px.pie(df4_2, values='소득 평균(만원)', names=['주택 미소유','주택 소유'])
    fig2.update_traces(marker_colors =['#ecddfe','#ff5500'], textfont_size=20)

    st.plotly_chart(fig2)