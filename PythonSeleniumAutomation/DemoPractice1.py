import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Locators

driver.get("https://rahulshettyacademy.com/angularpractice/")

#Locators- id , X-Path

driver.find_element(By.NAME, "name").send_keys("SANKET PATIL")
driver.find_element(By.NAME, "email").send_keys("patilsanket792@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Sanket@9538")


driver.find_element(By.ID,"exampleCheck1").click()

driver.find_element(By.XPATH , "//input [@type='submit']").click()
driver.find_element(By.XPATH,"//input[@value='option1']").click()
message=driver.find_element(By.CLASS_NAME, "alert-success").text



print(message)

assert "Success" in message













time.sleep(15)