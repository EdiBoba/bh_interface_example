from tkinter import *

root = Tk()
root.title("Menu")

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть...")
file_menu.add_command(label="Новый")
file_menu.add_command(label="Сохранить...")
file_menu.add_command(label="Выход")

help_menu = Menu(main_menu, tearoff=0)
help_menu_2 = Menu(help_menu, tearoff=0)
help_menu_2.add_command(label="Локальная справка")
help_menu_2.add_command(label="На сайте")

help_menu.add_cascade(label="Помощь",
                      menu=help_menu_2)
help_menu.add_command(label="О программе")

main_menu.add_cascade(label="Файл",
                      menu=file_menu)
main_menu.add_cascade(label="Справка",
                      menu=help_menu)

root.mainloop()
