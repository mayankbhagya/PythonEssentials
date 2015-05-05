#everything is an object

x = 'Single quoted string: {0}'
y = "Double quoted string"
z = '''Triple quoted string''' #can be multiline


#indices start at 0
# print x[0]
# 
# print x[3]
# print x[-3]

# print x[3:]
# print x[:3]
# print x[:]
# print x[2:4]

#three kind of strings
print str(x) #simple string, __str__()
print repr(x) #representation of value so that obj can be reconstructed, __repr__()
print x.format('hello') #formatted string, __format__()
    
