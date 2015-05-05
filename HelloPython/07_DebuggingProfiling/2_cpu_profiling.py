import time
time.time()
time.clock()


def printerFunc():
    print [i for i in range(10000)]
    
def wrapper():
    n = 10
    while(n):
        printerFunc()
        n-=1


#timeit
# import timeit
# print timeit.timeit('x={}')
# print timeit.timeit('x=dict()')

# t = timeit.timeit('wrapper()', 'from __main__ import wrapper', number=10)
# print "Time taken:", t

   
# import cProfile
# cProfile.run('wrapper()', sort=2)


