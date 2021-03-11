from tkinter import *


def insert():
    entry.insert(0, "Tkinter - GUI ")


root = Tk()
root.title("Labels")
root.geometry('300x200')


entry = Entry(width=50)
button = Button(text="Вставить", command=insert)

entry.pack()
button.pack()
root.mainloop()
