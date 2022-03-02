#Division
print('Enter two number to divide')
divident = int(input('Enter divident : '))
divisor = int(input('Enter divisor : '))
result  = divident / divisor
print(divident,'/',divisor,'=',result)

#Half

value=int(input('Enter a number to split : '))
result=value/2
print('Half of ',value, 'is', result)

#temparature
#C = 5/9 * (F - 32)

degreeF = float(input('Enter F Degree'))
degreeC = 5/9 * (degreeF - 32)
print(degreeF,'degree F = ', degreeC ,'degree C')

#time convertion

seconds = int(input('Please enter seconds : '))
hour = seconds//3600
seconds = seconds%3600
minutes = seconds//60
seconds = seconds%60
print(hour,' : ',minutes,' : ',seconds)