
from tkinter import *
import csv

root=Tk()
root.title("lyric finder")
l=Label(root,text="enter the song name")
l.pack()
text=Text(root,width=40,height=1)
text.pack()

def search_lyrics():
    i=text.get("1.0","1.end")
    with open('test.csv','r')as f:
        data=csv.reader(f,delimiter=",")
        for row in data:
            if i==row[0]:
                l1=Label(root,text=row[1])
                l1.pack()
                print("lyrics:",row[1])
    
b=Button(root,text="search",command=search_lyrics)
b.pack()
root.mainloop()
