import re                           # RE for searching thorugh the gathered text
from urllib.request import urlopen  # Urlopen for getting the text
import deepl                        # Deepl for Api translation to english
url = "https://kejserindens-gryder.dk/frokostordning/ugens-menu"
page = urlopen(url)                                     #page has the code for the website
html = page.read().decode('cp1252','backslashreplace')  #html now has the raw text of the page
listPattern = "<p.*Salater.*</p>"
subSnip = re.findall(listPattern,html)                  #find and save the strings for each day
#cleaning the list
#testMenu = []
#for x in subSnip[1:]:
#    x = re.sub("&amp;",r"\&",x)
#    x = re.sub("<br />","\n",x)
#    x = re.sub("<.*?>","",x)
#    testMenu.extend(re.findall(r"\n(.+)",x))
#testMenu.insert(24,"Brændende kærlighed af kalkun m. rødbeder (7,15)")
#testMenu.insert(25,"Mos m. stegte svampe/veggie kebab & løg (1,7,15)")

#if len(testMenu) < 75:
   # print("Menu is fucked once again")
  #  exit

#Time to make this flexiable
#WHOO HOO :(
def day_menu(day, daylist):
    daylist = re.sub("&amp;",r"\&",daylist)
    daylist = re.sub("<br />","\n",daylist)
    daylist = re.sub("<.*?>","",daylist)
    day.extend(re.findall(r"\n(.+)",daylist))

#making lists for the days
monday, tuesday, wednesday, thursday, friday = ([] for i in range(5))

#getting the menu for each day into the lists
day_menu(monday,subSnip[2]) #IMPORTENT!!! SubSnip must be calliprated each time
day_menu(tuesday, subSnip[3])
#day_menu(wednesday, subSnip[]) #grundlovsdag
day_menu(thursday, subSnip[4])
day_menu(friday,subSnip[5])

#Flex clean
def menu_cleaner(menuDay): #standard claener
    if len(menuDay)==12:
        del menuDay[-2]
        del menuDay[-3]
        del menuDay[-5:-3]
        del menuDay[-8:-6]
    elif len(menuDay)==14: # for wednesday, cake line
        del menuDay[-2]
        del menuDay[-3]
        del menuDay[-4]
        del menuDay[-6:-4]
        del menuDay[-9:-7]
    else: # for the usuel fuckery
        print(menuDay + " Is missing data")

#clean the menus
menu_cleaner(monday)
menu_cleaner(tuesday)
#menu_cleaner(wednesday)
menu_cleaner(thursday)
menu_cleaner(friday)


'''
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
del testMenu[-27]
del testMenu[-28]
del testMenu[-30:-28]
del testMenu[-33:-31]
#Monday
del testMenu[-35]
del testMenu[-36]
del testMenu[-38:-36]
del testMenu[-41:-39]
## Menu is cleaned to only relevant lines'''
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
monAlgDan,tueAlgDan,wedAlgDan,thuAlgDan,friAlgDan = ([] for i in range(5))
monAlgEng,tueAlgEng,wedAlgEng,thuAlgEng,friAlgEng = ([] for i in range(5))
engMon,engTue,engWed,engThu,engFri = ([] for i in range(5))
#algDansk = []
#algEnglish = []
#etestMenu =  []


#filling out the algs for every day
def alg_fill(menuDay,dayAlgD,dayAlgE):
    for  i in menuDay:
        temp = re.findall(r'\d+(?!.*[(])',i)
        if temp == []:
            dayAlgD.extend(["N/A"])
            dayAlgE.extend(["N/A"]) 
        else:
            for j in temp:
                tempAlg.extend([allAlgDansk[int(j)-1]])
                etempAlg.extend([allAlgEnglish[int(j)-1]])
            dayAlgD.extend([", ".join(tempAlg)])
            dayAlgE.extend([", ".join(etempAlg)])
        temp.clear()
        tempAlg.clear()
        etempAlg.clear()

#calling the function to write the algs
alg_fill(monday,monAlgDan,monAlgEng)
alg_fill(tuesday,tueAlgDan,tueAlgEng)
#alg_fill(wednesday,wedAlgDan,wedAlgEng)
alg_fill(thursday,thuAlgDan,thuAlgEng)
alg_fill(friday,friAlgDan,friAlgEng)

