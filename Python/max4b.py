print('Enter 4 number to compare!')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
num4 = int(input('Enter fourth number: '))
max=num1
if num2>num1:
    max=num2
if num3>num2:
    max=num3
if num4>num3:
    max=num4
print('Maximum number is : ',max)
