import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()



driver.implicitly_wait(10)


#go to the e-commerce wesite

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#click on shop

driver.find_element(By.XPATH,"//a[normalize-space()='Shop']").click()

#pass the product name from the script

#go to chekout

#click on checkout
driver.find_element(By.XPATH,"//button[normalize-space()='Checkout']").click()

#Auto-suggestive dropdwon - enter "ind" and then click on india

#click on terms and conditons checkbox


#click on purchase

#verify the success messge is displayed using assertion
