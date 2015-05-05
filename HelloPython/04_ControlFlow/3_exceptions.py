
try:
    print "Hello"
    raise Exception("")
    print "World"
except:
    print "Exception!"
else:
    print "No exception here!"
finally:
    print "I will always run."
     
    