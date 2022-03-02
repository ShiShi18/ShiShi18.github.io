from tkinter.tix import COLUMN


infile = open('Oxford.dat','r')
odata = infile.readline().split('\\r\\n')
#print(odata[0],odata[1])
city = odata[0][2:]
location = odata[1]
del odata[-1][-1]

temp_data = odata[7:]
data ={}
data['place']=city
data['location']=location
data['data']={}
for line in temp_data:
    columns = line.split()
    #print(columns)
    year = columns[0]
    months = columns[1]
    if columns[-1] == 'Provisional':
        del columns[-1]
    for i in range(2,len(columns)):
        if columns[i] == '---':
            columns[i]=None
        elif columns[i][-1]=="*" or columns[i][-1]=='#':
            columns[i]=float(columns[i][:-1])
        else:
            columns[i]=float(columns[i])
    tmax,tmin,air_frost,rain,sun = columns[2:]
    print(tmax,tmin,air_frost,rain,sun)

