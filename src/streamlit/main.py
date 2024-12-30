import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

# 페이지 함수 정의
def home_page():
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.markdown("""
    <p style='text-align: center; color: #FFFFFF; font-size: 45px;'>
                <b>2024년 온라인 베스트셀러 :<br>국내 장르별 소설 점유율 분석</b></p>
                <br>
                <br>
    <p style='text-align: center; color: #FFFFFF; font-size: 20px;'>
                <b>3조 &nbsp;&nbsp; 황운서, 김해빈, 이미선</b></p>
    """, unsafe_allow_html=True)
    st.write(" ")

    # 전체 분석_임시
    novel_per_yes = pd.read_csv('C:/Users/NAKUL/sesac_proj_01/my_streamlit_app/novel_bestseller(total).csv', index_col=0)

    plt.figure(figsize=(12, 5))

    plt.plot(novel_per_yes, marker='o')
    plt.xlabel('월', labelpad=15)  # labelpad: 여백 크기
    plt.xticks(fontsize=13)
    plt.ylabel('소설의 점유율(%)', labelpad=15)  # labelpad: 여백 크기
    plt.yticks(fontsize=13)
    plt.title('2024년 소설의 베스트셀러 점유율', pad=15)  # pad: 여백 크기
    plt.legend(title='온라인 서점', title_fontsize=10, fontsize=8)

    st.pyplot(plt)  # Streamlit에 그래프 출력

def page1():
    st.title("페이지 1")
    st.write("교보문고")

def page2():
    st.title("페이지 2")
    st.write("예스24")
    genre_per_yes = pd.read_csv('scv/genre_novel(yes).csv', index_col=0)

    plt.figure(figsize=(12, 5))
    plt.plot(genre_per_yes, marker='o')
    plt.xlabel('월', labelpad=15)  # labelpad: 여백 크기
    plt.xticks(fontsize=13)
    plt.ylabel('각 장르의 점유율(%)', labelpad=15)  # labelpad: 여백 크기
    plt.yticks(fontsize=13)
    plt.title('하위 장르소설의 전체 장르소설에서의 점유율_예스24', pad=15)  # pad: 여백 크기
    plt.legend()
    
    st.pyplot(plt)  # Streamlit에 그래프 출력

def page3():
    st.title("알라딘")
    st.write("데이터 분석 결과")
    genre_per_ala = pd.read_csv('scv/genre_novel(ala).csv', index_col=0)

    plt.figure(figsize=(12, 5))
    plt.plot(genre_per_ala, marker='o')
    plt.xlabel('월', labelpad=15)  # labelpad: 여백 크기
    plt.xticks(fontsize=13)
    plt.ylabel('각 장르의 점유율(%)', labelpad=15)  # labelpad: 여백 크기
    plt.yticks(fontsize=13)
    plt.title('하위 장르소설의 전체 장르소설에서의 점유율_알라딘', pad=15)  # pad: 여백 크기
    plt.legend()
    
    st.pyplot(plt)  # Streamlit에 그래프 출력

    st.write('')
    st.write('')
    st.write('')
    # 종합 소설 베스트셀러 월별 조회
    data_path = 'C:/Users/NAKUL/sesac_proj_01/my_streamlit_app/novel_bestseller(ala).csv'
    data = pd.read_csv(data_path)
    
    st.markdown("""
    <p style='text-align: center; color: #FFFFFF; font-size: 20px;'>
                <b>종합 소설 베스트셀러 데이터 조회</b></p>             
    """, unsafe_allow_html=True)
    
    selected_month = st.selectbox('월 선택', options=data['Month'].unique())
    filtered_data = data[data['Month'] == selected_month]

    st.write(f"선택된 월: {selected_month}의 데이터")
    st.dataframe(filtered_data)

    # 장르 소설 베스트셀러 월별/장르별 조회
    data_path = 'C:/Users/NAKUL/sesac_proj_01/my_streamlit_app/genre_novel_bestseller(ala).csv'
    data = pd.read_csv(data_path)

    data['Month'] = data['Month'].str.replace('|', '').str.strip()
    st.write('')
    st.write('')
    st.write('')
  
    st.markdown("""
    <p style='text-align: center; color: #FFFFFF; font-size: 20px;'>
                <b>월별 소설 데이터 내 장르별 소설 순위 데이터 조회</b></p>             
    """, unsafe_allow_html=True)


    selected_month = st.selectbox('월 선택', options=data['Month'].unique())
    selected_genre = st.selectbox('장르 선택', options=data['Genre'].unique())
 
    filtered_data = data[(data['Month'] == selected_month) & (data['Genre'] == selected_genre)]

    
    st.write(f"선택된 월: {selected_month}, 장르: {selected_genre}의 데이터")
    st.dataframe(filtered_data)

# 옵션 메뉴 설정
with st.sidebar:
    selected = option_menu("Main Menu", ['HOME', 'KYOBO', 'YES24', 'ALADIN'],
                           icons=['house', 'book', 'book', 'book'], menu_icon="cast", default_index=0)
# 페이지 컨텐츠 설정
if selected == "HOME":
    home_page()
elif selected == "KYOBO":
    page1()
elif selected == "YES24":
    page2()
elif selected == "ALADIN":
    page3()
    