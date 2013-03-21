#!/usr/bin/python 
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
dev_token="S=s1:U=62321:E=144d9da1920:C=13d8228ed21:P=1cd:A=en-devtoken:V=2:H=d776ab5512f916a3a03ebafe38cdb242"
client = EvernoteClient(token=dev_token,sandbox=True)
userStore=client.get_user_store()
user=userStore.getUser()
print user.username

def noteStoreTest():
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks()

    for n in notebooks:
        print n.name

def createNoteTest():
    noteStore = client.get_note_store()
    note = Types.Note()
    note.title = "just a test note"
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>Hello, world!</en-note>'
    note = noteStore.createNote(note)

def createNoteBookTest():
    noteStore = client.get_note_store()
    notebook = Types.Notebook()
    notebook.name = "my noetbook"
    notebook = noteStore.createNotebook(notebook)
    print notebook.guid

if __name__=="__main__":
    #createNoteTest()
    #noteStoreTest()
    createNoteBookTest()

