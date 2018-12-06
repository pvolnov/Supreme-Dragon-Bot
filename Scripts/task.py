import datetime
import random
import re
import time
import warnings
from multiprocessing import Process, Queue
import sdbfuncs

import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config
import SBDdata

warnings.filterwarnings("ignore")

class Item():
    name = ''
    def __init__(self, name , color, size,category):
        self.name=name
        self.color=color
        self.category = category
        self.size=size
        self.sizeid=''
        self.shopid = ''
        self.itemid=''
        self.colid=''
        self.active=False
    def __str__(self):
        return  self.name+':  '+str(self.shopid)+':'+str(self.itemid)+':'+str(self.colid)


def findItems(item,q):
    #Найти товар на странице
    http = urllib3.PoolManager()

    ad=False
    r = http.request('GET', 'https://www.supremenewyork.com/shop/all/'+item.category)
    d = r.data
    soup = BeautifulSoup(d)
    brke=False

    for link in soup.find_all('a'):
        if(brke):
            break

        if (sdbfuncs.iseacval (link.contents[0], item.name )):

            for l in soup.find_all('a'):
                if l.get('href') == link.get('href') and (str(l.contents[0]).lower() == str(item.color).lower() or item.color=='any'):

                    page_url = l.get('href')
                    http = urllib3.PoolManager()
                    r = http.request('GET',
                                     "http://www.supremenewyork.com/" + page_url)
                    d = r.data
                    print(d)
                    parsed_html = BeautifulSoup(d)

                    at = parsed_html.body.find('select', attrs={'id': 'size'})
                    at = at.find_all('option')

                    for sz in at:
                        if (sz.text == item.size or item.size == 'any'):
                            item.sizeid=sz['value']
                            break

                    at = str(parsed_html.body.find('input', attrs={'id': 'style'}))
                    a = str(re.search(r'\d{4,6}', at).group())

                    ct = str(parsed_html.body.find('form', attrs={'id': 'cart-addf'}))
                    c = str(re.search(r'\d{5,6}', ct).group())
                    item.shopid = c
                    item.colid = a
                    if(a!=''):
                        item.active=True

                    print('Найден: ',item.name)
                    ad=True

                    brke=True
                    break

    if (ad==False) :
        print('Товар не найден:',item.name)

    q.put(item)


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
    #print('Ходят легенды, если потренеровать капчу заранее, шанс взять выше:')
    #driver.get('https://patrickhlauke.github.io/recaptcha/')

    print('Ожидание дропа.. ничего не трогай!')
    #sdbfuncs.waittime()
    url = "https://www.supremenewyork.com/shop/all/new"
    driver.get(url)
    #sdbfuncs.waitdrop()

    ti=time.clock()
    print("Бот запущен",datetime.datetime.now())


    q = Queue()
    proc =[]
    for item in items:
        proc.append(Process(target=findItems, args=(item, q)))


    for p in proc:#запускаем все
        p.start()

    for p in proc:#ждем окончание всех процессов
        p.join()

    print('all items detected')



    for i in range(len(items)):
        items[i]=q.get()
    #print('Добавлено в список задач', q.get())


    for i in range(len(items)):
        if(items[i].active==False):
            print('Товар не найден или sold out: ',items[i].name)
            continue

        cd = JScode.format(shopid=items[i].shopid, styleid=items[i].colid, sizeid=items[i].sizeid)
        driver.execute_script(cd)
        print("Товар добавлен в корзину", items[i], time.clock()-ti)
        if(i+1!=len(items)):
            time.sleep(0.3)


    JsBuy=JsBuy.format(name=data['fio'],email=data['email'],tel=data['tel']
                       ,adress=data['adress'],sity=data['sity'],cardnom=data['card_nom']
                       ,zip=data['postcode'],cvv=data['card_cvc'],card_type=data['card_type'],
                       card_month=data['card_month'],card_year=data['card_year'])
    driver.execute_script(JsBuy)
    print("Куплено", time.clock()-ti)
    time.sleep(5)
    driver.save_screenshot('scrin.png')
    time.sleep(360)

def main(data, items):
    bot(data, items)


def run():
    import SBDdata
    try:
        data=SBDdata.getdata()
    except :
        sdbfuncs.setdata()
        data = SBDdata.getdata()

    items = []

    name = 'Box Logo Crewneck Sweatshirt'
    print('name: ',name)
    size=input('Item size: ')
    color = input('Item color: ')

    wt=random.uniform(0.9, 1.8)
    while True:
        #name=input('Item name: ')

        if(name)=='-':
            break
        #size=input('Item size: ')
        #color=input('Item color: ')
        category=input('Item category [low letter]: ')
        if (category) == '-':
            break

        itm = Item(name, color, size, category)
        items.append(itm)
        wt += random.uniform(0.2, 0.5)

    print("--------------------------")
    print("Товар добавлен, рассчетное время работы бота",wt,'c')
    main(data,items)

def testrun():
    import SBDdata
    try:
        data = SBDdata.getdata()
    except:
        sdbfuncs.setdata()
        data = SBDdata.getdata()

    items = []

    name = 'Diamond Faux Fur Jacket'
    color="any"
    size="any"
    category="jackets"
    print('name: ', name)

    wt = random.uniform(0.9, 1.8)

    itm = Item(name, color, size, category)
    items.append(itm)
    wt += random.uniform(0.2, 0.5)

    print("--------------------------")
    print("Товар добавлен, рассчетное время работы бота", wt, 'c')
    main(data, items)

if __name__ == "__main__":
    print(config.avaimg)
    if(sdbfuncs.issetting()==False):
        sdbfuncs.setsetting()
    #boxlogorun()
    testrun()
    #run()