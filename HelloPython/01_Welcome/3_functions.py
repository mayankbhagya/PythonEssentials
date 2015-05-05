#indentation and scope
#natural language
#readability

def sampleFunction(firstName, lastName):
    
    if not firstName or not lastName:
        raise Exception("First name cannot be empty")
    
    print firstName, lastName

############################################


sampleFunction("John", None)

#https://www.python.org/dev/peps/
