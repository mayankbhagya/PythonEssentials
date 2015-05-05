class A(object):
    v = 2
    
    def __init__(self):
        self.stack = []

    def push(self, o):
        self.stack.append(o)
    
    def pop(self):
        return self.stack.pop()

    @staticmethod
    def staticM():
        print "I am static!" 

    @classmethod
    def classM(cls):
        print "Args:", cls

#dir function lists all instancemethods, attributes available on an object
x = A()
print dir(x)
#__dict__, __class__, __bases__
print x.__dict__

#class variable
# print x.v
# print A.v
# x.v = 15
# print A.v
# print x.v


#dynamic attributes
# x.abc = "def"
# print x.abc
# print x.__dict__

#static methods
# print A.staticM()
#exposed to instances too


#class methods
# A.classM()


#staticmethod and classmethod are decorators. will be discussed later.


#bound and unbound methods
# m1 = A.push
# print type(m1)
# m1(x, 4)
# print x.pop()

# y = A()
# m2 = y.push
# print type(m2)
# m2(7)
# print y.pop()


#__slots__ and __dict__ are two ways in which instance data is stored
#default is __dict__. __slots__ can be declared and is faster
class Account(object):
    __slots__ = ('name', 'balance')

#No new attributes can be added to objects based on slots