#type is also object
o = {'a':1}
t =  type(o)
print t
print type(t)

#types always point to same obj
# print id(type({'a':1})) == id(type({'b':2}))

#is operator: checks id
# print type({'a':1}) is type({'b':2})

# print type({'a':1}) is type(dict())


#is not safe for type checking
#use 'isinstance'
x = 2
print isinstance(x, int)

#avoid type check on runtime. :(

