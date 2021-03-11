from tkinter import *


def insert_text():
    s = "Hello World"
    text.insert(1.0, s)


def get_text():
    s = text.get(1.0, END)
    label['text'] = s


def delete_text():
    text.delete(1.0, END)


root = Tk()
root.title("Edit")
text_frame = Frame()
text_frame.pack()
text = Text(text_frame, width=25, height=5)

scroll = Scrollbar(text_frame, command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack(side=LEFT)
scroll.pack(side=LEFT, fill=Y)

frame = Frame()
frame.pack()
Button(frame, text="Вставить", command=insert_text).pack(side=LEFT)
Button(frame, text="Взять", command=get_text).pack(side=LEFT)
Button(frame, text="Удалить", command=delete_text).pack(side=LEFT)

label = Label()
label.pack()
root.mainloop()
