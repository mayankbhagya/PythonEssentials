#yield statement

def f():
    for i in range(10):
        print "starting"
        yield i*i
        
        print "in loop"
    print "end of loop"
    
x = f()
print x
# print x.next()
# print x.next()
# print x.next()
# x.close()

for i in x: print i

