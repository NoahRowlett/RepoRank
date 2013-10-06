import urllib2 as urllib
import json
from repo_class import *

def __main__(): 
  for page in range(1, 11):
    url = 'https://api.github.com/repositories?page=' + str(page)
    print url
    repos = []
    response = urllib.urlopen(url)
    html = response.read()
    info = json.loads(html)
    for i in range(0, len(info) - 1):
      temp = info[i]
      repos.append(Repo(temp['name']))
      print repos[i].get_name()

__main__()

#test change