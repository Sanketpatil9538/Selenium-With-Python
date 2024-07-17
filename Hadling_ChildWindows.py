import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()   #Parent window


Windows_opened=driver.window_handles   #it will grab all the windows which got open and it will put/Save  in the list

#Driver switch from parent to child window
driver.switch_to.window(Windows_opened[1])
print(driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']").text)   #Child window
driver.close()
#Driver switch from child to Parent window
driver.switch_to.window(Windows_opened[0])

assert "Opening a new window"==driver.find_element(By.XPATH,"//h3[normalize-space()='Opening a new window']").text
