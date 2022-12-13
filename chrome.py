#to use chromium with Selenium we need to install
#sudo apt-get install chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://www.google.com/")
time.sleep(10)
#identify the Google search text box and enter the value  
my_element = driver.find_element("name","q")
my_element.send_keys('instagram')
#driver.find_element_by_name("q").send_keys("javatpoint  ")  
time.sleep(3)
my_element.send_keys(Keys.ENTER)
time.sleep(10)
