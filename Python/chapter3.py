#arithmetic operator
num1 = int(input('Enter First Number'))
num2 = int(input('Enter Second Number'))
num3 = num1 + num2 #add
num4 = num1 - num2 #sub
num5 = num1 * num2 #multi
num6 = num1 / num2 #div
num7 = num1 % num2 #modulus
num8 = num1 //num2 #floordivision
num9 = num1 **num2 #exponent
print(num3,num4,num5,num6,num7,num8,num9)

#comparison Operator == , != , <> , >= , <= , > , < 
if num1==num2 :
    print('%s is equal to %s' %(num1,num2) )

if num1!=num2 : 
    print('%s is not equal to %s' %(num1,num2))

if num1>num2 :
    print('%s is greater than %s' %(num1,num2))

if num1<num2 :
    print('%s is less than %s' %(num1,num2))

if num1>=num2 :
    print('%s is greater than or equal to %s' %(num1,num2))

if num1<=num2 :
    print('%s is less than or equal to %s' %(num1,num2))

#assignment operator = , += , -= , /= , %= , **= , //=

num10 = num1 + num2
num10 += num2
num10 -= num2
num10 *= num1
print('Num 10 is %s ' %(num10))

#
a = 60 #0011 1100 #128 64 32 16 8 4 2 1
print(a<<2)

# 0000 0100 => 4
# 1111 0110 =>
#
#1100 => 12
#& 1000 => 8
#| 1101 =>13
#^ 0101 =>  5
#~0110 => 6
#~0011 => 3
a=4
b=12
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)

#logical operator

if True and True: #false soo no output
    print('ok')

if (5<9) and (2>1):
    print('ok')

print(True and False)
print(False or True)
print(not(True))
print(type(True))
