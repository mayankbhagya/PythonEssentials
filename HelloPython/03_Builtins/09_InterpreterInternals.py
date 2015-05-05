#many objects used by interpreter are exposed to user
#traceback, code, frame, generators, slices
from test.test_descrtut import defaultdict


#__new__(), __del__()
#del might not be called all the time


#operators are also methods!
class A(object):
    def __init__(self):
        import random
        self.n = random.random() * 10
        
    def __add__(self, other):
        tmp = A()
        tmp.n = self.n + other.n
        return tmp
    
# x = A()
# y = A()
# print x.n, y.n
# print (x + y).n




#() is also an operator!
#object's __call__ method is invoked when () are encountered
class B(object):
    def __call__(self, *args):
        print "Args:", args

# x = B()
# x(1, 2, "hello")


#dictionary access is also via methods
#slicing is also via methods

#instances have a special attribute called __class__ that refers to the type object