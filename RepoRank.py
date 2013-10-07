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
  for page in range(1, 2):
    print url
    r = requests.get(url, auth=(username,password))
    link = r.headers['Link']
    info = json.loads(r.content)
    tempurl = url
    for i in range(0, len(info) - 1):
      temp = info[i]
      # tempurl[0:-7] means taking 'https://api.github.com/repositories' and making it 'https://api.github.com/repos'
      url = tempurl[0:-7] + '/' + temp['full_name']
      r = requests.get(url, auth=(username,password))
      stuff = json.loads(r.content)
      repos.append(Repo(stuff['name'], watchers=stuff['watchers_count'], issues=stuff['open_issues_count']))
      print repos[-1].get_name() + " " + str(repos[-1].get_watchers()) + " " + str(repos[-1].get_issues())
    url = link[link.find('<')+1:link.find('>')]

__main__()