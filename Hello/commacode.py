def listecle(_list):
    if not _list:
        print("This List is empty")
        return 
    verlist = ""
    for index, item in enumerate(_list):
        if len(_list) == 1:
            verlist += item
        elif index != len(_list)-1:
            verlist += item + ", "
        else:
            verlist += "and " + item
    print(verlist)

nuller =[]
oner = ["Time"]
twoer = ["Good", "Evil"]
eightfold = ["North","East", "South", "West","Northeast","Southeast","Southwest","Northwest"]            

listecle(nuller)
print('\n')
listecle(oner)
print('\n')
listecle(twoer)
print('\n')
listecle(eightfold)
print('\n')
