import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TkInter StringVar')
        self.geometry("300x130+800+400")

        # Tkinter variables
        self.entry_name = tk.StringVar()
        self.label_name = tk.StringVar()

        # Entry
        tk.Label(self, text='Nome:').pack(anchor='w', padx=(10, 0), pady=(10, 0))
        name_entry = tk.Entry(self, textvariable=self.entry_name)
        name_entry.pack(anchor='w', padx=(10, 0))

        # Button
        submit_button = tk.Button(self, text='Ler', command=self.submit)
        submit_button.pack(anchor='w', padx=(10, 0), pady=(10, 0))

        # Output
        self.output_label = tk.Label(self, textvariable=self.label_name)
        self.output_label.pack(anchor='w', padx=(10, 0), pady=(10, 0))

    # Button command
    def submit(self):
        self.label_name.set(self.entry_name.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()