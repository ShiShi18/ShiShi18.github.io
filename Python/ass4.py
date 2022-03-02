from ast import Num


i = 0
sum = 0

print('Enter 20 numbers ! ')
while i < 20:
    val = float(input('Enter a number: '))
    if i == 0:
        max = val 
        min = val
    if val < 0:
        print('Negative Detected!Program Terminate!')
        break
    else:
        i+=1
        sum+=val
        if val > max:
            max = val
        elif val < min:
            min = val
else:
    print('Sum is ',sum)
    print('Average is ',sum/i)
    print('Max is ',max)
    print('Min is ',min)