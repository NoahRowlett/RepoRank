import urllib2 as urllib
import json
import base64
import getpass as g
from repoClass import *

def __main__(): 
  # url = 'https://api.github.com/repositories'
  url = 'https://api.github.com/rate_limit'
  username = raw_input("Enter username: ")
  password = g.getpass()
  passman = urllib.HTTPPasswordMgrWithDefaultRealm()
  repos = []
  # for page in range(1, 11):
    # print url
    # # request = urllib.Request(url)
    # # base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    # # request.add_header("Authorization", "Basic %s" % base64string)  
  passman.add_password(None, url, username, password)
  reponse = urllib.urlopen(url)
  print json.loads(reponse.read())['rate']['limit']
    # response = urllib.urlopen(url)
    # html = response.read()
    # headers = response.info()
    # link = headers['Link']
    # info = json.loads(html)
    # tempurl = url
    # for i in range(0, len(info) - 1):
      # temp = info[i]
      # # repos.append(Repo(temp['name'], watchers=temp['watchers_count']))
      # url = tempurl[0:-7] + '/' + temp['full_name']
      # # request = urllib.Request(url)
      # # base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
      # # request.add_header("Authorization", "Basic %s" % base64string)  
      # passman.add_password(None, url, username, password)
      # response = urllib.urlopen(url)
      # stuff = json.loads(response.read())
      # print stuff['name']
      # # print repos[-1].get_name()
      # # print repos[-1].get_watchers()
    # url = link[link.find('<')+1:link.find('>')]

__main__()