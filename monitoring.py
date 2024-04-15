import telebot

import pickle
from pathlib import Path
import datetime
import time
from scrapper import news_scr, announce
from settings import TOKEN


def send_message_news_or_announce(text, link):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(-1002115326292, f'{text}\n{link}')


def monitoring():
    file_path = Path('dict_stock.pickle')
    if file_path.exists():
        with open('dict_stock.pickle', 'rb') as file:
            dict_stock = pickle.load(file)
    else:
        dict_stock = {}

    news_dict = news_scr()
    announce_dict = announce()

    dict_stock_current = {
        'news': news_dict, 'announce': announce_dict,
    }

    with open('dict_stock.pickle', 'wb') as file:
        pickle.dump(dict_stock_current, file)

    for key in dict_stock_current:
        event_list = dict_stock_current[key]
        for link in event_list:
            if key in dict_stock:
                if link not in dict_stock[key]:
                    send_message_news_or_announce(event_list[link], link)
                    time.sleep(5)
            else:
                send_message_news_or_announce(event_list[link], link)
                time.sleep(5)


def wait_until_morning():
    current_time = time.strftime('%X').split(':')[0]
    target_time = '16'

    while current_time != target_time:
        current_time = time.strftime('%X').split(':')[0]
        time.sleep(30)


if __name__ == "__main__":
    while True:
        print(f'''Итерация запущена! {time.strftime('%X')}''')
        wait_until_morning()
        monitoring()
        time.sleep(30)
