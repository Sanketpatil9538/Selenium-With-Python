import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chrome_options=webdriver.ChromeOptions()

#U can find out all the arguments on google - chromeoptions argumets for python
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/",)
print(driver.title())




