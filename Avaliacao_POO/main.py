from refeicao import Refeicao
from bebida import Bebida
from sobremesa import Sobremesa
from cliente import Cliente
from pedido import Pedido



# CARDÁPIO

refeicao1 = Refeicao(
    1,
    "Feijoada Simples",
    30.00,
    "Normal"
)

refeicao2 = Refeicao(
    2,
    "Feijoada Grande",
    30.00,
    "Grande"
)

bebida1 = Bebida(
    3,
    "Coca-Cola Lata 350ml",
    5.00,
    350
)

bebida2 = Bebida(
    4,
    "Coca-Cola 1L",
    7.00,
    1000
)

sobremesa1 = Sobremesa(
    5,
    "Sorvete Simples",
    10.00,
    False
)

sobremesa2 = Sobremesa(
    6,
    "Sorvete Duplo",
    10.00,
    True
)


produtos = [
    refeicao1,
    refeicao2,
    bebida1,
    bebida2,
    sobremesa1,
    sobremesa2
]




# CADASTRO DO CLIENTE


def cadastrar_cliente():

    print("\n--- CADASTRO DO CLIENTE ---")

    while True:

        nome = input("Digite seu Nome: ")

        if len(nome.strip()) < 3:
            print("\nErro: O nome deve ter pelo menos 3 caracteres.\n")
            continue

        telefone = input("Digite seu Telefone: ")

        if not telefone.isdigit():
            print("ERRO: O telefone deve ser numérico.")
            continue

        if telefone.strip() == "":
            print("\nERRO: O telefone não pode ficar vazio.\n")
            continue

        cliente = Cliente(
            1,
            nome,
            telefone
        )

        print("\nCliente cadastrado com sucesso!")

        return cliente




# CRIAR PEDIDO


def criar_pedido(pedido):

    while True:

        print("\n==============================")
        print("          CARDÁPIO")
        print("==============================")

        for produto in produtos:

            print(f"Código: {produto.codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: R$ {produto.get_preco():.2f}")
            print()
            #print("------------------------------")

        print("0 - Voltar ao menu")

        print("==============================")

        try:
            escolha = int(input("Escolha o código do produto: "))

        except ValueError:

            print("\nDigite apenas números.")
            continue


        # VOLTAR AO MENU

        if escolha == 0:
            break


        # PROCURAR PRODUTO

        produto_escolhido = None

        for produto in produtos:
            if produto.codigo == escolha:
                produto_escolhido = produto
                break

        


        # ADICIONAR PRODUTO

        if produto_escolhido is not None:

            pedido.adicionar_produto(produto_escolhido)

            print(f"\n{produto_escolhido.nome} foi adicionado ao seu pedido!")
            print(f"Valor parcial do pedido: R$ {pedido.calcular_total():.2f}")

        else:
            print("\nProduto não encontrado.")



# FINALIZAR PEDIDO


def finalizar_pedido(pedido):

    if pedido.finalizar():

        print("\nPedido finalizado com sucesso!")

        pedido.exibir_resumo()

        return True

    return False




# MENU PRINCIPAL


def menu(pedido):

    while True:

        print("\n==============================")
        print("===========  MENU  ===========")
        print("==============================")
        print("1 - Criar pedido (Cardápio)")
        print("2 - Finalizar pedido")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")


        # CRIAR PEDIDO

        if opcao == "1":

            criar_pedido(pedido)


        # FINALIZAR PEDIDO

        elif opcao == "2":

            if finalizar_pedido(pedido):
                break


        # SAIR

        elif opcao == "0":

            print("\nSistema encerrado.")
            break


        else:

            print("\nOpção inválida.")



# Início


print("----- SISTEMA RESTAURANTE -----")

cliente = cadastrar_cliente()

pedido = Pedido(
    1,
    cliente
)

menu(pedido)