x = [1, 2, 3, [4, 5]]
y = []
y.append(x)
x.append(y)


#reference
# y = x
# x.append(6)


#shallow copy
# y = list(x)
# x.append(6)


#problem with shallow copy
# y = list(x)
# x[3].append(6)


#deepcopy
# import copy
# y = copy.deepcopy(x)
# x[3].append(6)

import copy
z = copy.deepcopy(y)
print z


print x
print y
