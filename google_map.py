from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time


options = ChromeOptions()
options.BinaryLocation = "/usr/bin/chromium-browser"
options.headless  = True
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
url = "https://www.google.com/maps/place/Araniko+College+of+Business+and+Technology/@27.670718,85.3034212,17z/data=!3m1!4b1!4m5!3m4!1s0x39eb198cc5d66fdb:0xd7fdccc44f930d41!8m2!3d27.670718!4d85.3056152"


