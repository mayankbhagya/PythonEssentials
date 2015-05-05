def f():
    print "Hello world"


# print type(f)
# 
# #default return value is None 
# x = f()
# print type(x)


#multiple args
# def g(*args):
#     return args
#     
# print g("this", "will", "print", "whatever", "args", "i", "give")


#keyword args
# def h(**args):
#     return args
#      
# print h(arg1="value1", arg2="value2")


#default values and multiple return values
def i(arg1, arg2=["one"]):
    return arg1, arg2
  
# x, y = i(1)
# print x
# print y

f = i


#using mutable values such as lists in default values is not advised


#new NS created each time a function is called
#local -> global -> builtins


#closures supported


#global keyword
v = 1
def func():
    global v
    v = 10
    print v
 
print v
func()
print v

#map-reduce support