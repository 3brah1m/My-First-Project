import random
import time

def typetester():
    print("plz type what's written bellow. plz type it fast and you have got 100 seconds to write it")
    lst = ['what happened to you','why are you crying','hello good morning','bye have a good day']
    rand = random.choice(lst)
    time1 = time.time()
    l = str(input(rand + '   '))
    if rand == l:
        print('Time:'+ str(time1))

typetester()
