from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text='Label1').grid(column=0, row=0)
lbl2 = Label(tab2, text= 'Label2').grid(column=0, row=0)

tab_control.pack(expand=True, fill=BOTH)

window.mainloop()
