import random
numberOfStreaks = 0
streakSize = 6
streak = 1
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    notes = []
    for i in range(100):     
        flip = random.randint(0,1)
        if flip == 0:
            notes.append("H")
        elif flip == 1:
            notes.append("T")
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
        # look at the first value, then check the next if they match you are starting a streak. then move on
    for i in  range(99):
        if notes[i] == notes[i+1]:
            streak +=1
            if streak == streakSize:
                numberOfStreaks += 1
        else:
            streak = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))

