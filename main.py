import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs


KEYWORDS = ['Дизайн', 'Фото', 'Web', 'Python']

URL_TEMPLATE = 'https://habr.com/ru/all/'
r = requests.get(URL_TEMPLATE)
print(r.status_code)

soup = bs(r.text, "html.parser")

post_titles = []
post_titles.append(soup.find_all('h2', attrs={'data-test-id': 'articleTitle'}))

main_link = 'https://habr.com'
data_links = []
for item in post_titles:
    for element in item:
        data_links.append(main_link + element.find('a').get('href'))


my_dict = {
    'Дата публикации:': '',
    'Название статьи:': '',
    'Ссылка:': '',
}

parse_dict = {
    'Дата публикации:': '',
    'Название статьи:': '',
    'Ссылка:': '',
}

result_pars = []
data_parse = []
links_KEYWORD = []


for link in data_links:

    data_link = link
    r = requests.get(link)
    soup = bs(r.text, 'html.parser')

    date_of_post = soup.find('time')['title']
    title_of_post = soup.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1')
    my_dict = ({
        'Дата публикации:': date_of_post,
        'Название статьи:': title_of_post.get_text(),
        'Ссылка:': data_link,
    })
    data_parse.append(my_dict)

    post_display = soup.find('article', class_='tm-article-presenter__content tm-article-presenter__content_narrow')
    #match_chek = post_display.find_all(text=KEYWORDS[0])
    tag_of_post = post_display.find('div', attrs={'data-test-id': 'articleHubsList'}).get_text()

    for word in KEYWORDS:

        if word in tag_of_post:
            links_KEYWORD.append(data_link)
            parse_dict = ({
                'Дата публикации:': date_of_post,
                'Название статьи:': title_of_post.get_text(),
                'Ссылка:': data_link,
            })
            result_pars.append(parse_dict)

        text_in_post = []
        for element in post_display:
            text_in_post.append(element.find('p'))
            if word in text_in_post:
                links_KEYWORD.append(data_link)
                parse_dict = ({
                    'Дата публикации:': date_of_post,
                    'Название статьи:': title_of_post.get_text(),
                    'Ссылка:': data_link,
                })
                result_pars.append(parse_dict)




pprint(result_pars)

#pprint(data_parse)




