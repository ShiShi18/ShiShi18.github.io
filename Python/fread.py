#read file

infile = open('data.txt','r')
sum = 0
count = 0
for line in infile:
    count += 1
    sum += int(line)
mean = sum/count
print('Mean is : ',mean)

infile.close()