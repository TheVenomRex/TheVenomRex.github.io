import re
from urllib.request import urlopen
# urlopen gets the text, 
# re gets the tools to search it
url = "https://kejserindens-gryder.dk/frokostordning/ugens-menu"
"""
page = urlopen(url)
html = page.read().decode('cp1252','backslashreplace')
#html now has the raw text of the page
#now to find and save the strings for each day
looking = open("html menu 15-16 v2.txt", "a")
looking.write(html)
looking.close
"""
#Temp data handeling, streamline later
# 
snips = open("html menu 15-16 v2.txt", "r").read()
#menuPattern = '<div class="menu2">.*<hr class="smallFatHr" />'
##subSnip = match_menuPattern.group()
listPattern = "<p.*Salater.*</p>"
subSnip = re.findall(listPattern,snips)
subSnipList = list(subSnip)
#subSnip = re.sub("<.*?>","",subSnip) 
#cleaning the list
#for x in subSnip:
    #x = re.sub("&amp;","&",x)
    #x = re.sub("</p>","\n",x)
[re.sub("<.*?>", " ", subSnipList[i]) for i in subSnipList]
menuSnip = open("menu snip uge 16.txt","a")
for x in subSnipList:
    menuSnip.write(x)
    menuSnip.write("\n")
menuSnip.close
