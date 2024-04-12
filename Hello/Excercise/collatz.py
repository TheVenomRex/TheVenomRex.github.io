import time

try:
    seq = int(input())
   
    while seq != 1:
        time.sleep(0.2)
        if seq % 2 == 0:
            seq /= 2
            print(seq)
        elif seq % 2 == 1:
            seq = 3*seq + 1
            print(seq)

except ValueError:
    print("You must enter an integer")