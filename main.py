import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL_TEMPLATE = 'https://habr.com/ru/all/'
r = requests.get(URL_TEMPLATE)
print(r.status_code)

soup = bs(r.text, "html.parser")

post_titles = []
post_titles.append(soup.find_all('h2', attrs={'data-test-id': 'articleTitle'}))

main_link = 'https://habr.com'
links = []
for item in post_titles:
    for element in item:
        links.append(element.find('a').get('href'))

my_dict = {
    'Дата публикации:': '',
    'Название статьи:': '',
    'Ссылка:': '',
}
for link in links:
    data_link = main_link + link
    r = requests.get(data_link)
    soup = bs(r.text, 'html.parser')

    data_post = soup.find_all('article', class_='tm-article-presenter__content tm-article-presenter__content_narrow')
    for word in KEYWORDS:
        N = +1
        data = soup.find_all(KEYWORDS[N-1])

    if data != None:
        date_of_post = soup.find('time')['title']
        title_of_post = soup.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1')
        my_dict.update({
            'Дата публикации:': date_of_post,
            'Название статьи:': title_of_post.get_text(),
            'Ссылка:': data_link,
        })
        pprint(my_dict)
    else:
        pass

