#This script visits google scholar 
#seacrh for articles in cryptography
#then set the custom range from 1900 to 2008

#to use chromium with Selenium we need to install
#sudo apt-get install chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
#options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://scholar.google.com/")
time.sleep(5)
#identify the Google search text box and enter the value  
#my_element = driver.find_element("name","q")
#my_element.send_keys('cryptography')



time.sleep(5)

driver.quit()
