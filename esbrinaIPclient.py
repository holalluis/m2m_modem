import urllib2
response = urllib2.urlopen('http://icanhazip.com/')
html = response.read()
print html
