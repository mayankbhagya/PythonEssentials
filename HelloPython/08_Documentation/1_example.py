

class MathOperations(object):
    '''Provides methods for basic mathematics'''
    
    @staticmethod
    def add(a, b):
        '''Method that adds two given numbers'''
        return a + b

    @staticmethod
    def subtract(a, b):
        '''Method that subtracts two given numbers'''
        return a - b

#help method
#help(MathOperations)


#__doc__ method
print MathOperations.__doc__
print MathOperations.add.__doc__
print MathOperations.subtract.__doc__