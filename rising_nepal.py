from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://risingnepaldaily.com/')
bs = BeautifulSoup(html.read(),'html.parser')

output = bs.find(class_="item-title px-5")
print('Headline')
print(output.a.text)

print('\n................\n')
print('Link for the headline')
link_for_full_article = output.a.get('href')
print(link_for_full_article)


print('\n................\n')
print('Visiting full article page')
full_article_html = urlopen(link_for_full_article)
bs_full_article = BeautifulSoup(full_article_html.read(),'html.parser')
output_full_article = bs_full_article.find_all(class_="blog-details")

output_full_article = output_full_article[3]


paragraphs = output_full_article.find_all("p")
print(len(paragraphs))
for paragraph in paragraphs:
    print(paragraph.text)
    print('\n...............\n')



#for header in headers:
 #   print(header)