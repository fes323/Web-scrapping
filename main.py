import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL_TEMPLATE = 'https://habr.com/ru/all/'
r = requests.get(URL_TEMPLATE)
print(r.status_code)

soup = bs(r.text, "html.parser")

new_post = soup.find_all('article', class_='tm-articles-list__item')  # получаем самый первый пост полностью (последний)

post_date = soup.find_all('span', class_='tm-article-snippet__datetime-published')  # дата публикации
article_title = soup.find_all('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')  # заголовок
link = soup.find_all('a', class_='tm-article-snippet__title-link')  # ссылка


habr_link = 'https://habr.com/'  #ссылка на хабр
data_link = ''

#Итоговый словарь
final_parse = {
    'date': '',
    'title': '',
    'link': '',
}

data_link = link.a['href']
final_link = habr_link + data_link

print(post_date.time['datetime'])
print(article_title.a.span.string)
print(final_link)