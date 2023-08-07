import os
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Photo Viewer")
piclist=os.listdir("pictures")
i=0
myimg=ImageTk.PhotoImage(Image.open("pictures\pic1.jpg"))
mlabel=Label(root, image=myimg,padx=50, pady=50, highlightthickness=5)
picname=Label(root, text='pic1.jpg')
mlabel.grid(row=0, column=0,rowspan=3,columnspan=3)
picname.grid(row=3, column=1)
status=Label(root, text=f"Image 1 of {len(piclist)}", relief=SUNKEN)
status.grid(row=4, column=0, columnspan=3)
def photochanger(place):
    global i
    global myimg
    global mlabel
    global status
    status.grid_forget()
    i=i+place
    
    listlenght= len(piclist)
    if i>= listlenght:
        i=listlenght-i
    if i<= (-1*listlenght):
        i=listlenght+i
    elif place==+1:
        status=Label(root, text=f"Image {(piclist.index(piclist[i]) + 1)} of {len(piclist)}")
        mlabel.grid_forget()
        myimg=ImageTk.PhotoImage(Image.open(f"pictures\{piclist[i]}"))
    elif place==-1:
        status=Label(root, text=f"Image {(piclist.index(piclist[i]) + 1)} of {len(piclist)}")
        mlabel.grid_forget()
        myimg=ImageTk.PhotoImage(Image.open(f"pictures\{piclist[i]}"))
    mlabel=Label(root, image=myimg,padx=50, pady=50, highlightthickness=5)
    picname=Label(root, text=f"{piclist[i]}")
    mlabel.grid(row=0, column=0,rowspan=3,columnspan=3)
    picname.grid(row=3, column=1)
    status.grid(row=4, column=0, columnspan=3)

nextbutton=Button(root, text=">>", command=lambda: photochanger(+1))
nextbutton.grid(row=3, column=3)

#picname.grid(row=4, column=1, columnspan=3)
backbutton=Button(root, text="<<", command=lambda: photochanger(-1))
backbutton.grid(row=3, column=0)
#backbutton.pack()
#
#nextbutton.pack()
root.mainloop()





