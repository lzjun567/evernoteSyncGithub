#!/usr/bin/python 
from evernote.api.client import EvernoteClient
dev_token="S=s1:U=62321:E=144d9da1920:C=13d8228ed21:P=1cd:A=en-devtoken:V=2:H=d776ab5512f916a3a03ebafe38cdb242"
client = EvernoteClient(token=dev_token)
userStore=client.get_user_store()
user=userStore.getUser()
print user.username



