#get size of table to print numbers
size= int (input('Please enter size of table: '))
print('      ',end='')

#first row with numbers
for i in range(1,size+1):
    print('{0:4}'.format(i),end='')
print()
print('    +',end='')

#second row with + and ----
for i in range(1,size+1):
    print('----',end='')
print()

#print table
for i in range(1,size+1):
     
    #print row number
    print('{0:3} | '.format(i),end='')
    for j in range(1,size+1):
        product =i*j
        print('{0:4}'.format(product),end='')
    print()
