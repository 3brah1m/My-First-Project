def patternprint():
    l = int(input("Which pattern do you want? "))
    l1 = '*'
    l2 = '* *'
    l3 = '* * *'
    l4 = '* * * *'
    l5 = '* * * * *'
    l1r = '    *'
    l2r = '   * *'
    l3r = '  * * *'
    l4r = ' * * * *'
    l1e = '        *'
    l2e = '       * *'
    l3e = '      * * *'
    l4e = '     * * * *'
    l5e = '    * * * * *'
    l6e = '   * * * * * *'
    l7e = '  * * * * * * *'
    l8e = ' * * * * * * * *'
    l9e = '* * * * * * * * *'
    if l == 1:
        print(l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5)
    if l == 2:
        print(l5 + '\n' + l4 + '\n' + l3 + '\n' + l2 + '\n' + l1)
    if l == 3:
        print(l1r + '\n' + l2r + '\n' + l3r + '\n' + l4r + '\n' + l5)
    if l == 4:
        print(l5 + '\n' + l4r + '\n' + l3r + '\n' + l2r + '\n' + l1r)
    if l == 5:
        print(l1e + '\n' + l2e + '\n' + l3e + '\n' + l4e + '\n' + l5e + '\n' + l6e + '\n' + l7e + '\n' + l8e + '\n' + l9e)
    if l == 6:
        print(l9e + '\n' + l8e + '\n' + l7e + '\n' + l6e + '\n' + l5e + '\n' + l4e + '\n' + l3e + '\n' + l2e + '\n' + l1e)
    if l == 7:
        print(l1e + '\n' + l2e + '\n' + l3e + '\n' + l4e + '\n' + l4e + '\n' + l3e + '\n' + l2e + '\n' + l1e)

patternprint()