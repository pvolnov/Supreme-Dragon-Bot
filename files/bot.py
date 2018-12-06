import re
import time
import warnings
from multiprocessing import Process, Queue
import config
warnings.filterwarnings("ignore")

import urllib3
from bs4 import BeautifulSoup


def decode(text):

    from Crypto.Cipher import DES
    des = DES.new(config.key, DES.MODE_ECB)
    data = des.decrypt(text)
    data = data.decode("utf-8")
    while data[-1] == ' ':
        data = data[:-1]
    return data

def encode(text):
    text=text.encode('utf-8')

    while len(text) % 8 != 0:
            text += b' '

    from Crypto.Cipher import DES
    des = DES.new(config.key, DES.MODE_ECB)

    encrypted_text = des.encrypt(text)
    return encrypted_text


if __name__ == '__main__':

    print(decode(encode('Привет, бро')))

