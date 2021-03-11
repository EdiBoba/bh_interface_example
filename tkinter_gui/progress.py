from tkinter import *
from tkinter.ttk import *
import time


root = Tk()
root.title("Progress")


progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='determinate')


def bar():
    value = 0
    while value <= 100:
        progress['value'] = value
        value += 20
        root.update_idletasks()
        time.sleep(1)


progress.pack(pady=10)
Button(root, text='Start', command=bar).pack(pady=10)
root.mainloop()
