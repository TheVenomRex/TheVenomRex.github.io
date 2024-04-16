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
listPattern = "<p.*Salater.*</p>"
subSnip = re.findall(listPattern,snips) #sub snips with html

#cleaning the list
testMenu = []
for x in subSnip[5:]:
    x = re.sub("&amp;",r"\&",x)
    x = re.sub("<br />","\n",x)
    x = re.sub("<.*?>","",x)
    testMenu.extend(re.findall(r"\n(.+)",x))

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
## Menu is cleaned to only relevant lines
# Now to partition line and allegens
# Make a new list for the allergens

allAlgDansk =[r"\algA",
              r"\algB",
              r"\algC",
              r"\algD",
              r"\algE",
              r"\algF",
              r"\algG",
              r"\algH",
              r"\algI",
              r"\algJ",
              r"\algK",
              r"\algL",
              r"\algM",
              r"\algN",
              r"\algO",
              r"\algP"]
allAlgEnglish =[r"\algAe",
              r"\algBe",
              r"\algCe",
              r"\algDe",
              r"\algEe",
              r"\algFe",
              r"\algGe",
              r"\algHe",
              r"\algIe",
              r"\algJe",
              r"\algKe",
              r"\algLe",
              r"\algMe",
              r"\algNe",
              r"\algOe",
              r"\algPe"]
tempAlg = []
etempAlg = []
algDansk = []
algEnglish = []

menuSnip = open("menu snip uge 16.txt","a") #slet
menuSnip.write("\n \n")                     #slet

for idi, i in enumerate(testMenu):
    temp = re.findall(r"\d+",i)
    if temp == []:
        algDansk.extend(["N/A"])
        algEnglish.extend(["N/A"]) 
    else:
        for j in temp:
            tempAlg.extend([allAlgDansk[int(j)-1]])
            etempAlg.extend([allAlgEnglish[int(j)-1]])
        algDansk.extend([", ".join(tempAlg)])
        algEnglish.extend([", ".join(etempAlg)])
    temp.clear()
    tempAlg.clear()
    etempAlg.clear()

    testMenu[idi] = re.sub(r"\(.*?\)","",i)    
    menuSnip.write(i + "\n")                #slet
    menuSnip.write(algDansk[idi] + "\n")    #slet
    menuSnip.write(algEnglish[idi] + "\n")  #slet
menuSnip.close                              #slet
with open("template menu.txt","r") as file:
    template = file.readlines()
#Overwiting the lines
#Monday salads
template[85] = testMenu[1] + "\n"
template[88] = algDansk[1] + "\n"
template[92] = testMenu[2] + "\n"
template[95] = algDansk[2] + "\n"

template[99] #automate translation
template[102] = algEnglish[1] + "\n"
template[106]
template[109] = algEnglish[2] + "\n"

#Monday cold cuts
template[114] = testMenu[3] + "\n"
template[117] = algDansk[3] + "\n"
template[121] = testMenu[4] + "\n"
template[124] = algDansk[4] + "\n"
template[128] = testMenu[5] + "\n"
template[131] = algDansk[5] + "\n"

template[135] #automate translation
template[138] = algEnglish[3] + "\n"
template[142]
template[145] = algEnglish[4] + "\n"
template[149]
template[152] = algEnglish[5] + "\n"

#Monday hot dishes
template[157] = testMenu[6] + "\n"
template[160] = algDansk[6] + "\n"
template[164] = testMenu[7] + "\n"
template[167] = algDansk[7] + "\n"
template[171] = testMenu[8] + "\n"
template[174] = algDansk[8] + "\n"

template[178] #automate translation
template[181] = algEnglish[6] + "\n"
template[185]
template[188] = algEnglish[7] + "\n"
template[192]
template[195] = algEnglish[8] + "\n"
#Monday done
#Tuesday
#Tuesday salads
template[202] = testMenu[9] + "\n"
template[205] = algDansk[9] + "\n"
template[209] = testMenu[10] + "\n"
template[212] = algDansk[10] + "\n"

template[216] #automate translation
template[219] = algEnglish[9] + "\n"
template[223]
template[226] = algEnglish[10] + "\n"

#Tuesday cold cuts
template[230] = testMenu[11] + "\n"
template[233] = algDansk[11] + "\n"
template[237] = testMenu[12] + "\n"
template[240] = algDansk[12] + "\n"
template[244] = testMenu[13] + "\n"
template[247] = algDansk[13] + "\n"

template[251] #automate translation
template[254] = algEnglish[11] + "\n"
template[258]
template[261] = algEnglish[12] + "\n"
template[265]
template[268] = algEnglish[13] + "\n"

#Tuesday hot dishes
template[272] = testMenu[14] + "\n"
template[275] = algDansk[14] + "\n"
template[279] = testMenu[15] + "\n"
template[282] = algDansk[15] + "\n"
template[286] = testMenu[16] + "\n"
template[289] = algDansk[16] + "\n"

template[293] #automate translation
template[296] = algEnglish[14] + "\n"
template[300]
template[303] = algEnglish[15] + "\n"
template[307]
template[310] = algEnglish[16] + "\n"
#Tuesday done
#Wednesday
#Wednesday salads
template[316] = testMenu[17] + "\n"
template[319] = algDansk[17] + "\n"
template[323] = testMenu[18] + "\n"
template[326] = algDansk[18] + "\n"

template[330] #automate translation
template[333] = algEnglish[17] + "\n"
template[337]
template[340] = algEnglish[18] + "\n"

#Wednesday cold cuts
template[344] = testMenu[19] + "\n"
template[347] = algDansk[19] + "\n"
template[351] = testMenu[20] + "\n"
template[354] = algDansk[20] + "\n"
template[358] = testMenu[21] + "\n"
template[361] = algDansk[21] + "\n"

template[365] #automate translation
template[368] = algEnglish[19] + "\n"
template[372]
template[375] = algEnglish[20] + "\n"
template[379]
template[382] = algEnglish[21] + "\n"

#Wednesday hot dishes
template[386] = testMenu[22] + "\n"
template[389] = algDansk[22] + "\n"
template[393] = testMenu[23] + "\n"
template[396] = algDansk[23] + "\n"
template[400] = testMenu[24] + "\n"
template[403] = algDansk[24] + "\n"

template[407] #automate translation
template[410] = algEnglish[22] + "\n"
template[414]
template[417] = algEnglish[23] + "\n"
template[421]
template[424] = algEnglish[24] + "\n"

#Wednesday cake
template[428] = testMenu[25] + "\n"
template[431] = algDansk[25] + "\n"

template[435] #automate translation
template[438] = algEnglish[25] + "\n"
#Wednesday done
#Thursday
# - - missing 2 day

with open("template 16.txt", "w") as file:
    file.writelines(template)
