from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Open URL
driver.get("http://germisstaging.gujarat.gov.in/frmLogin.aspx")
driver.maximize_window()

# Create wait object
wait = WebDriverWait(driver, 10)

# ---------------- LOGIN DETAILS ----------------

# Enter User ID
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ContentPlaceHolder1_Txt_UserName")
    )
).send_keys("p@yahoo.com")

# Enter Password
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ContentPlaceHolder1_Txt_Password")
    )
).send_keys("HIger@189")

# ---------------- CAPTCHA HANDLING ----------------

# Read first number
num1 = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ContentPlaceHolder1_Lbl_FirstNumber")
    )
).text

# Read second number
num2 = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ContentPlaceHolder1_Lbl_SecondNumber")
    )
).text

# Read operator
operator = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="ContentPlaceHolder1_LoginPanel"]/div[3]/div[2]')
    )
).text

# Convert string to integer
num1 = int(num1)
num2 = int(num2)

# Perform calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

# Enter captcha result
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ContentPlaceHolder1_TxtCapta")
    )
).send_keys(str(result))

# Click submit button
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "ContentPlaceHolder1_Btn_Submit")
    )
).click()

# ---------------------------------------------------
# Browser should not close automatically
input("Press Enter to close browser...")

driver.quit()