import re                           # RE for searching thorugh the gathered text
from urllib.request import urlopen  # Urlopen for getting the text
import deepl                        # Deepl for Api translation to english
url = "https://kejserindens-gryder.dk/frokostordning/ugens-menu"
page = urlopen(url)                                     #page has the code for the website
html = page.read().decode('cp1252','backslashreplace')  #html now has the raw text of the page
listPattern = "<p.*Salater.*</p>"
subSnip = re.findall(listPattern,html)                  #find and save the strings for each day
#cleaning the list
testMenu = []
for x in subSnip[3:]:
    x = re.sub("&amp;",r"\&",x)
    x = re.sub("<br />","\n",x)
    x = re.sub("<.*?>","",x)
    testMenu.extend(re.findall(r"\n(.+)",x))
testMenu.insert(24,"Fiskedunser (2 stk.) m. kartofler, persillesauce & sesamstegt broccoli (1,3,4,7,10,11,15)")
testMenu.insert(25,"Linsefrikadeller m. kartofler, persillesauce & sesamstegt broccoli (1,3,7,10,11,15,16)")

#if len(testMenu) < 72:
#    print("Menu is fucked once again")
#    exit


## Time to clean
#Friday
del testMenu[-2]
del testMenu[-3]
del testMenu[-5:-3]
del testMenu[-8:-6]
#Thursday
del testMenu[-10]
del testMenu[-11]
del testMenu[-13:-11]
del testMenu[-16:-14]
#Wednesday
del testMenu[-18]
del testMenu[-19]
del testMenu[-20]
del testMenu[-22:-20]
del testMenu[-25:-23]
#Tuesday
#del testMenu[-27]
#del testMenu[-28]
del testMenu[-30:-28]
del testMenu[-33:-31]
#Monday
del testMenu[-35]
del testMenu[-36]
del testMenu[-38:-36]
del testMenu[-41:-39]
## Menu is cleaned to only relevant lines
"""monday
del testMenu[2:4]
del testMenu[5:7]
del testMenu[6]
del testMenu[7]
#Tuesday
#del testMenu[-11]
#del testMenu[-12]
del testMenu[10:12]
del testMenu[13:15]
#onsdag
del testMenu[18:20]
del testMenu[21:23]
del testMenu[22]
del testMenu[23]
del testMenu[24]
"""




#testMenu[12] = 'ForÃ¥rssalat med rygeost og kalkun (3,6,7,10,15)'
#testMenu[20] = 'Kejserindens pÃ¸lsesalat (3,6,7,10,15)'

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
etestMenu =  []

#Translation by DeepL API, 
auth_key = "d817f7ec-5e15-4662-9380-0efcae84f25f:fx"
translator = deepl.Translator(auth_key)

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
    etestMenu.append((translator.translate_text(testMenu[idi],source_lang="DA",target_lang="EN-GB")).text)  

with open("template menu.txt","r") as file:
    template = file.readlines()
#Overwiting the lines
#Monday salads
template[85] = testMenu[0] + "\n"
template[88] = algDansk[0] + "\n"
template[92] = testMenu[1] + "\n"
template[95] = algDansk[1] + "\n"

template[99]  =  etestMenu[0] +"\n"
template[102] = algEnglish[0] + "\n"
template[106] =  etestMenu[1] + "\n"
template[109] = algEnglish[1] + "\n"

#Monday cold cuts
template[114] = testMenu[2] + "\n"
template[117] = algDansk[2] + "\n"
template[121] = testMenu[3] + "\n"
template[124] = algDansk[3] + "\n"
template[128] = testMenu[4] + "\n"
template[131] = algDansk[4] + "\n"

template[135] =  etestMenu[2] + "\n"
template[138] = algEnglish[2] + "\n"
template[142] =  etestMenu[3] + "\n"
template[145] = algEnglish[3] + "\n"
template[149] =  etestMenu[4] + "\n"
template[152] = algEnglish[4] + "\n"

#Monday hot dishes
template[157] = testMenu[5] + "\n"
template[160] = algDansk[5] + "\n"
template[164] = testMenu[6] + "\n"
template[167] = algDansk[6] + "\n"
template[171] = testMenu[7] + "\n"
template[174] = algDansk[7] + "\n"

template[178] =  etestMenu[5] + "\n"
template[181] = algEnglish[5] + "\n"
template[185] =  etestMenu[6] + "\n"
template[188] = algEnglish[6] + "\n"
template[192] =  etestMenu[7] + "\n"
template[195] = algEnglish[7] + "\n"
#Monday done
#Tuesday
#Tuesday salads
template[202] = testMenu[8] + "\n"
template[205] = algDansk[8] + "\n"
template[209] = testMenu[9] + "\n"
template[212] = algDansk[9] + "\n"

template[216] =  etestMenu[8] + "\n"
template[219] = algEnglish[8] + "\n"
template[223] =  etestMenu[9] + "\n"
template[226] = algEnglish[9] + "\n"

#Tuesday cold cuts
template[230] = testMenu[10] + "\n"
template[233] = algDansk[10] + "\n"
template[237] = testMenu[11] + "\n"
template[240] = algDansk[11] + "\n"
template[244] = testMenu[12] + "\n"
template[247] = algDansk[12] + "\n"

template[251] =  etestMenu[10] + "\n"
template[254] = algEnglish[10] + "\n"
template[258] =  etestMenu[11] + "\n"
template[261] = algEnglish[11] + "\n"
template[265] =  etestMenu[12] + "\n"
template[268] = algEnglish[12] + "\n"

#Tuesday hot dishes
template[272] = testMenu[13] + "\n"
template[275] = algDansk[13] + "\n"
template[279] = testMenu[14] + "\n"
template[282] = algDansk[14] + "\n"
template[286] = testMenu[15] + "\n"
template[289] = algDansk[15] + "\n"

