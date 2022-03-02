count = sum = 0
print('Enter 5 number!')
while count<5:
    val= float(input('Enter number: '))
    if val<0:
        print('Unacceptable! Terminating --- !')
        break  
    else:
        print('Avg = ', sum/count)
    count +=1
    sum += val