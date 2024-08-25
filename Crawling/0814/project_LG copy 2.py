'''
LG디스플레이
>> https://finance.naver.com/item/coinfo.naver?code=034220

LG전자
>> https://finance.naver.com/item/coinfo.naver?code=066570


재무 분석>> 포괄손익계산서 / 재무상태표 / 현금 흐름표>> 각 항목text

항목
>> PER, PBR, ROE, 영업이익증가율, 투자활동현금흐름

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Chrome 드라이버 자동 설치 및 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 네이버 금융 URL
url = "https://finance.naver.com/item/coinfo.naver?code=066570"
driver.get(url)

# 페이지가 완전히 로드될 때까지 대기
time.sleep(3)

# 필요한 데이터가 담긴 iframe으로 전환
driver.switch_to.frame(driver.find_element(By.ID, 'coinfo_cp'))

# 테이블 데이터 추출
table = driver.find_element(By.CLASS_NAME, 'cmp-table')

data = {
    '연도': [],
    'PER': [],
    'PBR': [],
    'ROE': [],
    '영업이익증가율': [],
    '투자활동현금흐름': []
}

# 테이블 내에서 데이터 추출
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    if len(cols) > 1:  # 데이터가 존재하는지 확인
        data['연도'].append(row.find_element(By.TAG_NAME, 'th').text.strip())
        data['PER'].append(cols[0].text.strip())
        data['PBR'].append(cols[1].text.strip())
        data['ROE'].append(cols[2].text.strip())
        data['영업이익증가율'].append(cols[3].text.strip())
        data['투자활동현금흐름'].append(cols[4].text.strip())

# pandas 데이터프레임 생성
df = pd.DataFrame(data)
df.set_index('연도', inplace=True)

# 데이터프레임 출력
print(df)

# 드라이버 종료
driver.quit()