import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)
search_box = driver.find_element(By.XPATH, "/html/body/ntp-app//div/div[3]/ntp-searchbox//div/cr-searchbox-input//div/textarea")
search_box.send_keys("GERMIS")
driver.quit()
