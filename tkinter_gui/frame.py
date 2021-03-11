from tkinter import ttk, Tk, Label

root = Tk()
root.title("Frames")
root.geometry('300x200')
parent_frame = ttk.LabelFrame(root, text='Родитель')
label_1 = Label(parent_frame, width=5, height=2, bg='yellow', text="1")
child_frame = ttk.LabelFrame(parent_frame, text='потомок')
label_2 = Label(child_frame, width=5, height=2, bg='orange', text="2")

parent_frame.pack()
child_frame.pack()
label_1.pack()
label_2.pack()

root.mainloop()
