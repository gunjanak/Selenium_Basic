#This does not work

# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
#options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)

driver.get("https://chromium.googlesource.com/chromium/src/+/master/chrome/test/data/dino/index.html")

# Start the game by pressing the space bar
driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

# Play the game using a simple algorithm
while True:
  # Check if the game is over
  if driver.execute_script("return Runner.instance_.crashed"):
    # Restart the game by pressing the space bar
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)
    continue

  # Move the dino by pressing the up arrow key
  driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
