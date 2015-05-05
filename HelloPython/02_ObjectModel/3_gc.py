class A(object):
    pass

#all objs are ref counted
x = A()
import sys
print sys.getrefcount(x)


#increases on assignment or adding to collection
y = x
print sys.getrefcount(x)

#decreases on del statement, when out of scope
del y
print sys.getrefcount(x)

#weakref
#import weakref
#print sys.getrefcount(x)
#y = weakref.ref(x)
#print sys.getrefcount(x)

#cyclic references cause trouble to gc
#removed in a while
#a = [1, 2, 3]
#b = {'a': a}
#a.append(b)
#print a

