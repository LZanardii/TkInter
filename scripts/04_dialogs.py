from tkinter import messagebox

messagebox.showinfo('Info', 'Conteúdo da mensagem')
messagebox.showwarning('Warning', 'Conteúdo da mensagem')
messagebox.showerror('Error', 'Conteúdo da mensagem')

print(messagebox.askquestion('Ask Question', 'Pergunta?'))
print(messagebox.askyesno('Ask Yes No','Pergunta?'))
print(messagebox.askyesnocancel('Ask Yes No Cancel','Pergunta?'))
print(messagebox.askokcancel('Ask Ok Cancel','Pergunta?'))
print(messagebox.askretrycancel('Ask Retry Cancel','Pergunta?'))
