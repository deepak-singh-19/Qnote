import time

import by
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://notes.quizsagar.com/")
driver.maximize_window()

#---Verify the page
if "QNote" in driver.title:
    print("QNote page is open")
else:
    print("QNote page is not open")

#----open register page
# driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a').click()
# if "register" in driver.current_url:
#     print("register page is open successfully")
# else:
#     print("register page is not open")
# time.sleep(3)
#
# #---Open the login page
driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
if "login" in driver.current_url:
    print("login page is open successfully")
else:
    print("login page is not open")
time.sleep(3)
driver.find_element(By.ID, 'email').send_keys("ds45063@gmail.com")
time.sleep(3)
driver.find_element(By.ID, 'password').send_keys("Deepak@123")

#---expected values
expected_username = "ds45063@gmail.com"
expected_password = "Deepak@123"

#---Actual value
actual_username = driver.find_element(By.ID, 'email').get_attribute("value")
actual_password = driver.find_element(By.ID, 'password').get_attribute("value")

if actual_username == expected_username and actual_password == expected_password:
    print("login test case is passed")
else:
    print("login test case failed")

#------Click on the login button
driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[4]/button').click()
if "dashboard" in driver.current_url:
    print("dashboard page is open")
else:
    print("dashboard page is not open")
time.sleep(3)

#--open the feedback popp
driver.find_element(By.ID, 'feedbackBtn').click()
time.sleep(2)
#---close the feedback popup
driver.find_element(By.XPATH, '//*[@id="feedbackModal"]/div/div/div[1]/button').click()

#-----Click on the logout button
# driver.find_element(By.ID, 'profileDropdown').click() #--Click on the profile button
# time.sleep(3)
#
# logout_btn = driver.find_element( By.XPATH,"//button[contains(.,'Log Out')]")
#
# # JavaScript click
# driver.execute_script("arguments[0].click();", logout_btn)
#
# print("Logout successful")

input("Press enter to close browser....")
driver.quit()