#Translation by DeepL API, 
auth_key = "d817f7ec-5e15-4662-9380-0efcae84f25f:fx"
translator = deepl.Translator(auth_key)

#translation function
def trans_day(menuDay,menuDayEng):
    for idi, i in enumerate(menuDay):
        menuDay[idi] = re.sub(r"\(.*?\)","",i)  
        menuDayEng.append((translator.translate_text(menuDay[idi],source_lang="DA",target_lang="EN-GB")).text)  

#translation time!
trans_day(monday,engMon)
trans_day(tuesday,engTue)
#trans_day(wednesday,engWed)
trans_day(thursday,engThu)
trans_day(friday,engFri)

'''
for idi, i in enumerate(testMenu):
    temp = re.findall(r'\d+(?!.*[(])',i)
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
'''

with open("template menu.txt","r") as file:
    template = file.readlines()
#Overwiting the lines
#Monday
def overwrite_monday():
    #Monday salads
    template[85] =    monday[0] + "\n"
    template[88] = monAlgDan[0] + "\n"
    template[92] =    monday[1] + "\n"
    template[95] = monAlgDan[1] + "\n"

    template[99]  =    engMon[0] + "\n"
    template[102] = monAlgEng[0] + "\n"
    template[106] =    engMon[1] + "\n"
    template[109] = monAlgEng[1] + "\n"

    #Monday cold cuts
    template[114] =    monday[2] + "\n"
    template[117] = monAlgDan[2] + "\n"
    template[121] =    monday[3] + "\n"
    template[124] = monAlgDan[3] + "\n"
    template[128] =    monday[4] + "\n"
    template[131] = monAlgDan[4] + "\n"

    template[135] =    engMon[2] + "\n"
    template[138] = monAlgEng[2] + "\n"
    template[142] =    engMon[3] + "\n"
    template[145] = monAlgEng[3] + "\n"
    template[149] =    engMon[4] + "\n"
    template[152] = monAlgEng[4] + "\n"

    #Monday hot dishes
    template[157] =    monday[5] + "\n"
    template[160] = monAlgDan[5] + "\n"
    template[164] =    monday[6] + "\n"
    template[167] = monAlgDan[6] + "\n"
    template[171] =    monday[7] + "\n"
    template[174] = monAlgDan[7] + "\n"

    template[178] =    engMon[5] + "\n"
    template[181] = monAlgEng[5] + "\n"
    template[185] =    engMon[6] + "\n"
    template[188] = monAlgEng[6] + "\n"
    template[192] =    engMon[7] + "\n"
    template[195] = monAlgEng[7] + "\n"
    #Monday done

#Tuesday
def overwrite_tuesday():
    #Tuesday salads
    template[202] =   tuesday[0] + "\n"
    template[205] = tueAlgDan[0] + "\n"
    template[209] =   tuesday[1] + "\n"
    template[212] = tueAlgDan[1] + "\n"

    template[216] =    engTue[0] + "\n"
    template[219] = tueAlgEng[0] + "\n"
    template[223] =    engTue[1] + "\n"
    template[226] = tueAlgEng[1] + "\n"

    #Tuesday cold cuts
    template[230] =   tuesday[2] + "\n"
    template[233] = tueAlgDan[2] + "\n"
    template[237] =   tuesday[3] + "\n"
    template[240] = tueAlgDan[3] + "\n"
    template[244] =   tuesday[4] + "\n"
    template[247] = tueAlgDan[4] + "\n"

    template[251] =    engTue[2] + "\n"
    template[254] = tueAlgEng[2] + "\n"
    template[258] =    engTue[3] + "\n"
    template[261] = tueAlgEng[3] + "\n"
    template[265] =    engTue[4] + "\n"
    template[268] = tueAlgEng[4] + "\n"

    #Tuesday hot dishes
    template[272] =   tuesday[5] + "\n"
    template[275] = tueAlgDan[5] + "\n"
    template[279] =   tuesday[6] + "\n"
    template[282] = tueAlgDan[6] + "\n"
    template[286] =   tuesday[7] + "\n"
    template[289] = tueAlgDan[7] + "\n"

    template[293] =    engTue[5] + "\n"
    template[296] = tueAlgEng[5] + "\n"
    template[300] =    engTue[6] + "\n"
    template[303] = tueAlgEng[6] + "\n"
    template[307] =    engTue[7] + "\n"
    template[310] = tueAlgEng[7] + "\n"
    #Tuesday done

