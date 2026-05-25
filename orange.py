from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()

# Optional: open fresh browser
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

login_details = [
    ['admin@gmail.com', 'Test@123'],
    ['abc@gmail.com', 'passwors@123'],
    ['xx@yahoo.com', 'password@123'],
    ['ds45063@gmail.com', 'Deepak@123'],
    ['Admin', 'admin123']
]

for data in login_details:

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    email = data[0]
    password = data[1]

    # --- Username field
    username_field = driver.find_element(By.NAME, 'username')
    username_field.clear()
    username_field.send_keys(email)

    time.sleep(2)

    # --- Password field
    password_field = driver.find_element(By.NAME, 'password')
    password_field.clear()
    password_field.send_keys(password)

    time.sleep(2)

    # --- Click login button
    login_button = driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    )

    login_button.click()

    time.sleep(3)

    # --- Validation
    if "dashboard" in driver.current_url:
        print(f"Login Passed for: {email}")
    else:
        print(f"Login Failed for: {email}")

    #---click on the profile icon
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li').click()
time.sleep(2)

#---click on the logout button
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a').click()


driver.quit()