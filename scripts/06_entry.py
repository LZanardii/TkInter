from tkinter import *

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

Label(window, text="Nome: ").grid(column=0, row=0)
Entry(window, width=30).grid(column=1, row=0)

Label(window, text="Sobrenome: ").grid(column=0, row=1)
Entry(window, width=30).grid(column=1, row=1)

window.mainloop()