#Wednesday
def overwrite_wednesday():
    #Wednesday salads
    template[316] = wednesday[0] + "\n"
    template[319] = wedAlgDan[0] + "\n"
    template[323] = wednesday[1] + "\n"
    template[326] = wedAlgDan[1] + "\n"

    template[330] =    engWed[0] + "\n"
    template[333] = wedAlgEng[0] + "\n"
    template[337] =    engWed[1] + "\n"
    template[340] = wedAlgEng[1] + "\n"

    #Wednesday cold cuts
    template[344] = wednesday[2] + "\n"
    template[347] = wedAlgDan[2] + "\n"
    template[351] = wednesday[3] + "\n"
    template[354] = wedAlgDan[3] + "\n"
    template[358] = wednesday[4] + "\n"
    template[361] = wedAlgDan[4] + "\n"

    template[365] =    engWed[2] + "\n"
    template[368] = wedAlgEng[2] + "\n"
    template[372] =    engWed[3] + "\n"
    template[375] = wedAlgEng[3] + "\n"
    template[379] =    engWed[4] + "\n"
    template[382] = wedAlgEng[4] + "\n"

    #Wednesday hot dishes
    template[386] = wednesday[5] + "\n"
    template[389] = wedAlgDan[5] + "\n"
    template[393] = wednesday[6] + "\n"
    template[396] = wedAlgDan[6] + "\n"
    template[400] = wednesday[7] + "\n"
    template[403] = wedAlgDan[7] + "\n"

    template[407] =    engWed[5] + "\n"
    template[410] = wedAlgEng[5] + "\n"
    template[414] =    engWed[6] + "\n"
    template[417] = wedAlgEng[6] + "\n"
    template[421] =    engWed[7] + "\n"
    template[424] = wedAlgEng[7] + "\n"

    #Wednesday cake
    template[428] = wednesday[8] + "\n"
    template[431] = wedAlgDan[8] + "\n"

    template[435] =    engWed[8] + "\n" 
    template[438] = wedAlgEng[8] + "\n"
    #Wednesday done

#Thursday
def overwrite_thursday():
    #Thursday salads
    template[443] =  thursday[0] + "\n"
    template[446] = thuAlgDan[0] + "\n"
    template[450] =  thursday[1] + "\n"
    template[453] = thuAlgDan[1] + "\n"

    template[457] =    engThu[0] + "\n"
    template[460] = thuAlgEng[0] + "\n"
    template[464] =    engThu[1] + "\n"
    template[467] = thuAlgEng[1] + "\n"

    #Thursday cold cuts
    template[471] =  thursday[2] + "\n"
    template[474] = thuAlgDan[2] + "\n"
    template[478] =  thursday[3] + "\n"
    template[481] = thuAlgDan[3] + "\n"
    template[485] =  thursday[4] + "\n"
    template[488] = thuAlgDan[4] + "\n"

    template[492] =    engThu[2] + "\n"
    template[495] = thuAlgEng[2] + "\n"
    template[499] =    engThu[3] + "\n"
    template[502] = thuAlgEng[3] + "\n"
    template[506] =    engThu[4] + "\n"
    template[509] = thuAlgEng[4] + "\n"

    #Thursday hot dishes
    template[513] =  thursday[5] + "\n"
    template[516] = thuAlgDan[5] + "\n"
    template[520] =  thursday[6] + "\n"
    template[523] = thuAlgDan[6] + "\n"
    template[527] =  thursday[7] + "\n"
    template[530] = thuAlgDan[7] + "\n"

    template[534] =    engThu[5] + "\n"
    template[537] = thuAlgEng[5] + "\n"
    template[541] =    engThu[6] + "\n"
    template[544] = thuAlgEng[6] + "\n"
    template[548] =    engThu[7] + "\n"
    template[551] = thuAlgEng[7] + "\n"
    #Thursday done

