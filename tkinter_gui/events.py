"""
<Activate>: Window has become active.
<Deactivate>: Window has been deactivated.
<MouseWheel>: Scroll wheel on mouse has been moved.
<KeyPress>: Key on keyboard has been pressed down.
<KeyRelease>: Key has been released.
<ButtonPress>: A mouse button has been pressed.
<ButtonRelease>: A mouse button has been released.
<Motion>: Mouse has been moved.
<Configure>: Widget has changed size or position.
<Destroy>: Widget is being destroyed.
<FocusIn>: Widget has been given keyboard focus.
<FocusOut>: Widget has lost keyboard focus.
<Enter>: Mouse pointer enters widget.
<Leave>: Mouse pointer leaves widget.
"""

from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Starting...")
label.grid()
label.bind('<Enter>', lambda e: label.configure(text='Moved mouse inside'))
label.bind('<Leave>', lambda e: label.configure(text='Moved mouse outside'))
label.bind('<ButtonPress-1>',
           lambda e: label.configure(text='Clicked left mouse button'))
label.bind('<3>', lambda e: label.configure(text='Clicked right mouse button'))
label.bind('<Double-1>', lambda e: label.configure(text='Double clicked'))
label.bind('<B3-Motion>',
           lambda e: label.configure(text='right button drag to %d,%d' % (e.x, e.y)))
label.bind('<B1-Motion>',
           lambda e: label.configure(text='left button drag to %d,%d' % (e.x, e.y)))
root.mainloop()
