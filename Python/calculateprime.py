#prime => start from 2
#can divided by itself
#search 10 to 19
'''
for i in range(1,15,2):
    print(i)

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print('%d is %d * %d' %(num,j,i))
            break
    else:
        print(num,' is prime')


i=2
while i<100:
    j=2
    while j<=i/j:
        if not(i%j): break
        j = j+1
    if j> i/j : print(i,' is prime')
    i = i+ 1

num1 = int(input('Enter a starting number : '))
num2 = int(input('Enter a ending number : '))

for num in range(num1,num2):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print(' %d is %d x %d' %(num,i,j))
            break
    else:
        print(end='***')
        print(num,' is prime')
'''

i = 2
while i < 100:
    j = 2
    while j <= (i/j):
        if not(i%j):
            break
        j+=1
    if j > i/j:
        print(i,' is prime')
    i+=1
    