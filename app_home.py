import streamlit as st

def run_home_app():
    st.write('Republic of Korea Ministry of Defense statistical survey')
    st.title('대한민국 신혼부부 통계자료 조사')
    
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.subheader('신혼부부통계 작성 대상')
    st.text('▶ 매년 11월 1일 기준')
    st.text('▶ 혼인 신고한 지 5년 이내')
    st.text('▶ 혼인관계 유지')
    st.text('▶ 부부 중 1명 이상 국내에 거주')
    
    img_url = 'https://images.unsplash.com/photo-1505765052322-75804bb2e5f1?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

    st.image(img_url)