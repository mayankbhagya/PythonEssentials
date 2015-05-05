#imports and modules
#constructor
#member variables
#methods with __xx__
#exception handling

#classes from object

import random

class RandomNumber(object):
    v = 5
    
    def __init__(self):
        self.n = round(random.random() * 10)
        print "Object created"

    def getEven(self):
        if int(self.n) % 2 == 0:
            return self.n
        else:
            raise Exception("Not Even")

############################################


r = RandomNumber()
print r.v
print RandomNumber.v
RandomNumber.v = 15
print RandomNumber.v
print r.v

# try:
#     print r.getEven()
# except Exception as e:
#     print str(e)

#loop this 5 times
#for i in [0, 1, 2, 3, 4]:
#    print i
