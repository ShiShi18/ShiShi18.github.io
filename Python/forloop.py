#for loop with in
for letter in 'Python':
    print('Current letter', letter)

fruits=['Banana','Mango','Orange']
for fruit in fruits:
    print('I like',fruit)

print(fruits[0])
print(fruits[1])
print(len(fruits))
for i in range(len(fruits)):
    print('I like',fruits[i])

mylist = [2,4,6,8,9]
for i in range(len(mylist)):
    mylist[i]=mylist[i]**2
print(mylist)