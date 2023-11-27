import streamlit as st
from app_home import run_home_app
from app_char import run_char_app
from app_house import run_house_app
from app_work import run_work_app


def main():
    

    css = """
    <style>
    /* 여기에 CSS 코드를 추가합니다 */
    @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

    @font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}
    @font-face {
    font-family: 'KIMM_Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2212@1.0/KIMM_Bold.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}
    @font-face {
    font-family: 'KIMM_Thin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2212@1.0/KIMM_Bold.woff2') format('woff2');
    font-weight: 300;
    font-style: normal;
}
    *{    
        font-family: 'KIMM_Thin';
        font_weight: 300;
        color : #ff5500;
    }
    body {
        background-color: #ffffff;
    }
    .ycbcoloraxistitle{
        font-family: 'KIMM_Bold';
    }
    .st-emotion-cache-10trblm {
        font-family: 'KIMM_Bold';
    }
    .st-by{
        background-color: #ecddfe;
    }
    .st-emotion-cache-6qob1r{
        background-color: #ffffff;
    }
    .st-emotion-cache-18ni7ap{
        background-color: #ecddfe;
    }
    .st-emotion-cache-uf99v8{
        background-color: #ecddfe;
    }
    .st-emotion-cache-183lzff{
        font-family: 'KIMM_Thin';
        font-size: 16px;
    }
    .custom-button {
        background-color: #FF6347;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


    menu = ['HOME','우리나라 신혼부부 특성별','신혼부부 주택 소유 비중','맞벌이 신혼부부 비중']

    choice = st.sidebar.selectbox('메뉴선택',menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_char_app()
    elif choice == menu[2] :
        run_house_app()
    elif choice == menu[3] :
        run_work_app()

if __name__ == '__main__' :
    main()