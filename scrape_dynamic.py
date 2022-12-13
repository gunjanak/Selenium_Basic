from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions



#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = ChromeOptions()

options.BinaryLocation = "/usr/bin/chromium-browser"
options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://quotes.toscrape.com/js")
element = driver.find_element(By.CLASS_NAME,"author")
print(element.text)

elements = driver.find_elements(By.CLASS_NAME,"author")

for element in elements:
    print(element.text)
time.sleep(1)



soup = BeautifulSoup(driver.page_source,'lxml')
author_element =soup.find("small",class_="author")
print(author_element)
driver.quit()

