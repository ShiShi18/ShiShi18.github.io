value=int(input('Enter a number in range 0 to 10: '))
if value>=0:
    if value<=10:
        print(value, ' is in range')
    else:
        print(value,' is too large')
else:
    print(value,' is too small')