from tkinter import *

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

Label(window, text='Label 1').pack(fill = 'x')
Label(window, text='Label 2', bg='lime', font=("Arial Bold", 20)).pack(fill = 'x')
Label(window, text='Label 3', bg='silver', borderwidth=2, relief="groove", font=("Times New Roman", 48)).pack(fill = BOTH, expand = True)

window.mainloop()