#Friday
def overwrite_friday():
#Friday salads
    template[557] =    friday[0] + "\n"
    template[560] = friAlgDan[0] + "\n"
    template[564] =    friday[1] + "\n"
    template[567] = friAlgDan[1] + "\n"

    template[571] =    engFri[0] + "\n"
    template[574] = friAlgEng[0] + "\n"
    template[578] =    engFri[1] + "\n"
    template[581] = friAlgEng[1] + "\n"

    #Friday cold cuts
    template[585] =    friday[2] + "\n"
    template[588] = friAlgDan[2] + "\n"
    template[592] =    friday[3] + "\n"
    template[595] = friAlgDan[3] + "\n"
    template[599] =    friday[4] + "\n"
    template[602] = friAlgDan[4] + "\n"

    template[606] =    engFri[2] + "\n"
    template[609] = friAlgEng[2] + "\n"
    template[613] =    engFri[3] + "\n"
    template[616] = friAlgEng[3] + "\n"
    template[620] =    engFri[4] + "\n"
    template[623] = friAlgEng[4] + "\n"

    #Friday hot dishes
    template[627] =    friday[5] + "\n"
    template[630] = friAlgDan[5] + "\n"
    template[634] =    friday[6] + "\n"
    template[637] = friAlgDan[6] + "\n"
    template[641] =    friday[7] + "\n"
    template[644] = friAlgDan[7] + "\n"

    template[648] =    engFri[5] + "\n"
    template[651] = friAlgEng[5] + "\n"
    template[655] =    engFri[6] + "\n"
    template[658] = friAlgEng[6] + "\n"
    template[662] =    engFri[7] + "\n"
    template[665] = friAlgEng[7] + "\n"
    #Friday done
