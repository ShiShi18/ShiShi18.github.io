data = \
[[ 0.75,        0.29619813, -0.29619813, -0.75      ],
 [ 0.29619813,  0.11697778, -0.11697778, -0.29619813],
 [-0.29619813, -0.11697778,  0.11697778,  0.29619813],
 [-0.75,       -0.29619813,  0.29619813,  0.75      ]]

outfile=open('tmp_data.dat','w')
for list in data:
     for value in list:
         outfile.write('%14.8f' % value)
     outfile.write('\n')
outfile.close()