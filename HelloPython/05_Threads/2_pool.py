import requests


def f(arg):
    resp = requests.get(arg)
    print arg, resp.ok, len(resp.content)
    
urls = ['http://www.google.com', 'http://www.yahoo.com']

from concurrent import futures
threadPoolExec = futures.ThreadPoolExecutor(max_workers=1)
threads = [threadPoolExec.submit(f, url) for url in urls]
futures.wait(threads, timeout=10)
threadPoolExec.shutdown()



#Queue
#multiprocessing, IPC: pipes, queues, connections
#sync primitives: Lock, Semaphores, ConditionVariables, Events
