from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
import requests


#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = ChromeOptions()
options.BinaryLocation = "/usr/bin/chromium-browser"
options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)


path = "https://kathmandupost.com"

driver.get(path)
time.sleep(5)


soup = BeautifulSoup(driver.page_source,'lxml')

print('Headline Title')
print(soup.h2.text)

print('Headline summary')
output = soup.find(class_="1")
print(output.p.text)


print('Link page for this headline')

link_for_main_article = output.a.get('href')
link_for_main_article = path+link_for_main_article
print(link_for_main_article)

print('\n\n.........................\n\n')
print('Going to details of headline')
driver.get(link_for_main_article)
soup = BeautifulSoup(driver.page_source,'lxml')

output = soup.find(class_='story-section')
paragraphs = output.find_all("p")
print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text)
    print('\n...............\n')

driver.quit()

