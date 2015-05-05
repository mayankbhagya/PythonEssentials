#deafult sys.getsizeof
import sys

x = 1
print sys.getsizeof(x)

x = [1, 2, 3]
print sys.getsizeof(x)

x = [1, 2, [3, 4]]
print sys.getsizeof(x)



from memory_profiler import profile
 
def g():
    print len([i for i in range(100000)])
 
def h():
    print len([i for i in xrange(100000)])
 
@profile
def f():
    g()
    h()
 
 
f()
