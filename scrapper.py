import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def settings(url_):
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    response = requests.get(url_, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup


def news_scr():
    soup = settings('https://kitis.ru/press-center/news/')
    news_dict = {}

    news_block = soup.find_all('p', class_='t-1 mb-2 sf-title t-title с-text-primary l-inherit '
                                           'l-hover-primary l-hover-underline-none transition')
    for block in news_block:
        text = block.get_text(strip=True)
        link = 'https://kitis.ru' + block.a['href']

        news_dict[link] = text

    return news_dict


def announce():
    soup = settings('https://kitis.ru/press-center/announce/')
    announce_dict = {}

    news_block = soup.find_all('p', class_='t-1 sf-title t-title с-text-primary l-inherit l-hover-primary '
                                           'l-hover-underline-none transition')
    for block in news_block:
        text = block.get_text(strip=True)
        link = 'https://kitis.ru' + block.a['href']

        announce_dict[link] = text

    return announce_dict


