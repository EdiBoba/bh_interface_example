from tkinter import *


def add_item():
    box.insert(END, entry.get())
    entry.delete(0, END)


def del_list():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)


def save_list():
    frame = open('list000.txt', 'w')
    frame.writelines("\n".join(box.get(0, END)))
    frame.close()


root = Tk()
root.title("List")

box = Listbox(selectmode=EXTENDED)
box.pack(side=LEFT)
scroll = Scrollbar(command=box.yview)
scroll.pack(side=LEFT, fill=Y)
box.config(yscrollcommand=scroll.set)

frame = Frame()
frame.pack(side=LEFT, padx=10)
entry = Entry(frame)
entry.pack(anchor=N)
Button(frame, text="Add", command=add_item).pack(fill=X)
Button(frame, text="Delete", command=del_list).pack(fill=X)
Button(frame, text="Save", command=save_list).pack(fill=X)

root.mainloop()
