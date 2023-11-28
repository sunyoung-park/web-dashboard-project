import streamlit as st

def run_home_app():
    st.balloons()
    st.write('Republic of Korea Ministry of Defense statistical survey')
    st.title('대한민국 신혼부부 통계자료 조사')
    
    st.text('')
    st.text('')
    st.text('')
    img_url = './data/mc_img2.png'

    st.image(img_url)
    st.text('')
    st.text('')
    st.text('')
    st.title('✤')
    st.subheader('통계청 신혼부부통계 작성 대상')
    st.text('▶ 매년 11월 1일 기준')
    st.text('▶ 혼인 신고한 지 5년 이내')
    st.text('▶ 혼인관계 유지')
    st.text('▶ 부부 중 1명 이상 국내에 거주')
    
    