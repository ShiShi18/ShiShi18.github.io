num = int(input('Enter a number : '))
i = 0
while i<2*num:
    val = 1
    if i<num:
        while val<=i:
            print(end="*")
            val+=1
        
    elif i >= num:
        val = 2*num
        while val>i:
            print(end='*')
            val-=1
    print()
    i+=1