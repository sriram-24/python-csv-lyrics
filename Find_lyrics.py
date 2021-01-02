from tkinter import *
import csv

root = Tk()
root.state("zoomed")

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

def show_frame(frame):
    frame.tkraise()

# menubar = Menu(root)
# search = Menu(menubar,tearoff=0)
# menubar.add_cascade(label = "Search" ,menu=search,command=show_frame(frame1))

# list_songs = Menu(menubar,tearoff=0)
# menubar.add_cascade(label = "Songs list" ,menu=list_songs,command=show_frame(frame2))

# add_songs = Menu(menubar,tearoff=0)
# menubar.add_cascade(label = "Add songs" ,menu=add_songs)
# root.config(menu = menubar)

# def show_frame(frame):
#     frame.tkraise()

frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)

for frame in (frame1,frame2,frame3):
    frame.grid(row=0,column=0,sticky="nsew")

# frame 1
l=Label(frame1,text="enter the song name")
l.config(bg="white")
l.pack()

text=Text(frame1,width=40,height=1)
text.pack()
def search_lyrics():
    i=text.get("1.0","1.end")
    with open('test.csv','r')as f:
        data=csv.reader(f,delimiter=",")
        for row in data:
            if i==row[0]:
                l1=Label(frame1,text=row[1])
                l1.config(bg="white")
                l1.pack()
                print("lyrics:",row[1])
    
b=Button(frame1,text="search",command=search_lyrics)
b.pack()

btn1=Button(frame1,text="frame 3", command=lambda:show_frame(frame2))
btn1.pack()
# frame 2
text1=Label(frame2, text="frame 2")
text1.pack()
btn=Button(frame2,text="frame 3", command=lambda:show_frame(frame1))
btn.pack()
show_frame(frame1)


root.mainloop()