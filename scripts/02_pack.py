from tkinter import *

window = Tk()
window.title("GUI com TK")
window.geometry('600x300')

Label(window, text="Top", borderwidth=2, relief="groove").pack(side = TOP, fill = 'x')
Label(window, text="Bottom", borderwidth=2, relief="groove").pack(side = BOTTOM, fill = 'x')
Label(window, text="Left", borderwidth=2, relief="groove").pack(side = LEFT, fill = 'y')
Label(window, text="Right", borderwidth=2, relief="groove").pack(side = RIGHT, fill = 'y')
Label(window, text="Expand", borderwidth=2, relief="groove").pack(fill = BOTH, expand = True)

window.mainloop()
