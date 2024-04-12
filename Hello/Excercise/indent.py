import time
indent = 0
flex = 1

for i in range(1,21):
    print(" " * indent + "********")
    time.sleep(0.1)
    
      
    indent += 1*flex
    if i % 5 ==0:
        flex *= -1

    
