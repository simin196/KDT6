from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

print(driver.title)
print(driver.page_source) # 전체 html코드를 가져옴
time.sleep(2)
driver.quit()