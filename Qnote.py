import time

import by
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://notes.quizsagar.com/")
driver.maximize_window()

#----open register page
driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a').click()
time.sleep(3)

#---Open the login page
driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
time.sleep(3)





# input("Press enter to close browser....")
driver.quit()