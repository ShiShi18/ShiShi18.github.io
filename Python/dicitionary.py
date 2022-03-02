temps = {'Osolo':13,'London':14.3}
temps['Paris'] = 15
print(temps['London'])
print(temps.keys())
print(temps.values())
for key in temps:
    print(key,'==>',temps)