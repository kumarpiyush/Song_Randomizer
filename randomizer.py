#!/usr/bin/python


#  USAGE : python randomizer.py <songs_directory_name>. E.g., $ python randomizer.py MySongs
#
#  Script to shuffle songs for those mp3 players that just play songs sequentially alphabetically.
#  This inserts random permutation of [1..# of songs] before the file names, so player will play in that order.
#  This script is reusable, ie, can rerun on earlier shuffled songs. It will not re-prepend a number before already processed songs, they are treated separately
#  The script would recursively search for mp3 files in the given directory song_dir, and all processed files will be moved to song_dir


import os
import sys
import random

# Escape bad_chars in string be backslash
bad_chars="     \\()[]{}\"'&"       # this might be incomplete
def escape_necessary_characters(s):
    ret=""
    for c in s:
        if c in bad_chars : ret+="\\"+c
        else : ret+=c
    return ret

# Returns array of [folder containing file, filename.mp3]
def get_mp3s(song_dir):
    lst=[]
    for cd,subdirs,files in os.walk(song_dir):
        for f in files:
            if f.lower().endswith(".mp3"):      # change this if you want more formats
                lst+=[[cd,f]]

    return lst

# If original file name has a "number<period>" at the beginning, eg, "1001.It's not me, it's you.mp3",
# then that number will be removed to prevent long files names if script is used multiple times

# get_base_name("1001.a.mp3") = "a.mp3"
# get_base_name("a.mp3") = "a.mp3"

def get_base_name(s):
    parts=s.split(".")
    if isint(parts[0]) : parts=parts[1:]
    return ".".join(parts)

def isint(s):
    try:
        int(s)
        return True
    except Exception as e:
        return False

def main():
    song_dir=sys.argv[-1]
    songs=get_mp3s(song_dir)
    n=len(songs)

    pref=range(1,n+1)
    random.shuffle(pref)

    for i in range(n):
        command="mv "+escape_necessary_characters(songs[i][0])+"/"+escape_necessary_characters(songs[i][1])+" "
        command+=song_dir+"/"+`pref[i]`+"."+escape_necessary_characters(get_base_name(songs[i][1]))
        os.system(command)

main()
