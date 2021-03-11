from tkinter import *

root = Tk()
root.title("Pic")

img = PhotoImage(file="python.png")
panel = Label(root, image=img)
panel.pack(fill="both", expand="yes")
mainloop()
