def patternprint(n,y):
    if y == 1:
        for i in range(n):
            for j in range(i + 1):
                print('$',end = ' ')
            print('')
    if y == 2:
        for u in range(n):
            for k in range(u,n):
                print('!',end = ' ')
            print('')
    if y == 3:
        for t in range(n):
            for w in range(t,n):
                print(' ',end = ' ')
            for l in range(t + 1):
                print('#',end = ' ')
            print()
    if y == 4:
        for s in range(n):
            for e in range(s + 1):
                print(' ',end = ' ')
            for x in range(s,n):
                print('%',end = ' ')
            print()
    if y == 5:
        for d in range(n):
            for g in range(d,n):
                print(' ',end = ' ')
            for m in range(d):
                print('@',end = ' ')
            for m in range(d + 1):
                print('@',end = ' ')
            print()
    if y == 6:
        for z in range(n):
            for p in range(z + 1):
                print(' ',end = ' ')
            for v in range(z,n-1):
                print('/',end = ' ')
            for v in range(z,n):
                print('/',end = ' ')
            print()
    if y == 7:
        for d in range(n):
            for g in range(d,n):
                print(' ',end = ' ')
            for m in range(d):
                print('&',end = ' ')
            for m in range(d + 1):
                print('&',end = ' ')
            print()
        for d in range(n):
            for g in range(d + 1):
                print(' ',end = ' ')
            for m in range(d,n-1):
                print('&',end = ' ')
            for m in range(d,n):
                print('&',end = ' ')
            print()

patternprint(5,7)
