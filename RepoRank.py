import urllib2 as urllib
import json
import base64
import requests
import getpass as g
from repoClass import *

def __main__(): 
  url = 'https://api.github.com/repositories'
  username = raw_input("Enter username: ")
  password = g.getpass()
  repos = []
  for page in range(1, 11):
    print url
    r = requests.get(url, auth=(username,password))
    link = r.headers['Link']
    info = json.loads(r.content)
    tempurl = url
    for i in range(0, len(info) - 1):
      temp = info[i]
      # repos.append(Repo(temp['name'], watchers=temp['watchers_count']))
      url = tempurl[0:-7] + '/' + temp['full_name']
      r = requests.get(url, auth=(username,password))
      stuff = json.loads(r.content)
      print stuff['name']
      # print repos[-1].get_name()
      # print repos[-1].get_watchers()
    url = link[link.find('<')+1:link.find('>')]

__main__()