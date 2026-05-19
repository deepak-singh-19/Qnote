import time

import by
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://germisstaging.gujarat.gov.in/frmLogin.aspx")
driver.maximize_window()
time.sleep(3)

#-----------------------------------Enter the login details
#---Enter username
driver.find_element(By.ID, 'ContentPlaceHolder1_Txt_UserName').send_keys("p@yahoo.com")
time.sleep(3)

#--Enter the password
driver.find_element(By.ID, 'ContentPlaceHolder1_Txt_Password').send_keys("HIger@189")
time.sleep(3)

#-------------------------------------Captcha handling----------------------------
#--Read first number
num1 = driver.find_element(By.ID, 'ContentPlaceHolder1_Lbl_FirstNumber').text

#---Read second number
num2 = driver.find_element(By.ID, 'ContentPlaceHolder1_Lbl_SecondNumber').text

#---Read operator
operator = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_LoginPanel"]/div[3]/div[2]').text

#--convert to int
num1 = int(num1)
num2 = int(num2)

#---perform operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

#---- enter captcha result
driver.find_element(By.ID, 'ContentPlaceHolder1_TxtCapta').send_keys(str(result))

#----Click on the submit button
driver.find_element(By.ID, 'ContentPlaceHolder1_Btn_Submit').click()
time.sleep(5)

input("Press Enter to close browser...")

driver.quit()