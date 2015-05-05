#classes that create classes
#by default, for new style objects, that meta class is the class 'type'


class MyMetaClass(type):
    def __init__(self, name, bases, classDict):
        if not 'myMethod' in classDict: raise Exception("myMethod not implemented")


class A(object):
    __metaclass__ = MyMetaClass

    def __init__(self):
        print "Created instance"

    def myMethod(self):
        print "my method!"
    

    

x = A()