import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def run_char_app():
    st.title("우리나라 신혼부부 '특성별' 조사")

    df=pd.read_csv('./data/city_province_newlyweds_overal.csv')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('(2015-2021)우리나라 전국 총 신혼부부(연도별)')

    df01 = df.loc[df['행정구역별'] == '전국',['시점','신혼부부 수 (A)']]

    fig = px.bar(df01, x='시점', y='신혼부부 수 (A)',
             text_auto=False, color = '신혼부부 수 (A)', color_continuous_scale='peach')
    st.plotly_chart(fig)


    
    st.text('')
    st.text('')
    st.text('')

    st.subheader('(2015-2021)우리나라 전국 총 신혼부부 수(시도별)')

    df02 = df[['시점','행정구역별','신혼부부 수 (A)']]
    df02 = df02.drop(df02[df02['행정구역별'] == '전국'].index,axis=0)

    fig1 = px.line(df02, x='시점', y='신혼부부 수 (A)', color='행정구역별',markers=True)

    st.plotly_chart(fig1)

    st.text('')
    st.text('')
    st.text('')

    st.subheader('신혼부부 특성별 평균소득 현황')

    df2 = pd.read_csv('./data/newlywed_couple_ income_status.csv')
    df2 = df2.rename(columns={'데이터':'소득 평균(만원)'})
    df2.drop('소득구간별(1)',axis=1)
    df2=df2[df2['신혼부부 특성별(1)']!='전국']


    year_list = df2['시점'].unique()
    char_list1 = df2['신혼부부 특성별(1)'].unique()

    selected_year = st.selectbox('연도를 선택하세요.', year_list)
    
    # df2_result_final = df2.loc[(df2['시점']==selected_year) & (df2['신혼부부 특성별(1)']=='혼인1년차')& (df2['신혼부부 특성별(2)']=='혼인1년차'),'소득 평균(만원)'].values

    selected_char1 = st.selectbox('특성항목을 선택하세요.', char_list1)

    if selected_char1 == '혼인연차별':
        selected_married=df2.loc[df2['신혼부부 특성별(1)']=='혼인연차별','신혼부부 특성별(2)'].unique()
        selected_char2 = st.selectbox('혼인연차를 선택하세요.', selected_married)
    elif selected_char1 == '시도별':
        selected_city=df2.loc[df2['신혼부부 특성별(1)']=='시도별','신혼부부 특성별(2)'].unique()
        selected_char2 = st.selectbox('시도를 선택하세요.', selected_city)
    elif selected_char1 == '맞벌이여부별':
        selected_work=df2.loc[df2['신혼부부 특성별(1)']=='맞벌이여부별','신혼부부 특성별(2)'].unique()
        selected_char2 = st.selectbox('맞벌이 여부를 선택하세요.', selected_work)
    elif selected_char1 == '출산자녀수별':        
        selected_baby=df2.loc[df2['신혼부부 특성별(1)']=='출산자녀수별','신혼부부 특성별(2)'].unique()
        selected_char2 = st.selectbox('출산자녀수를 선택하세요.', selected_baby)

    else:        
        selected_house=df2.loc[df2['신혼부부 특성별(1)']=='주택소유물건수별','신혼부부 특성별(2)'].unique()
        selected_char2 = st.selectbox('출산자녀수를 선택하세요.', selected_house)

    df2_result = (df2['시점']==selected_year)&(df2['신혼부부 특성별(1)']==selected_char1)&(df2['신혼부부 특성별(2)']==selected_char2)
    
    df2_result_final = df2.loc[df2_result,'소득 평균(만원)'].values[0]

    st.subheader('해당 특성의 신혼부부의 평균소득은 ')
    st.title( str(df2_result_final)+ '만원 입니다.')



    

    st.subheader(df2.loc[(df2[selected_year] == df2[selected_year])
                         &(df2[selected_char1] == df2[selected_char1])
                         &(df2[selected_char2] == df2[selected_char2]),'소득 평균(만원)']
                         .values[0])
    

    st.dataframe(df2)

def new_func(df2_result):
    new_var = df2_result
    return new_var