file=open('table.dat','w')
file.write("""  A    B     C     D
1 11.7 0.035 2017  99.1
2 9.2  0.037 2019  101.2
3 12.2 no    no    105.1
4 10.1 0.031 no    102.1
5 9.1  0.033 2009  103.3
6 8.7  0.036 2015  101.9
""")
file.close()

infile=open('table.dat','r')
lines=infile.readlines()
infile.close()

data={}
firstline=lines[0]
properties=firstline.split()

for p in properties:
    data[p]={}
    
for line in lines[1:]:
    words = line.split()
    print(words)
    i = int(words[0])
    values = words[1:]
    for p,v in zip(properties,values):
        if v != 'no':
            data[p][i] = float(v)

print(data)
print(data['A'][1])
print(data['B'][4])
