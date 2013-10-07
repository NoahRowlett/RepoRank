import urllib2 as urllib
import json
import base64
import getpass as g
from repoClass import *

def __main__(): 
  url = 'https://api.github.com/repositories'
  
  username = raw_input("Enter username: ")
  password = g.getpass()
  repos = []
  for page in range(1, 11):
    request = urllib.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)  
    response = urllib.urlopen(url)
    html = response.read()
    headers = response.info()
    link = headers['Link']
    url = link[link.find('<')+1:link.find('>')]
    info = json.loads(html)
    for i in range(0, len(info) - 1):
      temp = info[-1]
      print temp
      repos.append(Repo(temp['name'], watchers=temp['watchers_count']))
      print repos[-1].get_name()
      print repos[-1].get_watchers()
      
__main__()