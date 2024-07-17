import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()


# switching to i-frame

driver.switch_to.frame("mce_0_ifr")  #In bracket , frame id is there from html code ,or u can use name also
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

#The above part is in iframe tag but to switch to main window, we use default_content
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//h3[normalize-space()='An iFrame containing the TinyMCE WYSIWYG Editor']").text)