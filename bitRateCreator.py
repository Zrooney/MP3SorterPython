import eyed3
import eyed3.mp3
from eyed3 import mp3
import os
import mp3Main
#from mp3Main import set_rootdir
import pathlib
import errno


rootdir = mp3Main.set_rootdir()


#artist folder creation and garbage collection.

for root, dirs, files in os.walk(rootdir):
    for name in files:
        try:
            audioFile = eyed3.load(os.path.join(root, name))
            songArtist = audioFile.tag.artist
            tag = mp3.Mp3AudioFile(os.path.join(root, name))
            x = (tag.info.bit_rate)
            bitRate = str(x[1])

            # search string for  numbers, /xxx/ if it comes with 1 then don't proceed with code
            #if bitRate.__len__() <= 2:
            #    bitRate = bitRate.zfill(3)

            source = os.path.join(root, name)
            dest = os.path.join(rootdir, songArtist, bitRate, name)

            pathlib.Path(rootdir, bitRate).mkdir(parents=True, exist_ok=True)
            print(dest)
            os.rename(source, dest)
        except:
            #creating the garbage root outside of the music directory stops it from being scanned by the rest of the program
            #create code to set root outside of user selected root dir
            print("on no")
