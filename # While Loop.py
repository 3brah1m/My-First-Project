import random
def numberguesser():

    userans = int(input("The computer has chosen a number between 0 and 5. Guess the number: "))

    lst1 = random.randint(0,5)
    if userans == lst1:
        print('You got the answer correct!')
    else:
        print('You got the answer wrong.')
        print('The number was: ' + str(lst1))

numberguesser()