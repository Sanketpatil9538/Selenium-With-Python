import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action=ActionChains(driver)   #import this



#for all the actions , .perform must be there for all the actions 
action.click_and_hold()
#action.double_click(driver.find_element(xpath location))
action.context_click() #right clikc
action.drag_and_drop(
# it will move only to the element - not performig any actions
action.move_to_element(driver.find_element(By.ID,"//button[@id='mousehover']")).perform())




