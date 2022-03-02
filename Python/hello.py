print('Hello World')
_name='Eric'
age=29
city='Yangon'
my_statement="He loves Mango"
about_me="""This is about me.
        how are you?"""
print(my_statement,about_me)
#Single Line Comment
'''
    multi
    line 
    comment
'''
print(_name,age,city)

if(age>20):
    print('age is over 20')
    print('age block')
    print('age final')
else:
    print('age is less than 20')
    print('this is else block')


#with [],{},()
fruits=['banana','mango',
'Payaya','Orange']
print(fruits)
myInfo=_name+\
city+\
my_statement+\
about_me
print(myInfo)

#Tuple elements cannot update as list
tuple = ('abcd',786,2.23,'John',70.2)
tinytuple=(123,'Yan')
print(tuple)
print(tuple[0])
print(tuple[1:4])
print(tinytuple*2)
print(tuple + tinytuple)

#dictionary

dict = {'one':"This is one"}
print(dict['one'])
dict[2]="This is Two"
print(dict[2])
dict2 = {'name':"john",'age':23,'city':'Yangon'}
print(dict2)
print(dict2['name'],dict2['age'])

