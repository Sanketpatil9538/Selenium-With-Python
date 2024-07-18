import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()



driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

#click on column header

driver.find_element(By.XPATH,"//span[normalize-space()='Veg/fruit name']").click()

#collect all vegetables names -browsersorted  veggielist  - (A,B,C)


#sort this browsersorted  veggielist =>newSortedlist  (A,B,C)

veggiewebelements =driver.find_elements(By.XPATH,"//tr/td[1]")   #This are web elements only . we need to iterate throuh loop and then pull out text

browsersortedveggies=[]
for vegglist in veggiewebelements:
    browsersortedveggies.append( vegglist.text)

originalbrowsesortedlist =browsersortedveggies.copy()  #.cpoy()- creating the new copy of the list, we have to use .copy() methods so that it creats another copy of the list

print(originalbrowsesortedlist)

browsersortedveggies.sort()

print(browsersortedveggies)

#browsersorted  veggielist ==newSortedlist ---- use assert for verification

assert originalbrowsesortedlist  == browsersortedveggies
#if there is bug in browser sorted list , then it will fail
#If there is bug this assertion will fail


