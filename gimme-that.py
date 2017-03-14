import os
import urllib
import time
now = time.strftime("%c")


input("What is the link for the 4chan thread: ")
os.chdir(os.path.join( os.getenv('USERPROFILE'), 'Downloads'))
if os.path.isdir((time.strftime("%d-%m-%Y"))):
    os.chdir(time.strftime("%d-%m-%Y"))
elif not os.path.isdir(time.strftime("%d-%m-%Y")):
    os.mkdir(time.strftime("%d-%m-%Y"))
    os.chdir(time.strftime("%d-%m-%Y"))

