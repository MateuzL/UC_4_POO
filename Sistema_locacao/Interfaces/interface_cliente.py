import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import messagebox
from cliente import Cliente

clientes = []

def cadastrar_cliente():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()

    if nome.strip() == "":
        messagebox.showerror(
            "Erro",
            "Informe o nome do cliente."
        )
        return

    if cpf.strip() == "":
        messagebox.showerror(
            "Erro",
            "Informa o CPF."
        )
        return

    codigo = len(clientes) + 1

    cliente = Cliente(
        codigo,
        nome,
        cpf
    )

    clientes.append(cliente)

    messagebox.showinfo(
        "Cadastro",
        f"Cliente {cliente.get_nome()} cadastrado!"
    )

    entrada_nome.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)


janela = tk.Tk()
janela.title("Sistema de Locação de Veículos")
janela.geometry("800x500")
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18)
)

titulo.pack(pady=20)

tk.Label(
    janela,
    text="Nome:"
).pack()

entrada_nome = tk.Entry(
    janela,
    width=40
)

entrada_nome.pack(
    pady=5
)

tk.Label(
    janela,
    text="CPF:"
).pack()

entrada_cpf = tk.Entry(
    janela,
    width=40
)

entrada_cpf.pack(
    pady=5
)

botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar Cliente",
    command=cadastrar_cliente,
    width=25
)

botao_cadastrar.pack(pady=20)

botao_sair = tk.Button(
    janela,
    text="Sair",
    command=janela.destroy,
    width=25
)

botao_sair.pack(pady=5)

janela.mainloop()
