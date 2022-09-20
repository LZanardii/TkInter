from tkinter import *
import tkinter.ttk as ttk

def btn_nome_click():
    lbl_status.configure(text='Nome = ' + entry_nome.get())

def btn_sexo_click():
    lbl_status.configure(text='Sexo = ' + combo_sexo.get())

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

lbl_status = Label(window, text='Status: ')
lbl_status.grid(row=0, column=1)

lbl_nome = Label(window, text='Nome: ').grid(row=1, column=0)
entry_nome = Entry(window, width=30)
entry_nome.grid(row=1, column=1)
btn_nome = Button(window, text='Ler Nome', command=btn_nome_click).grid(row=1, column=2)

Label(window, text='Sexo: ').grid(row=2, column=0)
combo_sexo = ttk.Combobox(window, width=28)
combo_sexo['values']= ('Masculino', 'Feminino')
combo_sexo.current(1)
combo_sexo.grid(row=2, column=1)
btn_sexo = Button(window, text='Ler Sexo', command=btn_sexo_click).grid(row=2, column=2)

window.mainloop()
