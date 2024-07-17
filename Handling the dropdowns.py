import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

#Locators

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

drpopdown_element=driver.find_element(By.ID,"exampleFormControlSelect1")
dropdown=Select(drpopdown_element)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)