'''
template[202] = testMenu[0] + "\n"
template[205] = algDansk[0] + "\n"
template[209] = testMenu[1] + "\n"
template[212] = algDansk[1] + "\n"

template[216] =  etestMenu[0] + "\n"
template[219] = algEnglish[0] + "\n"
template[223] =  etestMenu[1] + "\n"
template[226] = algEnglish[1] + "\n"

#Tuesday cold cuts
template[230] = testMenu[2] + "\n"
template[233] = algDansk[2] + "\n"
template[237] = testMenu[3] + "\n"
template[240] = algDansk[3] + "\n"
template[244] = testMenu[4] + "\n"
template[247] = algDansk[4] + "\n"

template[251] =  etestMenu[2] + "\n"
template[254] = algEnglish[2] + "\n"
template[258] =  etestMenu[3] + "\n"
template[261] = algEnglish[3] + "\n"
template[265] =  etestMenu[4] + "\n"
template[268] = algEnglish[4] + "\n"

#Tuesday hot dishes
template[272] = testMenu[5] + "\n"
template[275] = algDansk[5] + "\n"
template[279] = testMenu[6] + "\n"
template[282] = algDansk[6] + "\n"
template[286] = testMenu[7] + "\n"
template[289] = algDansk[7] + "\n"

template[293] =  etestMenu[5] + "\n"
template[296] = algEnglish[5] + "\n"
template[300] =  etestMenu[6] + "\n"
template[303] = algEnglish[6] + "\n"
template[307] =  etestMenu[7] + "\n"
template[310] = algEnglish[7] + "\n"
#Tuesday done
#Wednesday
#Wednesday salads
template[316] = testMenu[8] + "\n"
template[319] = algDansk[8] + "\n"
template[323] = testMenu[9] + "\n"
template[326] = algDansk[9] + "\n"

template[330] =  etestMenu[8] + "\n"
template[333] = algEnglish[8] + "\n"
template[337] =  etestMenu[9] + "\n"
template[340] = algEnglish[9] + "\n"

#Wednesday cold cuts
template[344] = testMenu[10] + "\n"
template[347] = algDansk[10] + "\n"
template[351] = testMenu[11] + "\n"
template[354] = algDansk[11] + "\n"
template[358] = testMenu[12] + "\n"
template[361] = algDansk[12] + "\n"

template[365] =  etestMenu[10] + "\n"
template[368] = algEnglish[10] + "\n"
template[372] =  etestMenu[11] + "\n"
template[375] = algEnglish[11] + "\n"
template[379] =  etestMenu[12] + "\n"
template[382] = algEnglish[12] + "\n"

#Wednesday hot dishes
template[386] = testMenu[13] + "\n"
template[389] = algDansk[13] + "\n"
template[393] = testMenu[14] + "\n"
template[396] = algDansk[14] + "\n"
template[400] = testMenu[15] + "\n"
template[403] = algDansk[15] + "\n"

template[407] =  etestMenu[13] + "\n"
template[410] = algEnglish[13] + "\n"
template[414] =  etestMenu[14] + "\n"
template[417] = algEnglish[14] + "\n"
template[421] =  etestMenu[15] + "\n"
template[424] = algEnglish[15] + "\n"

#Wednesday cake
template[428] = testMenu[16] + "\n"
template[431] = algDansk[16] + "\n"

template[435] =  etestMenu[16] + "\n" 
template[438] = algEnglish[16] + "\n"
#Wednesday done
#Thursday
#Thursday salads
template[443] = testMenu[17] + "\n"
template[446] = algDansk[17] + "\n"
template[450] = testMenu[18] + "\n"
template[453] = algDansk[18] + "\n"

template[457] =  etestMenu[17] + "\n"
template[460] = algEnglish[17] + "\n"
template[464] =  etestMenu[18] + "\n"
template[467] = algEnglish[18] + "\n"

#Thursday cold cuts
template[471] = testMenu[19] + "\n"
template[474] = algDansk[19] + "\n"
template[478] = testMenu[20] + "\n"
template[481] = algDansk[20] + "\n"
template[485] = testMenu[21] + "\n"
template[488] = algDansk[21] + "\n"

template[492] =  etestMenu[19] + "\n"
template[495] = algEnglish[19] + "\n"
template[499] =  etestMenu[20] + "\n"
template[502] = algEnglish[20] + "\n"
template[506] =  etestMenu[21] + "\n"
template[509] = algEnglish[21] + "\n"

#Thursday hot dishes
template[513] = testMenu[22] + "\n"
template[516] = algDansk[22] + "\n"
template[520] = testMenu[23] + "\n"
template[523] = algDansk[23] + "\n"
template[527] = testMenu[24] + "\n"
template[530] = algDansk[24] + "\n"

template[534] =  etestMenu[22] + "\n"
template[537] = algEnglish[22] + "\n"
template[541] =  etestMenu[23] + "\n"
template[544] = algEnglish[23] + "\n"
template[548] =  etestMenu[24] + "\n"
template[551] = algEnglish[24] + "\n"
#Thursday done
#Friday
#Friday salads
template[557] = testMenu[25] + "\n"
template[560] = algDansk[25] + "\n"
template[564] = testMenu[26] + "\n"
template[567] = algDansk[26] + "\n"

template[571] =  etestMenu[25] + "\n"
template[574] = algEnglish[25] + "\n"
template[578] =  etestMenu[26] + "\n"
template[581] = algEnglish[26] + "\n"

#Friday cold cuts
template[585] = testMenu[27] + "\n"
template[588] = algDansk[27] + "\n"
template[592] = testMenu[28] + "\n"
template[595] = algDansk[28] + "\n"
template[599] = testMenu[29] + "\n"
template[602] = algDansk[29] + "\n"

template[606] =  etestMenu[27] + "\n"
template[609] = algEnglish[27] + "\n"
template[613] =  etestMenu[28] + "\n"
template[616] = algEnglish[28] + "\n"
template[620] =  etestMenu[29] + "\n"
template[623] = algEnglish[29] + "\n"

#Friday hot dishes
template[627] = testMenu[30] + "\n"
template[630] = algDansk[30] + "\n"
template[634] = testMenu[31] + "\n"
template[637] = algDansk[31] + "\n"
template[641] = testMenu[32] + "\n"
template[644] = algDansk[32] + "\n"

template[648] =  etestMenu[30] + "\n"
template[651] = algEnglish[30] + "\n"
template[655] =  etestMenu[31] + "\n"
template[658] = algEnglish[31] + "\n"
template[662] =  etestMenu[32] + "\n"
template[665] = algEnglish[32] + "\n"
'''
with open("template 23.txt", "a") as file:
    file.writelines(template)

with open("menu snip.txt", "a") as file:
    file.write("\n".join(monday) +
               "\n".join(engMon) +
               "\n\n" +
               "\n".join(tuesday) +
               "\n".join(engTue) +
               "\n\n" +
#               "\n".join(wednesday) +
 #              "\n".join(engWed) +
  #             "\n\n" +
               "\n".join(thursday) +
               "\n".join(engThu) +
               "\n\n" +
               "\n".join(friday) +
               "\n".join(engFri) +
               "\n\n" 
               )
