import tkinter as tk
from tkinter import ttk

class RegistroFuncionario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastrar empresa")
        self.geometry("700x500")
        self.configure(bg='#FFFFFF')
        self.dados_empresa()

    def dados_empresa(self):
        self.grid_columnconfigure(0, weight=1)
        frame_destaque = tk.Frame(self, bg="#00008B")
        frame_destaque.grid(row=0, column=0, columnspan=3, sticky='ew')

        label_principal = tk.Label(frame_destaque, text='CADASTRAR EMPRESA',
                                   fg="#FFFFFF", bg="#00008B", font=("Arial", 14, "bold"))
        label_principal.pack(anchor='center')

        # # === Estilo para fundo branco do Notebook ===
        # style = ttk.Style()
        # style.theme_use('default')
        # style.configure('TNotebook', background='#FFFFFF', borderwidth=0)
        # style.configure('TNotebook.Tab', background='#FFFFFF', padding=[10, 5])
        # style.map("TNotebook.Tab", background=[("selected", "#FFFFFF")])

        # === Notebook ===
        cadastro = ttk.Notebook(self, style='TNotebook')
        cadastro.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

        aba1 = tk.Frame(cadastro, bg='#FFFFFF')
        aba2 = tk.Frame(cadastro, bg='#FFFFFF')
        aba3 = tk.Frame(cadastro, bg='#FFFFFF')

        cadastro.add(aba1, text='Dados da empresa')
        cadastro.add(aba2, text='Responsável')
        cadastro.add(aba3, text='Acesso e Controle Interno')

        # === ABA 1 ===
        campos_aba1 = [
            "Razão Social", "Nome Fantasia", "CNPJ", "Inscrição Municipal",
            "Natureza Jurídica", "Ramo de Atividade", "Data de Fundação",
            "Endereço", "CEP", "País",
            "Telefone Fixo", "Telefone Celular / WhatsApp", "E-mail Corporativo"
        ]
        self.entradas = {}
        for i, campo in enumerate(campos_aba1):
            tk.Label(aba1, text=campo, bg='#FFFFFF', anchor='w').grid(row=i, column=0, sticky='w', padx=5, pady=3)
            entry = tk.Entry(aba1, width=80, bg='#FFFFFF')
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entradas[campo] = entry

        # === ABA 2 ===
        campos_aba2 = ["Nome Completo", "Cargo", "CPF", "RG", "E-mail do responsável", "Telefone do responsável"]
        self.responsavel = {}
        for i, campo in enumerate(campos_aba2):
            tk.Label(aba2, text=campo, bg='#FFFFFF', anchor='w').grid(row=i, column=0, sticky='w', padx=5, pady=3)
            entry = tk.Entry(aba2, width=50, bg='#FFFFFF')
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.responsavel[campo] = entry

        # === ABA 3 ===
        campos_aba3 = ["Usuário administrador", "Nível de acesso permitido"]
        self.acesso = {}
        for i, campo in enumerate(campos_aba3):
            tk.Label(aba3, text=campo, bg='#FFFFFF', anchor='w').grid(row=i, column=0, sticky='w', padx=5, pady=3)
            entry = tk.Entry(aba3, width=50, bg='#FFFFFF')
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.acesso[campo] = entry

        salvar=tk.Button(self, text='SALVAR DADOS', bg="#00008B", fg='white',width=20, font=('Arial', 12, 'bold'))
        salvar.grid(sticky="n")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = RegistroFuncionario(master=root)
    app.mainloop()

    