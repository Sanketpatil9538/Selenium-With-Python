import time

from selenium import webdriver


#Chrome Driver Service




driver = webdriver.Chrome()

driver.get("https://www.syrow.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


























time.sleep(2)
