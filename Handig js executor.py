import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


ChromeOptions = webdriver.ChromeOptions()  #for testing in headless mode
ChromeOptions.add_argument("headless")

ChromeOptions.add_argument("--ignore-certificate-errors")  #for ignoreing ssl certification - secutity purposes



driver = webdriver.Chrome(options=ChromeOptions)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


# For scrolling the page ,we usde javascript executor
#This  below code we can use to scrolll down at the end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  #In bracket we had written the javascript code

#By using the above code we can scrol based on our requirements
driver.execute_script("window.scrollBy(0,270)")

#For taking the screenshot
driver.get_screenshot_as_file("screen.png")
time.sleep(10)


