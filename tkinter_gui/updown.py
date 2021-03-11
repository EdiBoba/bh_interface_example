from tkinter import *

root = Tk()
root.title("UpDown")
root.geometry("300x200")

w = Label(root, text='Spinbox', font="50")
w.pack()

sp = Spinbox(root, from_=0, to=20)
sp.pack()

root.mainloop()
