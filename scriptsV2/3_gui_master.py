import tkinter as tk
import tkinter.ttk as ttk
from orm_model import *


class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.var_student = {
            'id': tk.IntVar(),
            'name': tk.StringVar(),
            'lastname': tk.StringVar(),
            'sex': tk.StringVar(),
            'age': tk.IntVar()
        }

        Session = orm.sessionmaker(bind=engine)
        self.session = Session()
        self.db_student = None

        self.config_window()
        self.create_widgets()
        self.load_data()

    def config_window(self):
        self.title('TkInter SQLAlchemy Application')

        win_height = 405
        win_width = 520

        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        x_coor = int((scr_width/2) - (win_width/2))
        y_coor = int((scr_height/2) - (win_height/2))

        self.geometry(f'{win_width}x{win_height}+{x_coor}+{y_coor}')

    def create_widget(self, widget_type, **kwargs):
        elem = widget_type(self)
        for k, v in kwargs.items():
            elem[k] = v

        elem.pack(anchor='w', padx=(10, 0))
        return elem

    def create_widgets(self):
        self.create_widget(tk.Button, text='Salvar', command=self.save_data)
        self.create_widget(tk.Label, text='Id')
        self.create_widget(tk.Entry, textvariable=self.var_student.get('id'), state=tk.DISABLED)
        self.create_widget(tk.Label, text='Nome')
        self.create_widget(tk.Entry, textvariable=self.var_student.get('name'))
        self.create_widget(tk.Label, text='Sobrenome')
        self.create_widget(tk.Entry, textvariable=self.var_student.get('lastname'))
        self.create_widget(tk.Label, text='Sexo')
        self.create_widget(ttk.Combobox, textvariable=self.var_student.get('sex'), values=('M', 'F'), state='readonly')
        self.create_widget(tk.Label, text='Idade')
        self.create_widget(tk.Entry, textvariable=self.var_student.get('age'))

    def load_data(self):
        # Load Student
        self.db_student = self.session.query(Student).where(Student.id == 3).first()
        for k, v in self.var_student.items():
            v.set(getattr(self.db_student, k))

    def save_data(self):
        # Save Student
        if self.db_student:
            for k, v in self.var_student.items():
                setattr(self.db_student, k, v.get())

            self.session.commit()

if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()