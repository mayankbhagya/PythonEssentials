#urllib, urllib2

#requests
import requests

resp = requests.get('http://www.google.com', params=None, data=None, headers={}, cookies={}, files=None, timeout=10, verify=False, cert=None)

# requests.post
# requests.options
# requests.patch
# requests.put
# requests.delete

#response apis
print resp.ok
print len(resp.content)

#for i in dir(resp): print i if "__" not in i else ""

#server side framework
#django: http server, mvt

#tastypie, django-rest for REST

#Low level - https://docs.python.org/2/library/socket.html
