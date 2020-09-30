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

# print(article.prettify())

# step 5 - find article header
# headline = article.h2.a.text
# print(headline)

# step 6 - find summary text

# summary = article.find('div', class_='entry-content').p.text

# print(summary)

# step 7 - find video id link embedded in i-frame

vid_src = article.find('iframe', class_ ='youtube-player')['src']
# print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

# print(vid_id)

# step 8 create custom youtube link

yt_link = f'https://www.youtube.com/watch?v={vid_id}'
print(yt_link)
        
