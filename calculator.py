from tkinter import *
root=Tk()
root.title("CALCULATOR")
e1=Entry(root,borderwidth=7).grid(row=0,column=0,  columnspan=5)
def pint():
    e1.insert(0,Text)
b1=Button(root,activebackground="green", text="9",image="IMG_20170211_103306.jpeg", padx=20, pady=15).grid(column=2, row=2)
b2=Button(root,activebackground="green", text="8", padx=20, pady=15).grid(column=1, row=2)
b3=Button(root,activebackground="green", text="7", padx=20, pady=15).grid(column=0, row=2)
b4=Button(root,activebackground="green", text="6", padx=20, pady=15).grid(column=2, row=3)
b5=Button(root,activebackground="green", text="5", padx=20, pady=15).grid(column=1, row=3)
b6=Button(root,activebackground="green", text="4", padx=20, pady=15).grid(column=0, row=3)
b7=Button(root,activebackground="green", text="3", padx=20, pady=15).grid(column=2, row=4)
b8=Button(root,activebackground="green", text="2", padx=20, pady=15).grid(column=1, row=4)
b9=Button(root,activebackground="green", text="1", padx=20, pady=15).grid(column=0, row=4)
b0=Button(root,activebackground="green", text="0", padx=20, pady=15).grid(column=1, row=5)
badd=Button(root, text="+", padx=20, pady=15).grid(column=0, row=1)
bminus=Button(root, text="-", padx=20, pady=15).grid(column=1, row=1)
bmultiply=Button(root, text="x", padx=20, pady=15).grid(column=2, row=1)
bdivide=Button(root, text="/", padx=20, pady=15).grid(column=3, row=1)
bequal=Button(root, text="=", padx=20, pady=15).grid(column=3, row=2)

root.mainloop()