from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

Label(window, text='Selecione um item da lista: ').grid(row=0, column=0)
combo = ttk.Combobox(window)
combo['values']= (1, 2, 3.3, 'A', "Text")
combo.current(1)
combo.grid(row=0, column=1)

window.mainloop()
