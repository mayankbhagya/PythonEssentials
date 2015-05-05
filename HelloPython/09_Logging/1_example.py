#logger concepts: logger, handler, filter, formatter
#default: root logger
#level: DEBUG, INFO, WARNING, ERROR, CRITICAL

import logging, sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)


class Stack(object):
    def __init__(self):
        #init logger
        self.logger = logging.getLogger('myLogger')
        #configure logger
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        #init stack
        self.s = []
        self.logger.info("created stack")
        self.logger.debug(self.s)
    

    def push(self, obj):
        self.s.append(obj)
        self.logger.info("pushed")
        self.logger.debug(self.s)
        
    
    def pop(self):
        tmp = self.s.pop()
        self.logger.info("popped")
        self.logger.debug(self.s)
        return tmp



x = Stack()
x.push(10)
x.push(20)
print x.pop(), x.pop()