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

bebida1 =  Bebida(
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



print(" ----- SISTEMA RESTAURANTE ----- ")

print("\n--- CADASTRO DO CLIENTE ---")

while True:

    #try:
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")

        cliente = Cliente(
            1,
            nome,
            telefone
        )

        print("\nCliente cadastrado com sucesso!")
        break

    #except ValueError as erro:
        #print(f"\nErro: {erro}")
        #print("Digite os dados novamente.\n")



# CRIAÇÃO DO PEDIDO


pedido = Pedido(
    1,
    cliente
)



# ESCOLHA DOS PRODUTOS


while True:

    print("\n==============================")
    print("          CARDÁPIO")
    print("==============================")

    for produto in produtos:
        print(
            f"{produto.codigo} - "
            f"{produto.nome} - "
            f"R$ {produto.get_preco():.2f}"
        )

    print("0 - Finalizar pedido")

    print("==============================")

    try:
        escolha = int(input("Escolha o código do produto: "))

    except ValueError:
        print("Digite apenas números.")
        continue


    
    # FINALIZAR PEDIDO
    

    if escolha == 0:

        if len(pedido.produtos) == 0:
            print("\nVocê ainda não escolheu nenhum produto.")
            continue

        pedido.finalizar()

        print("\nPedido finalizado com sucesso!")

        pedido.exibir_resumo()

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

        print(
            f"\n{produto_escolhido.nome} "
            f"foi adicionado ao seu pedido!"
        )

    else:

        print("\nProduto não encontrado.")