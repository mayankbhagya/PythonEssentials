import datetime
 
def timedLog(func):
    def tmp(*args, **kwargs):
        print(datetime.datetime.now()),
        func(*args, **kwargs)
    return tmp
 
 
@timedLog
def printLog(msg):
    print msg

printLog("file generated")



