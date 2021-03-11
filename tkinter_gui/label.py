from tkinter import Tk, Label

root = Tk()
root.title("Labels")
root.geometry('300x200')

label_1 = Label(root, text="Я просто надпись")
label_2 = Label(root, text="Я тоже")
label_1.pack()
label_2.pack()
root.mainloop()
