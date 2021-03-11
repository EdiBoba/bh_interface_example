from tkinter import *

root = Tk()
root.title("ContextMenu")

label = Label(root,
              text="Right-click to display menu",
              width=40, height=20)
label.pack()

m = Menu(root, tearoff=0)
m.add_command(label="Cut")
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_command(label="Reload")
m.add_separator()
m.add_command(label="Rename")


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


label.bind("<Button-3>", do_popup)

mainloop()
