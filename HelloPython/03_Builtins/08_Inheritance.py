class A(object):
    def __init__(self, *args):
        print "Creating A"


class B(A):
    def __init__(self, name="John"):
        print "Creating B 1"
        A.__init__(self, name)
        print "Creating B 2"

x = B()


#multiple inheritance is supported
