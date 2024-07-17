import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)


results=driver.find_elements(By.XPATH,"//div[@class='products'] /div")
count=len(results)

assert count  > 0

for  result in results:
    result.find_element(By.XPATH,"div/button").click()   #Chaining of web elements [Chaining of Parent web elements to child web elelments to construct dynamically ]



driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
time.sleep(20)
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
