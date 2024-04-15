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
#subSnip = re.sub("<.*?>","",subSnip) 
#cleaning the list
#for x in subSnip:
    #x = re.sub("&amp;","&",x)
    #x = re.sub("</p>","\n",x)
#[re.sub("<.*?>", " ", i) for i in subSnipList]
menuSnip = open("menu snip uge 16.txt","a")
testMenu = []
for x in subSnip[5:]:
    x = re.sub("&amp;",r"\&",x)
    x = re.sub("<br />","\n",x)
    x = re.sub("<.*?>","",x)
    #x = re.sub("Salater","",x)
    #x = re.sub("Pålæg","",x)
    #x = re.sub("Varm ret","",x)
    #x = re.sub("/ minus gris","",x)
    #x = re.sub("/ vegetar","",x)    
#    menuSnip.write(x)
#    menuSnip.write("\n")
    testMenu.extend(re.findall(r"\n(.+)",x))
menuSnip.write("\n \n")

#testMenu.extend(re.findall("^.+.*$",subSnip))

## time to clean
#friday
del testMenu[-2]
del testMenu[-3]
del testMenu[-5:-3]
del testMenu[-8:-6]
#thursday
del testMenu[-10]
del testMenu[-11]
del testMenu[-13:-11]
del testMenu[-16:-14]
#wednesday
del testMenu[-18]
del testMenu[-19]
del testMenu[-20]
del testMenu[-22:-20]
del testMenu[-25:-23]
#tuesday
del testMenu[-27]
del testMenu[-28]
del testMenu[-30:-28]
del testMenu[-33:-31]
#thursday
del testMenu[-35]
del testMenu[-36]
del testMenu[-38:-36]
del testMenu[-41:-39]
#del testMenu[2:3]
for i in testMenu:
    menuSnip.write(i + "\n")
menuSnip.close

