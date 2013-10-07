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
    info = json.loads(html)
    for i in range(0, len(info) - 1):
      temp = info[i]
      # repos.append(Repo(temp['name'], watchers=temp['watchers_count']))
      url = url[0:-7] + '/' + temp['full_name']
      print url
      request = urllib.Request(url)
      base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
      request.add_header("Authorization", "Basic %s" % base64string)  
      response = urllib.urlopen(url)
      print response[0]['name']
      # print repos[-1].get_name()
      # print repos[-1].get_watchers()
    url = link[link.find('<')+1:link.find('>')]
__main__()