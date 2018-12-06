import shelve
import warnings
import warnings

import config

warnings.filterwarnings("ignore")


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
        self.active=False
    def __str__(self):
        return  self.name+':  '+str(self.shopid)+':'+str(self.itemid)+':'+str(self.colid)

def decode(text):

    from Crypto.Cipher import DES
    des = DES.new(config.key, DES.MODE_ECB)
    data = des.decrypt(text)
    data = data.decode("utf-8")
    while data[-1]==' ':
        data=data[:-1]
    return data

def encode(text):
    text=text.encode('utf-8')

    while len(text) % 8 != 0:
            text += b' '

    from Crypto.Cipher import DES
    des = DES.new(config.key, DES.MODE_ECB)

    encrypted_text = des.encrypt(text)
    return encrypted_text

def getdata():
    data = {}
    d = shelve.open('dbotdata')

    data['email']=decode( d['email'])

    data['fio']= decode(d['fio'])
    data['tel']= decode(d['tel'])
    data['adress']= decode(d['adress'])
    data['sity']= decode(d['sity'])
    data['postcode']= decode(d['postcode'])
    data['card_type']= decode(d['card_type'])
    data['country']= decode(d['country'])
    data['card_nom']=decode(d['card_nom'])
    data['card_cvc']=decode(d['card_cvc'])
    data['card_month']= decode(d['card_month'])
    data['card_year']= decode(d['card_year'])

    d.close()
    return data

def setdata(data):

    d = shelve.open('dbotdata')

    d['email']=encode( data['email'])
    d['fio']=encode( data['fio'])
    d['tel'] = encode(data['tel'])
    d['adress']=encode( data['adress'])
    d['sity']=encode( data['sity'])
    d['postcode']=encode( data['postcode'])
    d['card_type']=encode( data['card_type'])
    d['country']=encode( data['country'])
    d['card_nom']=encode( data['card_nom'])
    d['card_type']=encode( data['card_type'])
    d['card_cvc']=encode( data['card_cvc'])
    d['card_year']=encode( data['card_year'])
    d['card_month']=encode( data['card_month'])

    d.close()





