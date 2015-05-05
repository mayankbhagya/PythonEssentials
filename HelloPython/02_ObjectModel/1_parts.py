#4 parts
#name, id, type, value

x = {'a':1}

#memory location
print "id:", id(x)
print type(id(x))

#type is also called class
print "type:", type(x)


print "value:", x

class A(object):
    pass

y = A()
print type(y)

z = A()
print type(z)