from bs4 import BeautifulSoup
import requests


# step 1 - get source code

source = requests.get("https://coreyms.com/").text

# step 2 - create soup var containing source variable

soup = BeautifulSoup(source, 'lxml')

# step 3 - use print statement to confirm file gotten

# print(soup.prettify())

# step 4 - set article variable find first occurrence of article

article = soup.find('article')

print(article.prettify())