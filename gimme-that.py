import os
import urllib
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from wget import bar_adaptive
import wget
now = time.strftime("%c")


chan_url = input("What is the link for the 4chan thread: ")

req = Request(chan_url, headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(req)
content = url.read()
soup = BeautifulSoup(content, "html.parser")

os.chdir(os.path.join( os.getenv('USERPROFILE'), 'Downloads'))
if os.path.isdir((time.strftime("%d-%m-%Y"))):
    os.chdir(time.strftime("%d-%m-%Y"))
elif not os.path.isdir(time.strftime("%d-%m-%Y")):
    os.mkdir(time.strftime("%d-%m-%Y"))
    os.chdir(time.strftime("%d-%m-%Y"))

content = str(content)
#bunch of regexp stuff that took me really long to make
#still don't understand
#finds all the images in a thread
i = re.findall('\"[^\"]*/i.4cdn.org/[a-z]{0,4}/[0-9]*.(?:jpg|png|gif)\"', content)
i = list(set(i))
for link in i:
    link = link.replace('\"', '')
    link = "https:" + link
    wget.download(link)
