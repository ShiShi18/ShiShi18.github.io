counter=100
miles=1000.0
name="John"
print(counter,miles,name)
print(type(counter))
print(type(miles))
print(type(name))
#multiple assignment
a=b=c=1
print(a,b,c)
a,b,c=1,2,3
print(a,b,c)

str="Hello World!"
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "test")

#list example
list = ['abcd',786,2.23,'john',70.2]
tinylist = [123,'john']
print(list) 
list[0]="yan"
print(list[-1])
print(list[1:3])
print(list[:-2])
print(tinylist*2)
print(list + tinylist)