from tkinter import *
from tkcalendar import *


root = Tk()
root.title("Date")

cal = Calendar(root, selectmode="day", year=2021, month=3, day=3)
cal.pack(pady=20)


def get_date():
    label.config(text=cal.get_date())


button = Button(root, text="Select the Date", command=get_date)
button.pack(pady=20)


label = Label(root, text="")
label.pack(pady=20)

root.mainloop()
