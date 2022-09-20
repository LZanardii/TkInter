from tkinter import *

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

for i in range(5):
    for j in range(5):
        Label(window, text="Linha {} coluna {}".format(i, j),
        borderwidth=2, relief="groove").grid(row = i, column = j)

window.mainloop()
