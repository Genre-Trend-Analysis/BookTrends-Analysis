import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import os

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
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    total_file = os.path.join(data_dir, "novel_bestseller(total).csv")

    #plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.figure(figsize=(12, 5))
    
    novel_per = pd.read_csv(total_file, index_col=0)
    # Plot each series
    for column in novel_per.columns:
        plt.plot(novel_per.index, novel_per[column], marker='o', ms=4, label=column)
        # Annotate each data point with its value
        for i, value in enumerate(novel_per[column]):
            plt.text(novel_per.index[i], value, str(value), fontsize=12, ha='center', va='bottom')
    # Customize the plot
    plt.xlabel('월', labelpad=15, fontsize=12)
    plt.xticks(range(1, 13), range(1, 13), fontsize=13)
    plt.ylabel('소설의 점유율(%)', labelpad=15, fontsize=12)
    plt.yticks(fontsize=13)
    plt.title('2024년 소설의 베스트셀러 점유율', pad=13, fontsize=15)
    # Add legend
    plt.legend(title='온라인 서점', title_fontsize=10, fontsize=8)
    # Show the plot
    st.pyplot(plt)

def page1():
    st.title("교보문고")
    st.write("데이터 분석 결과")
    
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    yes24_file = os.path.join(data_dir, "genre_novel(kyobo).csv")
    genre_per_kyo = pd.read_csv(yes24_file, index_col=0)
    
    #plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.figure(figsize=(12, 5))
    # Define colors for each genre
    colors = ['blue', 'red', 'green', 'darkgrey', 'orange', 'darkgrey', 'salmon']
    genres = genre_per_kyo.columns
    # Plot each genre with a unique color
    for genre, color in zip(genres, colors):
        plt.plot(genre_per_kyo.index, genre_per_kyo[genre], marker='o', ms=3, linewidth=1, label=genre, color=color)
    # Customize the plot
    plt.xlabel('월', labelpad=10, fontsize=12)  # Labelpad: space
    plt.xticks(range(1, 13), range(1, 13), fontsize=13)
    plt.ylabel('각 장르의 점유율(%)', labelpad=10, fontsize=12)
    plt.yticks(fontsize=13)
    plt.title('하위 장르소설의 전체 장르소설에서의 점유율_교보문고', pad=13, fontsize=15)
    # Add legend
    plt.legend(title='하위 장르', title_fontsize=10, fontsize=8)
    # Show the plot
    st.pyplot(plt)

def page2():
    st.title("예스24")
    st.write("데이터 분석 결과")
    
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    yes24_file = os.path.join(data_dir, "genre_novel(yes).csv")
    genre_per_yes = pd.read_csv(yes24_file, index_col=0)

    #plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.figure(figsize=(12, 5))
    # Define colors for each genre
    colors = ['blue', 'red', 'green', 'darkgrey', 'orange', 'darkgrey', 'salmon']
    genres = genre_per_yes.columns
    # Plot each genre with a unique color
    for genre, color in zip(genres, colors):
        plt.plot(genre_per_yes.index, genre_per_yes[genre], marker='o', ms=3, linewidth=1, label=genre, color=color)
    # Customize the plot
    plt.xlabel('월', labelpad=10, fontsize=12)  # Labelpad: space
    plt.xticks(range(1, 13), range(1, 13), fontsize=13)
    plt.ylabel('각 장르의 점유율(%)', labelpad=10, fontsize=12)
    plt.yticks(fontsize=13)
    plt.title('하위 장르소설의 전체 장르소설에서의 점유율_교보문고', pad=13, fontsize=15)
    # Add legend
    plt.legend(title='하위 장르', title_fontsize=10, fontsize=8)
    # Show the plot
    st.pyplot(plt)
    
    # 장르 소설 베스트셀러 월별/장르별 조회
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    data_path = os.path.join(data_dir, "genre_yes.csv")
    data_yes = pd.read_csv(data_path)

    #data_yes['월'] = data_yes['월'].astype(str).str.replace('|', '').str.strip()
    st.write('')
    st.write('')
    st.write('')
  
    st.markdown("""
    <p style='text-align: center; color: #FFFFFF; font-size: 20px;'>
                <b>월별 소설 데이터 내 장르별 소설 순위 데이터 조회</b></p>             
    """, unsafe_allow_html=True)


    selected_month = st.selectbox('월 선택', options=data_yes['월'].unique())
    selected_genre = st.selectbox('장르 선택', options=data_yes['genre'].unique())
 
    filtered_data = data_yes[(data_yes['월'] == selected_month) & (data_yes['genre'] == selected_genre)]

    
    st.write(f"선택된 월: {selected_month}, 장르: {selected_genre}의 데이터")
    st.dataframe(filtered_data)

def page3():
    st.title("알라딘")
    st.write("데이터 분석 결과")
    
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    aladin_file = os.path.join(data_dir, "genre_novel(ala).csv")
    genre_per_ala = pd.read_csv(aladin_file, index_col=0)

    #plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.figure(figsize=(12, 5))
    # Define colors for each genre
    colors = ['blue', 'red', 'green', 'darkgrey', 'orange', 'darkgrey', 'salmon']
    genres = genre_per_ala.columns
    # Plot each genre with a unique color
    for genre, color in zip(genres, colors):
        plt.plot(genre_per_ala.index, genre_per_ala[genre], marker='o', ms=3, linewidth=1, label=genre, color=color)
    # Customize the plot
    plt.xlabel('월', labelpad=10, fontsize=12)  # Labelpad: space
    plt.xticks(range(1, 13), range(1, 13), fontsize=13)
    plt.ylabel('각 장르의 점유율(%)', labelpad=10, fontsize=12)
    plt.yticks(fontsize=13)
    plt.title('하위 장르소설의 전체 장르소설에서의 점유율_교보문고', pad=13, fontsize=15)
    # Add legend
    plt.legend(title='하위 장르', title_fontsize=10, fontsize=8)
    # Show the plot
    st.pyplot(plt)

    st.write('')
    st.write('')
    st.write('')
    # 종합 소설 베스트셀러 월별 조회
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    data_path = os.path.join(data_dir, "novel_bestseller(ala).csv")
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
    project_root = os.path.dirname(os.getcwd())  
    data_dir = os.path.join(project_root, 'datas')
    data_path = os.path.join(data_dir, "genre_novel_bestseller(ala).csv")
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
    