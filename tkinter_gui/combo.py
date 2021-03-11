from tkinter import *
from tkinter import ttk


def callback(event):
    label_result["text"] = f"Favourite month: {month_var.get()}"


root = Tk()
root.title("Combo")

label = Label(root,
              text="Choose your favourite month:")

month_var = StringVar()
month = ttk.Combobox(root, textvariable=month_var,
                     values=(
                         "January",
                         "February",
                         "March",
                         "April"
                     ))
month.current(2)
month.bind("<<ComboboxSelected>>", callback)

label_result = Label(root)

label.pack()
month.pack()
label_result.pack()
root.mainloop()
