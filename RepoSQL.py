import MySQLdb
from repoClass import *
from dbAccess import *

def importToDB(repoList):
    for item in repoList:
        item.save()

