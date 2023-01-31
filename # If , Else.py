import random
mypoints = 0
cpupoints = 0
while(True):
    mychoice = int(input('Enter 1 for Rock, 2 for Paper, 3 for Scissors: '))
    cpuchoice = random.randint(1,3)
    if mychoice == cpuchoice:
        print('It is a tie. No points will be given')
    elif mychoice == 1:
        if cpuchoice == 2:
            print('CPU chose paper and won!')
            cpupoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
        if cpuchoice == 3:
            print('CPU chose scissors and lost!')
            mypoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
    elif mychoice == 2:
        if cpuchoice == 1:
            print('CPU chose rock and lost!')
            mypoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
        if cpuchoice == 3:
            print('CPU chose scissors and won!')
            cpupoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
    else:
        if cpuchoice == 1:
            print('CPU chose rock and won!')
            cpupoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
        if cpuchoice == 2:
            print('CPU chose paper and lost!')
            mypoints += 1
            print('CPU score: ' + str(cpupoints))
            print('Your score: ' + str(mypoints))
    if mypoints == 5:
        print('You won!! Best 5 out of 6!')
        break
    if cpupoints == 5:
        print('You lost. CPU won.')
        break