import random
import array
def passgen():
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    signs = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    for i in range(8):
        randnum = random.choice(num)
        randlow = random.choice(low)
        randup = random.choice(up)
        randsigns = random.choice(signs)
        tempass = randnum + randlow + randup + randsigns
    print(tempass)

passgen()