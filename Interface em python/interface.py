#Importando a Biblioteca
import tkinter as tk   

def mostrar_nome():
    nome = entrada_nome.get()
    resultado.config(
        text=f"Olá {nome}"
    )

#Cria a janela principal
janela = tk.Tk()

#Definir o título exibido na barra superior
janela.title("Minha primeira janela")

#Definir o tamanho da janela
janela.geometry("500x400")

janela.config(bg="green")

#Criar um texto dentro da janela
'''titulo = tk.Label(
    janela,
    text="Sistema de Locação de Veículos",
    font=("Arial", 18)
)'''

tk.Label(
    janela,
    font=("Arial", 18, "bold"), bg="black", fg="white",
    text="Digite o seu nome: "
).pack(pady=10)

'''def mensagem():
    print("Botão Clicado!!!")

#Adicionando um botão
botao = tk.Button(
    janela,
    text="Clique aqui",
    command=mensagem
)'''

'''tk.Button(
    janela,
    text="Confirmar",
    command=mostrar_nome
).pack(pady=15)'''

#Campo de entrada
entrada_nome = tk.Entry(
    janela,
    width=40
)

entrada_nome.pack()

tk.Button(
    janela,
    text="Confirmar",
    command=mostrar_nome
).pack(pady=15)

resultado = tk.Label(
    janela,
    bg="green", 
    text=""
)

resultado.pack()

#Exibe o componente na janela
'''titulo.pack(pady=30)
botao.pack(pady=20)'''


#Mantém a janela aberta
janela.mainloop()
