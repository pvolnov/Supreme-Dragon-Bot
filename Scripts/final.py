import datetime
import os
import urllib
from threading import Thread
import  time
import re
import webbrowser

import urllib3
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

from pyvirtualdisplay import Display
import time
from bs4 import BeautifulSoup
import warnings

class Item():
    name = ''
    def __init__(self, name , color, size,category):
        self.name=name
        self.color=color
        self.category = category
        self.size=size
        self.shopid = ''
        self.itemid=''
        self.colid=''
    def __str__(self):
        return  self.name+':'+str(self.shopid)+'-'+str(self.itemid)+' '+str(self.colid)

def search_partial_text(src, dst):
    dst_buf = dst
    result = 0
    for char in src:
        if char in dst_buf:
            dst_buf = dst_buf.replace(char, '', 1)
            result += 1
    r1 = int(result / len(src) * 100)
    r2 = int(result / len(dst) * 100)
    return '{}%'.format(r1 if r1 < r2 else r2)

def findItems(items):
    http = urllib3.PoolManager()


    for i in range(len(items)):

        r = http.request('GET', 'https://www.supremenewyork.com/shop/all/'+items[i].category)
        d = r.data
        soup = BeautifulSoup(d)

        for link in soup.find_all('a'):
            if (link.contents[0] == items[i].name):
                for l in soup.find_all('a'):
                    if l.get('href') == link.get('href') and l.contents[0] == items[i].color:
                        print("Найдена ссылка на товар", l.get('href'), time.clock())
                        page_url = l.get('href')
                        http = urllib3.PoolManager()
                        r = http.request('GET',
                                         "http://www.supremenewyork.com/" + page_url)
                        d = r.data
                        parsed_html = BeautifulSoup(d)

                        # items[i].itemid =
                        at = str(parsed_html.body.find('input', attrs={'id': 'style'}))
                        a = str(re.search(r'\d{4,6}', at).group())
                        # items[i].colid
                        bt = str(parsed_html.body.find('option'))
                        b = str(re.search(r'\d{5}', bt).group())
                        # items[i].shopid
                        ct = str(parsed_html.body.find('form', attrs={'id': 'cart-addf'}))
                        c = str(re.search(r'\d{5,6}', ct).group())
                        items[i].shopid = c
                        items[i].itemid = b
                        items[i].colid = a
                        print(items[i])

    return items

def wait():
    http = urllib3.PoolManager()
    r = http.request('GET',
                     "https://www.supremenewyork.com/shop/new")
    d = r.data
    d1 = d
    while (d == d1):
        r = http.request('GET',
                         "https://www.supremenewyork.com/shop/new")
        d1 = r.data
        time.sleep(2)

def bot(data,items):

    firefox_profile = webdriver.FirefoxProfile()
    # firefox_profile.set_preference('permissions.default.image', 2)
    JsBuy = open('buy.js').read()
    JScode = open('additem.js').read()
    options = Options()
    options.add_argument('test-type')
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_argument("user-data-dir=selenium")
    # options.set_headless(headless=True)

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1050, 650)
    url = "https://www.supremenewyork.com/shop/all/new"
    driver.get(url)
    time.sleep(1)
    wait()

    #
    # f = urllib.request.urlopen(url)
    print("Бот запущен", time.clock())


    items = findItems(items)

    for i in range(len(items)):
        cd = JScode.format(items[i].shopid, items[i].colid, items[i].itemid)
        driver.execute_script(cd)
        print("Товар добавлен в корзину", items[i], time.clock())

    JsBuy=JsBuy.format(name=data['fio'],email=data['email'],tel=data['tel']
                       ,adress=data['adress'],sity=data['sity'],cardnom=data['card_nom']
                       ,zip=data['postcode'],cvv=data['card_cvc'],card_type=data['card_type'],
                       card_month=data['card_month'],card_year=data['card_year'])
    driver.execute_script(JsBuy)
    print("Куплено", time.clock())
    time.sleep(60)

def main(data, items):
    while True:
        if(datetime.datetime.now().hour==13 and datetime.datetime.now().minute==59):

            bot(data, items)
        else:
            time.sleep(15)


