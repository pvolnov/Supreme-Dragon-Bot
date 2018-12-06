import datetime
import shelve
import time

import urllib3
import SBDdata


def iseacval(s1, s2):
    s1=str(s1)
    s2=str(s2)

    s1 = s1.lower()
    s2 = s2.lower()
    d = shelve.open('setting')

    s1m = s1.split(' ')
    s2m = s2.split(' ')
    le = 0
    for ss in s1m:
        if (ss in s2m):
            le += 1
    return le / len(s1m) > float(d['accuracy'])

def setsetting():
    d = shelve.open('setting')
    print('Введите настройки бота')
    a=input('accuracy :')
    d['accuracy'] = a
    d.close()

def issetting():
    try:
        d = shelve.open('setting')
        print(d['accuracy'])
        return True
    except :
        return False

def setdata():
    print("Введите ваши данные. Будте внимательны!")
    a = input('email : ')
    data={}
    data.setdefault('email', a)
    a = input('fio [Petr Volnov] : ')
    data.setdefault('fio', a)
    a = input('tel [+79151343364] : ')
    data.setdefault('tel', a)
    a = input('adress [festival st., h. 65] : ')
    data.setdefault('adress', a)
    a = input('sity [Moscow] : ')
    data.setdefault('sity', a)
    a = input('postcode [129634] : ')
    data.setdefault('postcode', a)
    a = input('card_type [master, visa] : ')
    data.setdefault('card_type', a)
    a = input('country [RU] : ')
    data.setdefault('country', a)
    a = input('card_nom [1232 .. 8700] : ')
    data.setdefault('card_nom', a)
    a = input('card_cvc [434] : ')
    data.setdefault('card_cvc', a)
    a = input('card_month [01,02 .. 12] : ')
    data.setdefault('card_month', a)
    a = input('card_year [2019 .. 2022] : ')
    data.setdefault('card_year', a)
    SBDdata.setdata(data)

def waittime():
    while True:
        if(datetime.datetime.now().hour==13 and datetime.datetime.now().minute==59):
            break
        else:
            time.sleep(15)
def waitdrop():
    http = urllib3.PoolManager()
    r = http.request('GET',
                     "https://www.supremenewyork.com/shop/new")
    d = r.data
    d1 = d
    while (d == d1):
        r = http.request('GET',
                         "https://www.supremenewyork.com/shop/new")
        d1 = r.data
        time.sleep(1)
if __name__ == '__main__':
    setdata()