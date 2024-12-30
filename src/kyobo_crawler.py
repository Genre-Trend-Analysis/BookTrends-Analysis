import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--headless')  # 브라우저 창을 띄우지 않음
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# 현재 2024년 1 ~ 11월까지만 나와있음
def get_url(year, month, page):
    return f'https://store.kyobobook.co.kr/bestseller/online/monthly?page={page}&per=50&ymw={year}{month:02d}'

def crawling_monthly(year, month):
    data = []
    for page in range(1, 3):
        driver = webdriver.Chrome(options=options)
        url = get_url(year, month, page)
        driver.get(url)
        time.sleep(5)
        
        # 광고 제거
        try:
            ad_element = driver.find_element(By.CSS_SELECTOR, ".absolute.bottom-\\[85px\\].right-\\[27px\\].h-\\[30px\\].w-\\[30px\\].p-\\[3px\\]")
            ad_element.click()
            driver.find_element(By.CSS_SELECTOR, ".bg-blue-700").click()
            time.sleep(5)
        except Exception as e:
            print(f'광고 없음 혹은 제거 실패: {e}')
        
        try:
            # 책 목록들
            book_list = driver.find_elements(By.CSS_SELECTOR, ".mt-9.pt-9.border-t.border-gray-300")
            if not book_list:
                print(f"{page}가 없음.")
                break
            time.sleep(5)
        except Exception as e:
            print(f'{page}로드 실패')
            break

        for book in book_list:
            time.sleep(4)
            title_element = book.find_element(By.CSS_SELECTOR, '.prod_link.font-weight-medium.line-clamp-2.text-black')
            title = title_element.text

            # author, publisher, date
            elements = book.find_element(By.CSS_SELECTOR, '.line-clamp-2.flex.overflow-hidden.whitespace-normal.break-all.text-gray-800.fz-14.mt-1').text
            if len(elements.splitlines()) > 1:
                detail = elements.splitlines()[0].split('·')
                date = elements.splitlines()[1].replace("· ", "").strip()

                if len(detail) > 1:
                    author = detail[0].strip()
                    publisher = detail[1].strip()
                else:
                    author, publisher = "None", "None"
        
            time.sleep(2)

            # 데이터 저장
            data.append({
                "Month": month,
                "Title": title,
                "Author": author,
                "Publisher": publisher,
                "Publish_Date": date,
            })

            time.sleep(2)
        print(data)
    
    return data
        
        
def df_to_csv():
    for month in range(1, 12):
        monthly_data = crawling_monthly(2024, month)
        df = pd.DataFrame(monthly_data)

        # csv로 저장
        if not df.empty:
            # 프로젝트 루트 디렉터리 기준으로 'data' 디렉터리 접근
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 두 번 상위 디렉터리로 올라가기
            data_dir = os.path.join(project_root, 'data_kyobo')
            file_name = os.path.join(data_dir, f'kyobo_bestseller_synthesis_{2024}년 {month:02d}월.csv')
            df.to_csv(file_name, index=False)
            print(f"{month}월 csv 저장")

def csv_add_category():
    for month in range(1, 12):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 두 번 상위 디렉터리로 올라가기
        data_dir = os.path.join(project_root, 'data_kyobo')
        file_name = os.path.join(data_dir, f'kyobo_bestseller_{2024}년 {month:02d}월.csv')
        
        df = pd.read_csv(file_name)
        
        category_dir = os.path.join(project_root, 'data_yes24')
        
        df['Category'] = '일반'
        
        for f in os.listdir(category_dir):
            if f.endswith('.csv'):
                category_name = f.replace('_df.csv', '')
                category_df = pd.read_csv(os.path.join(category_dir, f))
                
                for index, row in df.iterrows():
                    if row['Title'] in category_df['제목'].values:
                        df.at[index, 'Category'] = category_name
        output_path = os.path.join(data_dir, f'kyobo_bestseller_{2024}년 {month:02d}월.csv') 
        df.to_csv(output_path, index=False)
        print(f"처리 완료: {file_name}")
        
    print("모든 CSV 파일 처리가 완료되었습니다!")
    
if __name__ == "__main__":
    df_to_csv()
    #csv_add_category()
    driver.quit()