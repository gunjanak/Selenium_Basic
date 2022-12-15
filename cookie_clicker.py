#This script visits google scholar 
#seacrh for articles in cryptography
#then set the custom range from 1900 to 2008

#to use chromium with Selenium we need to install
#sudo apt-get install chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup
import time

#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
#options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
#identify the Google search text box and enter the value  
#my_element = driver.find_element("name","q")
#my_element.send_keys('cryptography')
link = driver.find_element(By.LINK_TEXT,"Got it!")
link.click()
time.sleep(10)


eng_lang = driver.find_element(By.ID,"langSelect-EN")
eng_lang.click()
time.sleep(10)


bigCookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")
#actions = ActionChains(driver)
#actions.click(bigCookie)


#cursor_click = driver.find_element(By.LINK_TEXT,"Cursor")
productPrice0 = driver.find_element(By.ID,"productPrice0")
print(productPrice0.text)

#grandma
productPrice1 = driver.find_element(By.ID,"productPrice1")
print(productPrice1.text)




def farm():
    print("Inside farm price")
    #buying farm
    productPrice2 = driver.find_element(By.ID,"productPrice2")
    productPrice2 = productPrice2.text
    productPrice2 = productPrice2.replace(",", "")
    print(productPrice2)
    return productPrice2

farm_price = farm()
if(farm_price):
    print("Inside if")

    print(farm_price)

productName2 = driver.find_element(By.ID,"productName2")
#print(productName2.text)


soup = BeautifulSoup(driver.page_source,'lxml')



print('Headline summary')
output = soup.find(id="productName2").parent
print(output)
print(type(output))







import time
tic = time.time()
tok = time.time()

while(tok-tic < 300):
    bigCookie.click()
    count = int(cookie_count.text.split(" ")[0])

    farm_price = farm()
    if(farm_price):
        if(count > int(farm_price)):
            print("Buying Farm")
            productPrice2 = driver.find_element(By.ID,"productPrice2")
            actions4 = ActionChains(driver)
            actions4.move_to_element(productPrice2)
            actions4.click(productPrice2)
            actions4.perform()



    if(count > int(productPrice1.text)):
        print("Buying Grandma")
        actions3 = ActionChains(driver)
        actions3.move_to_element(productPrice1)
        actions3.click(productPrice1)
        actions3.perform()

    elif(count > int(productPrice0.text)):
        print('Buying cursor')
        actions2 = ActionChains(driver)
        actions2.move_to_element(productPrice0 )
        actions2.click(productPrice0 )
        actions2.perform()

    tok = time.time()







    


print(cookie_count.text)
time.sleep(10)

driver.quit()
