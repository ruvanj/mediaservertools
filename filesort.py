#!/usr/bin/env python
import os, shutil, logging

#TODO add loggging
#logging.basicConfig(filename='filesort.log')

audio_tags = [".mp3",".flac"]
video_tags = [".mkv",".mp4"] # unused

audio_dir = os.path.expanduser('~/Music/')
video_dir = os.path.expanduser('~/Videos/')
root = os.path.expanduser('~/misc')
preconditions = [audio_dir,video_dir]
def isMusic(fn):
    for tag in audio_tags:
        if(fn.endswith(tag)):
            return True
    return False

def moveTo(fn_path, dest):
    try:
        shutil.move(fn_path,dest)
    except shutil.Error as e:
        #Maybe do dif of folders for more advanced add-only copy
        print(e)

def containsMusic(fn_path):
    for root, dirs, files in os.walk(fn_path):
        for name in files:
            if isMusic(name):
                return True
    return False

if __name__ == "__main__":
    for condition in preconditions:
        if not os.path.exists(condition):
            os.makedirs(condition)

    for fn in os.listdir(root):
        fn_path = os.path.join(root,fn)
        if fn.startswith('.'):
            continue
        if os.path.isfile(fn_path):
            if isMusic(fn):
                moveTo(fn_path,audio_dir)
            else:
                moveTo(fn_path,video_dir)
        else:
            if containsMusic(fn_path):
                moveTo(fn_path,audio_dir)
            else:
                moveTo(fn_path,video_dir)
