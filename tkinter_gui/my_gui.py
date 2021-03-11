"""
Последняя строка вызывает функцию mainloop. Эта функция вызывает бесконечный цикл окна, поэтому окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто.
"""

from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
# Мы можем установить размер окна по умолчанию, используя функцию geometry следующим образом:
window.geometry('400x250')
# Затем мы установим позицию в окне с помощью функции grid и укажем ее следующим образом:
# Если функция grid не будет вызвана, текст не будет отображаться.
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
# Установка фокуса виджета ввода
# Здесь все очень просто, ведь все, что нам нужно сделать, — это вызвать функцию focus:
# Когда вы запустите свой код, вы заметите, что виджет ввода в фокусе, который дает возможность сразу написать текст.
txt.focus()
# Чтобы отключить виджет ввода, отключите свойство состояния:
# txt = Entry(window,width=10, state='disabled')
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=2, row=0)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=1)
# Чтобы получить элемент select, вы можете использовать функцию get вот таким образом:
# combo.get()
chk_state = BooleanVar()
chk_state.set(True)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=1, row=1)
# Установка состояния Checkbutton
# Здесь мы создаем переменную типа BooleanVar, которая не является стандартной переменной Python, это переменная Tkinter, затем передаем ее классу Checkbutton, чтобы установить состояние чекбокса как True в приведенном выше примере.
# Вы можете установить для BooleanVar значение false, что бы чекбокс не был отмечен.
# Так же, используйте IntVar вместо BooleanVar и установите значения 0 и 1.
# chk_state = IntVar()
# chk_state.set(0) # False
# chk_state.set(1) # True
# Эти примеры дают тот же результат, что и BooleanVar.
window.mainloop()
