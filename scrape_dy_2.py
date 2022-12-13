import requests
from bs4 import BeautifulSoup
import re
import json
response = requests.get('https://quotes.toscrape.com/js')
soup = BeautifulSoup(response.text,"lxml")
script_tag = soup.find("script",src=None)
print(script_tag)
pattern = "var data =(.+?);\n"
raw_data = re.findall(pattern,script_tag.string,re.S)
if raw_data:
    data = json.loads(raw_data[0])

print(data)