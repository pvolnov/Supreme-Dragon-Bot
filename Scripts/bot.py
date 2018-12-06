import urllib3
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

def iseacval(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    
    s1m=s1.split(' ')
    s2m=s2.split(' ')
    le=0
    for ss in s1m:
        if(ss in s2m):
            le+=1
    return le / len(s1m)


s1='Patchwork Shearling B-3 Jacket'
s2='Supreme Patchwork shearling B-3 Jacket'

print (iseacval(s1,s2) )
