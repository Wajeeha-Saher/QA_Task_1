from utilities.resources import ApiResources
from utilities.configurations import getConfig

def CreateUser():
    body = {"name": "morpheus","job": "leader"}
    return body

def UpdateUser():
    body = {"name": "morpheus","job": "zion resident"}
    return body

def RegisterSuccessfulUser():
    body = {"email": "eve.holt@reqres.in","password": "pistol"}
    return body

def RegisterUnSuccessfulUser():
    body = {"email": "sydney@fife"}
    return body

def LoginSuccessful():
    body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    return body

def LoginUnSuccessful():
    body = {"email": "peter@klaven"}
    return body