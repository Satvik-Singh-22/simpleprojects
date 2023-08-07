from tkinter import *
root=Tk()
root.title("CALCULATOR")
#root.resizable("DISABLED")
e=Entry(root, borderwidth=5)
e.grid(row=0,column=0,  columnspan=7)    
first_num=0
parameter=''
def cadd(comm):
    global first_num
    global parameter
    first_num=int(e.get())
    parameter=comm
    e.delete(0,END)
def cequal():
    sno=e.get()
    e.delete(0,END)
    if parameter=='+':
        e.insert(0,first_num+ int(sno)  )
    elif parameter=='-':
        e.insert(0,(first_num -int(sno)))
    elif parameter=="*":
        e.insert(0,(first_num  *int(sno)))
    elif parameter=='/':
        e.insert(0,(first_num /int(sno)))
def numbutton(number,rno,cno):
    numbutton=Button(root,activebackground="green",text=number,padx=20,pady=15, command= lambda:e.insert(END,number))
    numbutton.grid(row=rno, column=cno)
b1=numbutton(1,3,0)
b2=numbutton(2,3,1)
b3=numbutton(3,3,2)
b4=numbutton(4,2,0)
b5=numbutton(5,2,1)
b6=numbutton(6,2,2)
b7=numbutton(7,1,0)
b8=numbutton(8,1,1)
b9=numbutton(9,1,2)
b0=numbutton(0,4,1)
bclear=Button(root,text="Clear", padx=10, pady=15, command=lambda: e.delete(0,END)).grid(row=4, column=2)
badd=Button(root, text="+", padx=20, pady=15, command=lambda:cadd('+') ).grid(column=3, row=1)
bminus=Button(root, text="-", padx=20, pady=15, command=lambda:cadd('-')).grid(column=3, row=2)
bmultiply=Button(root, text="x", padx=20, pady=15, command=lambda:cadd('*')).grid(column=3, row=3)
bdivide=Button(root, text="/", padx=20, pady=15, command=lambda:cadd('/')).grid(column=3, row=4)
bequal=Button(root, text="=", padx=20, pady=15, command=cequal).grid(column=0, row=4)

root.mainloop()