template[293] =  etestMenu[13] + "\n"
template[296] = algEnglish[13] + "\n"
template[300] =  etestMenu[14] + "\n"
template[303] = algEnglish[14] + "\n"
template[307] =  etestMenu[15] + "\n"
template[310] = algEnglish[15] + "\n"
#Tuesday done
#Wednesday
#Wednesday salads
template[316] = testMenu[16] + "\n"
template[319] = algDansk[16] + "\n"
template[323] = testMenu[17] + "\n"
template[326] = algDansk[17] + "\n"

template[330] =  etestMenu[16] + "\n"
template[333] = algEnglish[16] + "\n"
template[337] =  etestMenu[17] + "\n"
template[340] = algEnglish[17] + "\n"

#Wednesday cold cuts
template[344] = testMenu[18] + "\n"
template[347] = algDansk[18] + "\n"
template[351] = testMenu[19] + "\n"
template[354] = algDansk[19] + "\n"
template[358] = testMenu[20] + "\n"
template[361] = algDansk[20] + "\n"

template[365] =  etestMenu[18] + "\n"
template[368] = algEnglish[18] + "\n"
template[372] =  etestMenu[19] + "\n"
template[375] = algEnglish[19] + "\n"
template[379] =  etestMenu[20] + "\n"
template[382] = algEnglish[20] + "\n"

#Wednesday hot dishes
template[386] = testMenu[21] + "\n"
template[389] = algDansk[21] + "\n"
template[393] = testMenu[22] + "\n"
template[396] = algDansk[22] + "\n"
template[400] = testMenu[23] + "\n"
template[403] = algDansk[23] + "\n"

template[407] =  etestMenu[21] + "\n"
template[410] = algEnglish[21] + "\n"
template[414] =  etestMenu[22] + "\n"
template[417] = algEnglish[22] + "\n"
template[421] =  etestMenu[23] + "\n"
template[424] = algEnglish[23] + "\n"

#Wednesday cake
template[428] = testMenu[24] + "\n"
template[431] = algDansk[24] + "\n"

template[435] =  etestMenu[24] + "\n" 
template[438] = algEnglish[24] + "\n"
#Wednesday done
#Thursday
#Thursday salads
template[443] = testMenu[25] + "\n"
template[446] = algDansk[25] + "\n"
template[450] = testMenu[26] + "\n"
template[453] = algDansk[26] + "\n"

template[457] =  etestMenu[25] + "\n"
template[460] = algEnglish[25] + "\n"
template[464] =  etestMenu[26] + "\n"
template[467] = algEnglish[26] + "\n"

#Thursday cold cuts
template[471] = testMenu[27] + "\n"
template[474] = algDansk[27] + "\n"
template[478] = testMenu[28] + "\n"
template[481] = algDansk[28] + "\n"
template[485] = testMenu[29] + "\n"
template[488] = algDansk[29] + "\n"

template[492] =  etestMenu[27] + "\n"
template[495] = algEnglish[27] + "\n"
template[499] =  etestMenu[28] + "\n"
template[502] = algEnglish[28] + "\n"
template[506] =  etestMenu[29] + "\n"
template[509] = algEnglish[29] + "\n"

#Thursday hot dishes
template[513] = testMenu[30] + "\n"
template[516] = algDansk[30] + "\n"
template[520] = testMenu[31] + "\n"
template[523] = algDansk[31] + "\n"
template[527] = testMenu[32] + "\n"
template[530] = algDansk[32] + "\n"

template[534] =  etestMenu[30] + "\n"
template[537] = algEnglish[30] + "\n"
template[541] =  etestMenu[31] + "\n"
template[544] = algEnglish[31] + "\n"
template[548] =  etestMenu[32] + "\n"
template[551] = algEnglish[32] + "\n"
#Thursday done
#Friday
#Friday salads
template[557] = testMenu[33] + "\n"
template[560] = algDansk[33] + "\n"
template[564] = testMenu[34] + "\n"
template[567] = algDansk[34] + "\n"

template[571] =  etestMenu[33] + "\n"
template[574] = algEnglish[33] + "\n"
template[578] =  etestMenu[34] + "\n"
template[581] = algEnglish[34] + "\n"

#Friday cold cuts
template[585] = testMenu[35] + "\n"
template[588] = algDansk[35] + "\n"
template[592] = testMenu[36] + "\n"
template[595] = algDansk[36] + "\n"
template[599] = testMenu[37] + "\n"
template[602] = algDansk[37] + "\n"

template[606] =  etestMenu[35] + "\n"
template[609] = algEnglish[35] + "\n"
template[613] =  etestMenu[36] + "\n"
template[616] = algEnglish[36] + "\n"
template[620] =  etestMenu[37] + "\n"
template[623] = algEnglish[37] + "\n"

#Friday hot dishes
template[627] = testMenu[38] + "\n"
template[630] = algDansk[38] + "\n"
template[634] = testMenu[39] + "\n"
template[637] = algDansk[39] + "\n"
template[641] = testMenu[40] + "\n"
template[644] = algDansk[40] + "\n"

template[648] =  etestMenu[38] + "\n"
template[651] = algEnglish[38] + "\n"
template[655] =  etestMenu[39] + "\n"
template[658] = algEnglish[39] + "\n"
template[662] =  etestMenu[40] + "\n"
template[665] = algEnglish[40] + "\n"
#Friday done

with open("template 20.txt", "a") as file:
    file.writelines(template)

with open("menu snip.txt", "a") as file:
    file.write("\n\n" + "\n".join(testMenu))
    file.write("\n\n" + "\n".join(etestMenu))