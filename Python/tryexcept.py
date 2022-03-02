#try caluse to validate
temp = input('Enter F degree')
try: 
    temp = float(temp)
    cel = (temp - 32)*5.0/9.0
    print(cel)
except: 
    print('Error!')