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
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

# def LG_D():
url1='https://finance.naver.com/item/coinfo.naver?code=034220'
driver = webdriver.Chrome()  # 웹 드라이버 선택 (예: Chrome)
driver.get(url1)  # 접근할 웹 페이지의 URL 입력
iframe_element = driver.find_element(By.ID, "coinfo_cp")
driver.switch_to.frame(iframe_element)  # iframe 내부로 전환
a=driver.find_element(By.CLASS_NAME, "bg_txt")

print(a)

# def LG_E():
#     url2='https://finance.naver.com/item/coinfo.naver?code=066570'
#     html2 = requests.get(url2)
#     soup2 = BeautifulSoup(html2.text, 'html.parser')
#     a1=soup2.find('',{'class':'blind'}).find_all('dd')
