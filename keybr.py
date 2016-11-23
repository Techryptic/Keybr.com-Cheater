#!/usr/bin/python
# -*- coding: utf-8 -*-

#anthonys.io | Twitter.com/Tech
#Copy div class= "TextInput TextInput--sizeX0 TextInput--inactive" Then run script:
#python keybr.py
#Than focus back on your browser

#sudo pip install requests beautifulsoup4
#sudo apt-get install python-tk language-pack-en

import os;
import sys;
import re;
import subprocess
import time
import Tkinter
from Tkinter import *
import sys;

#Unicode errors fixing
reload(sys);
sys.setdefaultencoding("utf8")

#After we copied from InspectElement, we hold clipboard data
r = Tk()
r.clipboard_get()
copiedtext = r.clipboard_get()

#Save copied data to file
text_file = open("input.txt", "w")

#Fixed unicode errors with sys.set/
text_file.write(copiedtext)
r.clipboard_append('')
r.destroy()
text_file.close()

#replace all varibles
replacements = {'<span class="TextInput-item TextInput-item--cursor">':'', '</span>':'', '<wbr>':'', '<span class="TextInput-item ">':'', '<span class="TextInput-item TextInput-item--special ">':'', '<div style="position: absolute; top: 0px; left: 0px; width: 0em; height: 1em; overflow: hidden;"><input style="display: block; margin: 0px; padding: 0px; width: 1em; height: 1em; font-size: 1em; line-height: 1em; border: medium none; outline: medium none;" type="text"></div><div class="TextInput-fragment">':'','<br>':'', '</div><div class="TextInput-label">Click to activate...</div>':'', '␣':' ', '↵':' ', '<div class="TextInput TextInput--sizeX0 TextInput--inactive">':''}
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)

#open the textfile, 1 Second to go back to website so it can type text.
time.sleep(1)
text = open('output.txt', 'r').read().strip()
for ch in text:
#type out the text
    subprocess.call(["xdotool", "type", ch])
#increase or decrease the time below to type slower or faster
time.sleep(0.0001)

#now lets overwrite the file to save space and then delete it
open('input.txt', 'w').close()
open('output.txt', 'w').close()
os.remove("input.txt")
os.remove("output.txt")

