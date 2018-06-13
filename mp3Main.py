import eyed3
import os
from tkinter import *
from tkinter import filedialog

#select root directory with GUI tKinter
def set_rootdir():
    root = Tk()
    root.filename = filedialog.askdirectory(initialdir = "/home/zach/Music/")
    rootdir = (root.filename)
    root.destroy()
    return rootdir

#rename files on the song name in mp3 tag
def mp3_rename():
    rootdir = set_rootdir()
    for root, dirs, files in os.walk(rootdir):
        for name in files:
            try:
                tempFile = eyed3.load((os.path.join(root, name)))
                #print(os.path.join(root, name))
                newName = tempFile.tag.title +".mp3"
                #print(newName)
                source = os.path.join(root, name)
                dest = os.path.join(root,newName)
                os.rename(source, dest)
            except:
                print("Invalid mp3 header / eyeD3 goofed")
             #print(os.getcwd())

mp3_rename()
