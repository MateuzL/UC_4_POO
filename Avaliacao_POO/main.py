from produto import Produto
from refeicao import Refeicao
from bebida import Bebida
from sobremesa import Sobremesa
from cliente import Cliente

def main():
    cliente1 = Cliente(
        1,
        "Mateus",
        "(11)95816-1406"
    )

    refeicao1 = Refeicao(
        1,
        "Feijoada",
        30.00,
        "Normal"
    )

    refeicao2 = Refeicao(
        2,
        "Feijoada",
        36.00,
        "Grande"
    )

    bebida1 =  Bebida(
        1,
        "Coca-Cola",
        5.00,
        "350 ml"
    )

    bebida2 = Bebida(
        2,
        "Coca-Cola",
        8.00,
        "1L"
    )

    sobremesa1 = Sobremesa(
        1,
        "Sorvete",
        10.00,
        "Normal"
    )

    sobremesa2 = Sobremesa(
        2,
        "Sorvete",
        11.50,
        "Especial"
    )

    cliente1.exibir_dados()
    refeicao1.exibir_dados()
    refeicao2.exibir_dados()
    bebida1.exibir_dados()
    bebida2.exibir_dados()
    sobremesa1.exibir_dados()
    sobremesa2.exibir_dados()
main()