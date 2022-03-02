from tkinter import *
root = Tk()
C_entry = Entry(root,width=4)
C_entry.pack(side= 'left')

C_unit_label = Label(root,text='Celsius')
C_unit_label.pack(side='left')

def compute():
    C = float(C_entry.get())
    F = (9.0/5)*C + 32
    F_label.configure(text='%g' % F)

compute = Button(root,text=' is ',command=compute)
compute.pack(side='left',padx=4)

F_label = Label(root,width = 4)
F_label.pack (side = 'left',padx=4)

F_unit_label=Label(root,text='Fahrenheit')
F_unit_label.pack(side='left')
root.mainloop()