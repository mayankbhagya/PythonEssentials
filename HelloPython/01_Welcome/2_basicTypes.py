#Dynamically typed
#    one var can have multiple types
#    no formal declaration

x = None
print type(x)

x = True
print type(x)

x = "Forty two"
print type(x)

x = 42
print type(x)

x = 42.42
print type(x)

#container types
x = [1, 2, 'a', 'b']
print type(x)

x = ('a', 'b', 1, 2)
print type(x)

x = {1, 2, 3}
print type(x)

x = {'a':1, 2:'b'}
print type(x)
#array, deque, defaultdict, namedtuples, heapq


