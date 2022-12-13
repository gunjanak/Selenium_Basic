from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup


#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = ChromeOptions()
options.BinaryLocation = "/usr/bin/chromium-browser"
options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://thehimalayantimes.com")
time.sleep(1)


soup = BeautifulSoup(driver.page_source,'lxml')
#author_element =soup.find("small",class_="ht-homepage-left-one-article")
#print(soup)

output = soup.find(class_="ht-homepage-left-one-article")
print(output.h3.text)
print(type(output))
print('\n\n.........................................................\n\n')
print(output.text)
driver.quit()


#identify the Google search text box and enter the value  
#my_element = driver.find_element("name","description")
#print(my_element.text)

#author = driver.find_element(By.CLASS_NAME,"article-details")
#print(author)

#print(author.txt)