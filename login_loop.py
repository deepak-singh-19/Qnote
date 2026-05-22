#--login with loop
import time

import by
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://notes.quizsagar.com/")
driver.maximize_window()

login_data = [
    ['admin@gmail.com', 'Test@123'],
    ['abc@gmail.com', 'passwors@123'],
    ['xx@yahoo.com', 'password@123'],
    ['ds45063@gmail.com', 'Deepak@123']
]
for data in login_data:
    #--open login page
    driver.get("https://notes.quizsagar.com/login")

    email = data[0]
    password = data[1]

#--email field
    email_field = driver.find_element(By.ID, 'email')
    email_field.clear()
    email_field.send_keys(email)
    time.sleep(3)

    #---password field
    password_field = driver.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(2)

    #--click on the login button
    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[4]/button').click()
    if "dashboard" in driver.current_url:
        print("dashboard page is open")
    else:
        print("Login failed")
    time.sleep(3)

input("Press enter to close browser....")
driver.quit()