if __name__ == "__main__":
    warnings.simplefilter("ignore")

    data={}
    print("""

        ╔═══╗╔╗─╔╗╔═══╗╔═══╗╔═══╗╔═╗╔═╗╔═══╗     ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═╗─╔╗     ╔══╗─╔═══╗╔════╗
        ║╔═╗║║║─║║║╔═╗║║╔═╗║║╔══╝║║╚╝║║║╔══╝     ╚╗╔╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║║║╚╗║║     ║╔╗║─║╔═╗║║╔╗╔╗║
        ║╚══╗║║─║║║╚═╝║║╚═╝║║╚══╗║╔╗╔╗║║╚══╗     ─║║║║║╚═╝║║║─║║║║─╚╝║║─║║║╔╗╚╝║     ║╚╝╚╗║║─║║╚╝║║╚╝
        ╚══╗║║║─║║║╔══╝║╔╗╔╝║╔══╝║║║║║║║╔══╝     ─║║║║║╔╗╔╝║╚═╝║║║╔═╗║║─║║║║╚╗║║     ║╔═╗║║║─║║──║║──
        ║╚═╝║║╚═╝║║║───║║║╚╗║╚══╗║║║║║║║╚══╗     ╔╝╚╝║║║║╚╗║╔═╗║║╚╩═║║╚═╝║║║─║║║     ║╚═╝║║╚═╝║──║║──
        ╚═══╝╚═══╝╚╝───╚╝╚═╝╚═══╝╚╝╚╝╚╝╚═══╝     ╚═══╝╚╝╚═╝╚╝─╚╝╚═══╝╚═══╝╚╝─╚═╝     ╚═══╝╚═══╝──╚╝──


    """)
    '''
░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▀▄▄░░░░░▀▀███▄▄▄░░░░░░░░░░░░░░░░░░░░░░
░░▀▀██▄▄▄▄░░░▀▀▀██▄▄░░░░░░░░░░░░░░░░░░
░░░░░░▀▀▀███▄▄░░░▀▀░▄▄▄▄░░░░░░░░░░░░░░
░░░░░░░░░░▄█████████▀░░▀█░░░░░░░░░░░░░
░░░░░░░░░▀█░░▀███▀░░░░░░▀█▄▄░░░░░░░░░░
░░░░░▄█████░░░░░░░░░░░░░░░▀▀█░░░░░░░░░
░░░░░░██▄░░░▀▀██░░░░░░░░░░░░██░░░░░░░░
░░▄▄█▀▀▀▀░░░░▄░░░░░░░░▀▀██░░▀█▄░░░░░░░
░░▄▄██░░░░░▀▀▀▀░░░░░░░░░░░░░░░▀█▄░░▄░░
░██▀▀▀░░░░░░░▄░░░░░░░██▀▀█▄▄░░░▀████░░
░█▀░░░░░░░░▄▀▀░░░░░░░▀█▄░░▀██▄░░░▀▀█▄░
░█▄░░░░░░░░░░░░░░░░░░░░█▄░░▀▀██▄░░░░██
░░█▄░░░░░░░░░░░░██▀█▄░░▀██░░░░▄██▄░░█▀
░░░█▄░░░░░░░░░▄█▀░░░▀█▄░▀██▄▄░░░▄███▀░
░░░░▀█▄░░░░░░░█▀░░░░░░▀█▄░▀▀█▄░░░░░░░░
░░░░░░▀██▄▄▄░▄█░░░░░░░░░████▀░░░░░░░░░
░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░
    '''
    print("Введите ваши данные. Будте внимательны, "
          "в целях безопасность данные не сохраняются и вы "
          "не сможите их отредактировать")
    a=input('email : ')
    data.setdefault('email',a)
    a = input('fio [Petr Volnov] : ')
    data.setdefault('fio',a)
    a = input('tel [+79151343364] : ')
    data.setdefault('tel',a)
    a = input('adress [festival st., h. 65] : ')
    data.setdefault('adress',a)
    a = input('sity [Moscow] : ')
    data.setdefault('sity',a)
    a = input('postcode [129634] : ')
    data.setdefault('postcode',a)
    a = input('card_type [master, visa] : ')
    data.setdefault('card_type',a)
    a = input('country [RU] : ')
    data.setdefault('country',a)
    a = input('card_nom [1232 .. 8700] : ')
    data.setdefault('card_nom',a)
    a = input('card_cvc [434] : ')
    data.setdefault('card_cvc',a)
    a = input('card_month [01,02 .. 12] : ')
    data.setdefault('card_month',a)
    a = input('card_year [2019 .. 2022] : ')
    data.setdefault('card_year',a)

    items = []
    wt=2.3;
    while True:
        print("--------------------------")
        print("Что бы завершить добавление товаров введите в поле для имени 0")

        name = input('Item full name [Patchwork Shearling B-3 Jacket] : ')
        if name=='0':
            break
        color = input('Item color [White] : ')
        size = input('Item size [Medium] : ')
        category = input('Item category [jackets] : ')
        itm = Item(name, color,size,category)
        items.append(itm)
        wt+=1.5
        print("Товар добавлен, рассчетное время работы бота",wt,'c')

    print("Не закрывайте программу! бот активируется в 13:59")

    main(data,items)