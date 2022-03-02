#user input
print('Enter 5 number !')
num1 = int(input('Enter Number 1 : '))
num2 = int(input('Enter Number 2 : '))
num3 = int(input('Enter Number 3 : '))
num4 = int(input('Enter Number 4 : '))
num5 = int(input('Enter Number 5 : '))
max_num = num1
min_num = num1

#maximum number
if num2>num1: max_num = num2
if num3>num2: max_num = num3
if num4>num3: max_num = num4
if num5>num4: max_num = num5
print(max_num,' is Maximum number.')

#minimum number
if num2<num1: max_num = num2
if num3<num2: max_num = num3
if num4<num3: max_num = num4
if num5<num4: max_num = num5
print(min_num,' is Minimum number.')


