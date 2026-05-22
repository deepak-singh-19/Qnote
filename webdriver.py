# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://google.com")
# driver.maximize_window()
# time.sleep(5)
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Red bus")
# search_box.submit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# 1. Navigate
driver.get("https://www.google.com")
driver.maximize_window()

# 2. Find the element using a reliable locator (Name is better than long XPath)
# In Google, the search bar name attribute is 'q'
search_box = driver.find_element(By.NAME, "q")

# 3. Action
search_box.send_keys("red bus")

# 4. Submit the search
search_box.submit()

print("Script executed successfully!")