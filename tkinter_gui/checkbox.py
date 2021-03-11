from tkinter import *

root = Tk()
root.title("Checkbox")


def show():
    lab['text'] = f"Var1: {var1.get()}\nVar2:{var2.get()}"


frame = Frame()
frame.pack(side=LEFT)

var1 = BooleanVar()
var1.set(0)

var2 = IntVar()
var2.set(-1)

c1 = Checkbutton(frame, text="First",
                 variable=var1, onvalue=1,
                 offvalue=0, command=show)
c1.pack(anchor=W, padx=10)


c2 = Checkbutton(frame, text="Second",
                 variable=var2, onvalue=1,
                 offvalue=0, command=show)
c2.pack(anchor=W, padx=10)

lab = Label(width=25, height=5, bg="lightblue")
lab.pack(side=RIGHT)

root.mainloop()
