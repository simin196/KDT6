from selenium import webdriver
from selenium.webdriver.common.by import By
import time

agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' + user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element(By.NAME,'id').send_keys('gusska1966') # 아이디 
driver.find_element(By.NAME,'pw').send_keys('alsdkjf') # 비밀번호

driver.find_element(By.ID, 'log.login').click()
time.sleep(3)
driver.quit()