#pdb
def printerFunc():
    print [i for i in range(10000)]
    
def wrapper():
    n = 10
    while(n):
        printerFunc()
        n-=1
        
import pdb
pdb.run('wrapper()')


#c, n, s, r 
#l, w (list, where)
#up, down (stack)
#p, b, tbreak, condition
#commands
