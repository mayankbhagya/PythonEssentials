x = []
x.append(1)
x.extend([2, 3, 4])

#methods in x
# x.

#operators: also implemented via methods
print x + x


#iterating
# for i in x: 
#     print i

#range
# print range(10)
# for i in range(10): print i

#comprehensions
y = []
for i in x: 
    y.append(i*i)
print y

print [i*i for i in x]

# print [i*i for i in x]
