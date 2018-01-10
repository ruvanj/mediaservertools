#!/usr/bin/env python
import os
import shutil


audio_tags = [".mp3",".flac"]
video_tags = [".mkv",".mp4"] # unused

audio_dir = '~/Music/'
video_dir = '~/Videos/'
root = '~/misc/'

def isMusic(fn):
    for tag in audio_tags:
        if(fn.endswith(tag)):
            return True
    return False

def moveTo(fn_path, dest):
    try:
        shutil.move(fn_path,dest)
    except shutil.Error:
        print('Overwriting: ' + fn_path)
        shutil.copy2(fn_path,dest)
        shutil.remove(fn_path,dest)

def containsMusic(fn):
    for root, dirs, files in os.walk(fn):
        for name in files:
            if isMusic(name):
                return True
    return False

if __name__ == "__main__":
    for fn in os.listdir(os.expanduser(root)):
        if fn.startswith('.'):
            continue
        if os.isfile(fn):
            if isMusic(fn):
