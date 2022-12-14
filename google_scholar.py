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
time.sleep(1)
#identify the Google search text box and enter the value  
my_element = driver.find_element("name","q")
my_element.send_keys('cryptography')


my_element.send_keys(Keys.ENTER)
time.sleep(3)
#Trying to click Custom range...
#By.CLASS_NAME,"author"
link = driver.find_element(By.LINK_TEXT,"Custom range...")
link.click()
time.sleep(2)

#Fill values of custom range
year_low = driver.find_element(By.ID,"gs_as_ylo")
driver.implicitly_wait(5)
print(year_low)
year_low.send_keys("1900")
print(year_low.get_attribute('value'))
year_low.send_keys(Keys.TAB)
focused_elem = driver.switch_to.active_element
print(focused_elem)
focused_elem.send_keys("2008")
focused_elem.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()
