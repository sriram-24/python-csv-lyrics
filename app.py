# import required modules
from tkinter import *
import csv
from csv import writer
# pandas is for csv file parsing
import pandas as pd 

# defining the root window or main window
# geometry is height and width of window
# Screen cannot be maximized because of the unresponsive design. so, resizable set to 0

root=Tk()
root.geometry("889x600")
root.resizable(0,0)

# configuring rows and columns 
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

# main title of the application
root.title("lyric finder")

# display frames in window
# tkraise will display frame at top
def show_frame(frame):
    frame.tkraise()

# defining the frames for application
search_frame = Frame(root)
Add_songs_frame = Frame(root)
list_songs_frame = Frame(root)

# parsing the seperate frames and positions
for frame in (search_frame,Add_songs_frame,list_songs_frame):
    frame.grid(row=0,column=0,sticky="nsew")


#search frame

# background image for frame
# relwidth relheight is relative height and width of the image
search_filepath=r"undraw_the_search_s0xf.png"
search_filename = PhotoImage(file=search_filepath)
search_background = Label(search_frame ,image=search_filename)
search_background.place(x=0,y=0,relwidth=1,relheight=1)

# Adding button navigation to search frame
# lambda function used to call the frames seperately
# place(x,y) is position of the button in x and y coordinates
# search_frame in the Button parameter is to show on which frame button is placed
search_button = Button(search_frame,text="Search lyrics", command = lambda:show_frame(search_frame) )
search_button.place(x=20,y=10)

list_songs_button = Button(search_frame,text="Songs list", command = lambda:show_frame(list_songs_frame))
list_songs_button.place(x=100,y=10)

add_songs_button = Button(search_frame,text="Add songs", command = lambda:show_frame(Add_songs_frame))
add_songs_button.place(x=170,y=10)

# adding labels to search frame
# config is used to modify the label. bg->backgroundcolor
l=Label(search_frame,text="Enter the songname")
l.config(bg="white")
l.place(x=400,y=25)

# adding text box
text=Text(search_frame,width=40,height=1)
text.place(x=300,y=55)

# defining search lyrics function
# text.get() to get text from the textbox 
def search_lyrics():
    i=text.get("1.0","1.end")
    # opens csv file search the song name and place the lyrics in label
    with open('test.csv','r',newline='')as f:
        data=csv.reader(f,delimiter=",")
        for row in data:
            if i==row[0]:
                l1=Label(search_frame,text=row[1],wraplength=600)
                l1.place(x=200,y=150)
                print("lyrics:",row[1])

# adding search button to excecute the search operation
search=Button(search_frame,text="search",command=search_lyrics)
search.place(x=435,y=85)


# list songs frame

# background image for list songs frame
song_list_filepath=r"undraw_happy_music_g6wc.png"
song_list_filename = PhotoImage(file=song_list_filepath)
song_list_background = Label(list_songs_frame ,image=song_list_filename)
song_list_background.place(x=0,y=0,relwidth=1,relheight=1)

# read the csv file using the pandas library and convert all the song names into list
# selects all the songname from column of index 0 and add it to list
df = pd.read_csv("test.csv")
matrix2 = df[df.columns[0]].to_numpy()
song_list_final = matrix2.tolist()

# adding song listbox
# list box used to display the songs in list form
song_label=Listbox(list_songs_frame)

# parsing through every song name and insert it in the listbox
# insert(index, songname)
for index in range(len(song_list_final)):
    song_label.insert(index,song_list_final[index])
song_label.place(x=400,y=55)

# defining the song list navigation in the list_songs_frame
search_button = Button(list_songs_frame,text="Search lyrics", command = lambda:show_frame(search_frame))
search_button.place(x=20,y=10)

list_songs_button = Button(list_songs_frame,text="Songs list", command = lambda:show_frame(list_songs_frame))
list_songs_button.place(x=100,y=10)

add_songs_button = Button(list_songs_frame,text="Add songs", command = lambda:show_frame(Add_songs_frame))
add_songs_button.place(x=170,y=10)

# adding label in list_songs_frame
song_list = Label(list_songs_frame,text="List of song lyrics available")
song_list.place(x=400,y=25)

# add songs frame 

# defining add song function
# assigning empty song list and adding the inputs to the list
def add_song():

    song=[]
    name = song_name.get("1.0","end-1c")
    lyrics = lyrics_name.get("1.0","end-1c")
    song.append(name)

    # replace line breaks to space because csv cannot parse line breaks
    # replace commas because commas seperate the string to a new value that may cause errors while displaying lyrics
    newline=lyrics.replace("\n"," ")
    comma_removed = newline.replace(","," ")
    song.append(comma_removed)

    # opens file and append songs at end of the file
    # csv writer writes the song to file
    # delimeter, escapechar,etc are optional parameters for defining the csv file options
    # writerow() wites only on single row
    with open('test.csv','a+',newline='') as write_song:
        csv_writer = writer(write_song,delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE, lineterminator='\n')
        csv_writer.writerow(song)
        print(song)

# background image for add songs frame
filepath=r"undraw_compose_music_ovo2.png"
filename = PhotoImage(file=filepath)
background = Label(Add_songs_frame ,image=filename)
background.place(x=0,y=0,relwidth=1,relheight=1)

#  defining buttons for add songs frame
search_button = Button(Add_songs_frame,text="Search lyrics", command = lambda:show_frame(search_frame))
search_button.place(x=20,y=10)

list_songs_button = Button(Add_songs_frame,text="Songs list", command = lambda:show_frame(list_songs_frame))
list_songs_button.place(x=100,y=10)

add_songs_button = Button(Add_songs_frame,text="Add songs", command = lambda:show_frame(Add_songs_frame))
add_songs_button.place(x=170,y=10)

# adding labels to the frame
l=Label(Add_songs_frame,text="Song name :")
l.config(bg="white")
l.place(x=300,y=25)

# adding text input to the frame
song_name=Text(Add_songs_frame,width=40,height=1)
song_name.place(x=400,y=25)

# adding label to the frame
l=Label(Add_songs_frame,text="Lyrics:")
l.config(bg="white")
l.place(x=300,y=55)

# adding text input to the frame
lyrics_name=Text(Add_songs_frame,width=40,height=20)
lyrics_name.place(x=400,y=55)

# adding button to excecute the add song function in the frame
add_button=Button(Add_songs_frame,text="Add lyrics", command=add_song)
add_button.place(x=435,y=390)

# default frame on the main window when the application starts
show_frame(search_frame)

# looping infinite to display the main window until user closes the application
root.mainloop()
