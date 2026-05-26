from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()

# Optional: open fresh browser
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

login_details = [
    # ['admin@gmail.com', 'Test@123'],
    # ['abc@gmail.com', 'passwors@123'],
    # ['xx@yahoo.com', 'password@123'],
    # ['ds45063@gmail.com', 'Deepak@123'],
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

#---open the admin page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
if 'viewSystemUsers' in driver.current_url:
    print("Admin page is open")
else:
    print("Admin page is not open")
time.sleep(3)

#-- open the PIM page
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
if 'viewEmployeeList' in driver.current_url:
    print("PIM page is open")
else:
    print("PIM page is not open")
time.sleep(3)

#---open the leave page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
if 'viewLeaveList' in driver.current_url:
    print("LEAVE page is open")
else:
    print("LEAVE page is not open")
time.sleep(3)

#--Open the Time page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
if 'viewEmployeeTimesheet' in driver.current_url:
    print("Time page is open")
else:
    print("Time page is not open")
time.sleep(3)

#---open the Recruitment page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
if 'viewCandidates' in driver.current_url:
    print("Recruitment page is open")
else:
    print("Recruitment page is not open")
time.sleep(3)

#--Open my info page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
if 'viewPersonalDetails' in driver.current_url:
    print("Info page is open")
else:
    print("Info page is not open")
time.sleep(3)

#---Open Performance page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
if 'searchEvaluatePerformanceReview' in driver.current_url:
    print("Performance review page is open")
else:
    print("Performance review page is not open")
time.sleep(3)

#--Open the Directory page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').click()
if 'viewDirectory' in driver.current_url:
    print("Directory page is open")
else:
    print("Directory page is not open")
time.sleep(3)

#--Open the Maintenance page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()
if 'maintenance' in driver.current_url:
    print("Maintenance page is open")
else:
    print("Maintenance page is not open")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[1]').click()
time.sleep(3)

#--Open the claim page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').click()
if 'viewAssignClaim' in driver.current_url:
    print("Claim page is open")
else:
    print("Claim page is not open")
time.sleep(3)

#--Open the Buzz page
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span').click()
if 'viewBuzz' in driver.current_url:
    print("Buzz page is open")
else:
    print("Buzz page is not open")
time.sleep(3)

# #---click on the profile icon
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li').click()
# time.sleep(2)
#
# #---click on the logout button
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a').click()
# if 'login'in driver.current_url:
#     print("Logout successfully")
# else:
#     print("You are still in website")

input("Press Enter to close browser")
driver.quit()