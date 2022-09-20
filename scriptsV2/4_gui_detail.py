import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
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

        self.grid_columns = {
            'address': 'Endereço',
            'email': 'E-mail'
        }

        Session = orm.sessionmaker(bind=engine)
        self.session = Session()
        self.db_student = None

        self.config_window()
        self.create_widgets()
        self.create_grid()
        self.load_data()

    def config_window(self):
        self.title('TkInter SQLAlchemy Application')

        win_height = 430
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

    def create_grid(self):
        self.create_widget(tk.Label, text='Endereços')

        self.grid = self.create_widget(
            ttk.Treeview, height=5, selectmode="extended")
        self.grid['columns'] = tuple(self.grid_columns.keys())
        self.grid.column('#0', stretch=tk.NO, minwidth=0, width=0)

        for k, v in self.grid_columns.items():
            self.grid.heading(k, text=v, anchor=tk.W)
            self.grid.column(k, stretch=tk.NO, minwidth=50, width=250)

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
        self.create_widget(tk.Button, text="Editar Endereço", command=self.update_grid)

    def load_data(self):
        # Load Student
        self.db_student = self.session.query(Student).where(Student.id == 3).first()
        for k, v in self.var_student.items():
            v.set(getattr(self.db_student, k))

        # Load Addresses
        for addr in self.db_student.addresses:
            val = []
            for k in self.grid_columns.keys():
                val.append(getattr(addr, k))

            # Insert data and key into the grid
            self.grid.insert('', tk.END, values=val, tags=addr.id)

    def save_data(self):
        if self.db_student:
            # Save Student
            for k, v in self.var_student.items():
                setattr(self.db_student, k, v.get())

            # Save Addresses
            addrs = self.db_student.addresses
            for item in self.grid.get_children():
                addr_id = self.grid.item(item).get('tags')[0]
                addr = [row for row in addrs if getattr(row, 'id') == addr_id]
                if addr:
                    item_val = dict(zip(self.grid_columns.keys(), self.grid.item(item).get('values')))
                    for k in self.grid_columns.keys():
                        setattr(addr[0], k, item_val[k])

            self.session.commit()

    def update_grid(self):
        # Update selected address

        item = self.grid.focus()
        if item:
            item_val = dict(zip(self.grid_columns.keys(), self.grid.item(item).get('values')))
            item_val['address'] += ' Editado'
            self.grid.item(item, values=list(item_val.values()))
        else:
            msg.showinfo('Item', 'Nenhum endereço selecionado')


if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
