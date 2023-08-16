#importing necessary modules
import urllib.request
import requests
from tkinter import *
from PIL import Image,ImageTk  # pip install Pillow
import webbrowser

def callback(url):
   webbrowser.open_new_tab(url)

root= Tk()   #First window
root.title("News Searcher")
txt=Label(root,text="Enter Text to search news").grid(row=0,column=0)   #the topic to search news
search_key=Entry(root)
search_key.grid(row=1,column=0)

def search(news):                  #the function for the news page
    try:
        search_key.delete(0,END)
        window=Toplevel()
        window.title(f"News on {news}")
    # window.geometry('300x250')
        info=requests.get(f"https://newsapi.org/v2/everything?q={news}&sortBy=popularity&apiKey=2b9d99b6e7134e84a70c26de80c994c9")
        query=info.json()
        allnews=query["articles"][0]
        urllib.request.urlretrieve(allnews['urlToImage'],'tempic.jpg')
        image=Image.open("tempic.jpg")
        image1=image.resize((300,205), Image.LANCZOS)
        myimg=ImageTk.PhotoImage(image1)

        title=Label(window,text=allnews["title"], font=("Comic Sans", 20, 'bold')).grid(row=0,column=0,columnspan=2)
        topic_pic=Label(window,image=myimg).grid(row=1,column=0,columnspan=2)
        description=Message(window,text=allnews['description']).grid(row=2,column=0, rowspan=2,columnspan=2)
    # description.insert(END,allnews['description'])
        link_box=Label(window, text="click here for more info:", cursor="hand2", fg='blue',font=('Helveticabold', 10))
        link_box.grid(row=2,column=2)
        link_box.bind("<Button-1>", lambda e:
        callback(allnews['url']))
        window.mainloop()
    except:                           # in case no info is available on that topic
        window=Toplevel()
        tell=Label(window, text="No Information Available on this, Search something else if you wish")
        tell.pack()
        window.mainloop()

getbutton=Button(root,text="Search the news",padx=20,pady=15, command=lambda:search(search_key.get()))
getbutton.grid(row=2,column=0)

root.mainloop()

'''
All the details that can be accessed with eample as : Apple-
{'source': {'id': None, 'name': 'Lifehacker.com'}, 
'author': 'Amanda Blum', 
'title': 'My Three Favorite Tools for Processing Summer Fruit', 
'description': 'Processing fruit every summer can be daunting. We all start out with the same ambition: We see the cherry branches dripping with red lobes and dream of an entire winter of cherry pies. We side-eye the apple tree, thinking this is the year we’re going to final…', 
'url': 'https://lifehacker.com/my-three-favorite-tools-for-processing-summer-fruit-1850654124',
 'urlToImage': 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/62c0f14c6c6a4aaab2341695625ee092.jpg', 
 'publishedAt': '2023-07-19T14:30:00Z', 
 'content': 'Processing fruit every summer can be daunting. We all start out with the same ambition: We see the cherry branches dripping with red lobes and dream of an entire winter of cherry pies. We side-eye th… [+4046 chars]'
}'''

