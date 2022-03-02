#if statement False,0,None = False
var1 = 100 #none so yin alote ma lote
if var1:
    print('100 is True expression')
    print(var1)
print('End')

#if else
var2 = int(input('Enter a number: '))
if var2&2 == 1:
    print(var2, ' is ODD')
else:
    print(var2, ' is EVEN')
print('bye')

#else if statement 
var3 = 100
if var3<200:
    print(var3, ' is less than 200')
    if var3 == 150:
        print(' which is 150')
    elif var3 == 100:
        print('which is 100')
    elif var3 == 50:
        print('Which is 50')
    elif var3 <50:
        print('which is less than 50')
else:
    print(var3, ' is greater than or equal to 200')
print('Bye!')

#check divisor not to  be zero
divident = int(input('Enter Divident: '))
divisor = int(input('Enter Divisor: '))
#if divisor zero or not
if divisor !=0:
    quotient=divident/divisor
    print(divident, '/',divisor,'=',quotient)
print('End!')

# 1 => 0001 / 12 => 0012 => 135 => 0135
print(end='[')
print('2')
print('3')