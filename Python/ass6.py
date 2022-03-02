num = int(input('Enter a number : '))
i = 0
while i < num*2:

    if i <= num:
        #space value
        val = num - i
        while val>0:
            print(end=' ')
            val-=1

        #star value
        val = i
        while val>0:
            print(end='*')
            val-=1
    
    elif i > num:
        #space value
        val = i-num
        while val>0:
            print(end=' ')
            val-=1

        #star value
        val = i-num
        while val<num:
            print(end='*')
            val+=1
    print()
    i+=1