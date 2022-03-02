#space => height - row
#star => 2*row+1
height = int(input('Enter tree height : '))
row = 0
while row<height:
    #space count = height-row
    count=0
    while count<height-row:
        print(end=' ')
        count+=1
    #star count = 2* row + 1
    count = 0
    while count<2*row+1:
        print(end='*')
        count+=1
    print()
    row+=1