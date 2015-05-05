import requests, threading

def f(arg):
    resp = requests.get(arg)
    print arg, resp.ok, len(resp.content)

# f('http://www.google.com')

urls = ['http://www.google.com', 'http://www.yahoo.com']
threads = [threading.Thread(target=f, args=(i,)) for i in urls]
 
 
for t in threads:
    t.start()
for t in threads:
    t.join()


#python threads are restricted
#GIL: interpreter is protected by a lock
#use c extensions rather

#io bound are good
#but no computing distribution


