import eyed3
import os
import mp3Main
import pathlib
import errno




rootdir = mp3Main.set_rootdir()


#artist folder creation and garbage collection.

for root, dirs, files in os.walk(rootdir):
    for name in files:

        try:
            tempFile = eyed3.load((os.path.join(root, name)))
            songArtist = tempFile.tag.artist
            source = os.path.join(root, name)
            dest = os.path.join(rootdir, (tempFile.tag.artist), name)



           # pathlib.Path(rootdir, songArtist).mkdir(parents=True, exist_ok=True)

            #tempPath = pathlib.Path("/home/zach/Music/Jim's iPod/%" % tempFile.tag.artist).mkdir( exist_ok=True)

            os.rename(source, dest)

            print(os.path.join(root, name))
        except:
            #creating the garbage name outside of the music directory stops it from being scanned by the rest of the program
            #create code to set name outside of user selected root dir

            source = os.path.join(root, name)
            dest = os.path.join(rootdir,"00Garbage_Collection", name)
            pathlib.Path(rootdir, "00Garbage_Collection").mkdir(parents=True, exist_ok=True)
            os.rename(source, dest)

            print(os.path.basename(name))
