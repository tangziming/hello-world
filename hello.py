from selenium import webdriver 
import time 

driver = webdriver.Chrome()

driver.get("http://192.168.0.90/zfcapp/index.html")

time.sleep(30)

driver.quit()