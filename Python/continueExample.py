#enter positive numbers to add , 999 to exit , skip negative numbers

#val = int (input('Enter a number to add 999 to quit : '))
sum = 0
done = False
while not done: 
    val = int(input('Enter a number to add 999 to quit : '))
    if val<0:
        print('Negative value ',val,' ignored!')
        continue
    if val!= 999:
        print('Tallying ',val)
        sum += val
    else:
        done=(val==999)
print('Sum is : ',sum)