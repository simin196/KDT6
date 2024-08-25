from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버 설정
driver = webdriver.Chrome()
driver.get("https://finance.naver.com/item/coinfo.naver?code=034220")

# iframe으로 전환
driver.switch_to.frame("coinfo_cp")

# PER, PBR, ROE, 영업이익률, 투자활동현금흐름 데이터 가져오기
per = driver.find_element(By.XPATH, "//some_xpath_for_per").text
pbr = driver.find_element(By.XPATH, "//some_xpath_for_pbr").text
roe = driver.find_element(By.XPATH, "//some_xpath_for_roe").text
operating_profit_margin = driver.find_element(By.XPATH, "//some_xpath_for_profit_margin").text
cash_flow = driver.find_element(By.XPATH, "//some_xpath_for_cash_flow").text

print(f"PER: {per}, PBR: {pbr}, ROE: {roe}, 영업이익률: {operating_profit_margin}, 투자활동현금흐름: {cash_flow}")

driver.quit()