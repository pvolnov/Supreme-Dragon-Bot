from multiprocessing import Process



import shelve
d = shelve.open('dbotdata')
d['name']='Petr'
d.close()

d = shelve.open('dbotdata')
print(d['name'])
d.close()