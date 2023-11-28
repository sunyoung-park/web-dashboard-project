import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.subplots as sp

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def run_work_app():
    st.title("'맞벌이' 신혼부부 비중")

    st.subheader('✤ 연도별 우리나라 총 신혼부부 맞벌이 비중(%)')

    df5 = pd.read_csv('./data/newlywed_all.csv')

    fig = px.bar(df5, x='시점', y='맞벌이 비율 (B/A*100)', color='맞벌이 비율 (B/A*100)', color_continuous_scale='peach',labels=dict(시점="연도"))
    fig.update_yaxes(range=[35, 60])
    
    fig.update_layout(margin_l=100
                       ,margin_r=70)
    st.plotly_chart(fig)

    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ (15-21년) 신혼 부부의 맞벌이/외벌이 추이(%)')
    colors3=px.colors.qualitative.T10
    df5['외벌이 비율 ((A-B)/A*100)']=(df5['신혼부부 수 (A)']-df5['맞벌이 부부 수 (B)'])/df5['신혼부부 수 (A)']*100
    df5['외벌이 비율 ((A-B)/A*100)'] =df5['외벌이 비율 ((A-B)/A*100)'].round(2)

    df5.rename(columns={'맞벌이 비율 (B/A*100)':'맞벌이 비율','외벌이 비율 ((A-B)/A*100)':'외벌이 비율'}, inplace = True)
    df5554 = df5[['시점','맞벌이 비율','외벌이 비율']]

    fig1 = px.line(df5554, x='시점', y=['맞벌이 비율','외벌이 비율'],markers=True,labels=dict(시점="연도", value='비율'))    

    fig1.update_traces(line_width=2,marker_size=20)
    fig1.update_layout(margin_l=100
                       ,margin_r=70)
    
    st.plotly_chart(fig1)

    

    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ 21년 n년차 부부 맞벌이 비중(%)')

    df6 = pd.read_csv('./data/couple_work.csv')
    
    df6['전체'] = df6['맞벌이']+df6['외벌이']
    fgg=df6['맞벌이']/df6['전체']*100
    df6['맞벌이 비율']=fgg.round(2)
    working_list= df6['신혼부부 특성별(2)'].values


    selected_working = st.selectbox('혼인 연차를 선택하세요.', working_list)

    
    sw_result=df6.loc[df6['신혼부부 특성별(2)']==selected_working,'맞벌이 비율'].values[0]

    if selected_working == '혼인 1년차':
        st.subheader(str(selected_working) + ' 의 맞벌이 비율은 ' )
        st.title(str(sw_result) + '\% 입니다.')
    elif selected_working == '혼인 2년차':
        st.subheader(str(selected_working) + ' 의 맞벌이 비율은 ' )
        st.title(str(sw_result) + '\% 입니다.')
    elif selected_working == '혼인 3년차':
        st.subheader(str(selected_working) + ' 의 맞벌이 비율은 ' )
        st.title(str(sw_result) + '\% 입니다.')
    elif selected_working == '혼인 4년차':
        st.subheader(str(selected_working) + ' 의 맞벌이 비율은 ' )
        st.title(str(sw_result) + '\% 입니다.')
    elif selected_working == '혼인 5년차':
        st.subheader(str(selected_working) + ' 의 맞벌이 비율은 ' )
        st.title(str(sw_result) + '\% 입니다.')

        
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.subheader('✤ 맞벌이 비율과 첫자녀 출산 부부 혼인연도별 비교')

    df7=pd.read_csv('./data/couple_baby.csv')
    df7 =df7.rename(columns={'데이터':'첫자녀 출산 부부'})
    df7
    df6['첫자녀 출산 부부']=df7['첫자녀 출산 부부']
    df6

    colors=px.colors.sequential.Peach
    colors2=px.colors.sequential.Blugrn
    fig11 = go.Figure()

    fig11 = make_subplots(specs=[[{"secondary_y": True}]])

    fig11.add_trace(go.Bar(x=df6['신혼부부 특성별(2)'],y=df6["맞벌이 비율"],name="맞벌이 비율",marker_color=colors),secondary_y=False)
    fig11.add_trace(go.Scatter(x=df7['신혼부부 특성별(2)'],y=df7["첫자녀 출산 부부"],mode='lines+markers',
        name="첫자녀 출산 부부수",marker_size=20,marker_line_color=colors2),secondary_y=True)

    fig11.update_layout(
        xaxis_title='혼인연차별',
        yaxis_title='맞벌이 비율',
        yaxis2_title='첫자녀 출산 부부',
        margin_l=100,
        margin_r=70
    )

    st.plotly_chart(fig11)

    
    
    st.text('')
    st.text('')
    st.text('')    
    st.text('')
    st.text('')
    st.text('')
    st.title('🧺')
    st.title('가사분담은 어떻게 해야한다고 생각하는지?')
    st.title('.')
    st.title('.')

    st.subheader('✤ 가사분담에 대한 견해')

    df8=pd.read_csv('./data/homework.csv')

    fig2 = px.pie(df8, values='2022', names=['남편이 전적으로 책임','남편이 주로 하고 아내도 분담','공평하게 분담','아내가 주로 하고 남편도 분담','아내가 전적으로 책임'])
    fig2.update_traces(marker_colors =px.colors.qualitative.Set3)    
    fig2.update_annotations(font=dict(family="Helvetica", size=20))

    
    st.plotly_chart(fig2)

    
    st.text('')
    st.text('')
    st.text('')    
    st.text('')
    st.text('')
    st.text('')
    st.subheader('✤ 실제 가사 분담은 어떻게 이루어지고 있는지?')

    df9=pd.read_csv('./data/homework_real.csv')

    fig3 = px.pie(df9, values='2022', names=['남편이 전적으로 책임','남편이 주로 하고 아내도 분담','공평하게 분담','아내가 주로 하고 남편도 분담','아내가 전적으로 책임'])
    fig3.update_traces(marker_colors =px.colors.qualitative.Set3)
    fig3.update_annotations(font=dict(family="Helvetica", size=20))

    
    st.plotly_chart(fig3)
    st.text('')
    st.text('')
    st.text('')    
    st.text('')
    st.text('')
    st.text('')
    st.subheader('✤ ✤ ')
    st.subheader('가사분담에 대한 견해와 실태 비교')

    # 서브플롯을 만들어 두 개의 파이 차트를 나란히 결합
    fig4 = sp.make_subplots(rows=1, cols=2, subplot_titles=['견해', '실태'],specs=[[{"type": "pie"}, {"type": "pie"}]],
    shared_yaxes=True, # 특정 축을 공유하게 그래프를 그릴 수 있음
    horizontal_spacing=0.05, # 너비 간격을 설정할 수 있음
    column_widths=[0.5, 0.5])

    fig4.add_trace(fig2.data[0], row=1, col=1)
    fig4.add_trace(fig3.data[0], row=1, col=2)

    # 레이아웃 및 사이즈 조정
    fig4.update_layout(height=650, width=1000, margin_l=70)
    fig4.update_traces(textfont_size=20)
    fig4.update_annotations(font=dict(family="Helvetica", size=20))

# 스트림릿에 플롯 출력
    st.plotly_chart(fig4)






