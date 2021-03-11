from tkinter import *


def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'


root = Tk()
root.title("Button")
root.geometry('300x200')
b1 = Button(text="Сменить цвет кнопки", width=20, height=3)
b1.config(command=change)
b1.pack()
root.mainloop()
