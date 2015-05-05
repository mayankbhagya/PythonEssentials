#yield to take input
def f():
    z = []
    print "starting"
    for i in range(3):
        print "before yield"
        v = yield
        print "after yield"
        z.append(v)
    print "end of loop", z

try:
    x = f()
    x.next()
    print "Hello"
    x.send(10)
    x.send(11)
    x.send(12)
except StopIteration:
    print "Finished"
    
        