from cliente import Cliente
from carro import Carro
from moto import Moto
from caminhonete import Caminhonete
from eletrico import Eletrico
from aluguel import Aluguel


def cadastrar_cliente():
    """
    Solicita os dados do cliente via teclado e retorna
    um objeto Cliente já validado.
    """
    print("\n--- CADASTRO DO CLIENTE ---")

    # Validação simples para aceitar somente número inteiro.
    while True:
        try:
            codigo = int(input("Informe o código do cliente: "))
            break
        except ValueError:
            print("Digite um código numérico válido.")

    # Validação do nome antes de criar o objeto.
    while True:
        nome = input("Informe o nome do cliente: ").strip()

        if len(nome) >= 3:
            break

        print("O nome deve possuir pelo menos três caracteres.")

    # Validação didática do CPF.
    while True:
        cpf = input("Informe o CPF com 11 números: ")

        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            break

        print("CPF inválido. Informe exatamente 11 números.")

    return Cliente(codigo, nome, cpf)


def criar_veiculos():
    """
    Cria os veículos iniciais da locadora.

    Observe que todos os objetos podem ser colocados na mesma lista,
    pois Carro, Moto, Caminhonete e Eletrico são tipos de Veiculo.
    """
    carro1 = Carro(
        1,
        "Chevrolet",
        "Onix",
        180.00,
        4
    )

    carro2 = Carro(
        2,
        "Toyota",
        "Corolla",
        280.00,
        4
    )

    moto1 = Moto(
        3,
        "Honda",
        "CG 160",
        90.00,
        160
    )

    moto2 = Moto(
        4,
        "Yamaha",
        "Fazer 250",
        130.00,
        250
    )

    caminhonete1 = Caminhonete(
        5,
        "Toyota",
        "Hilux",
        350.00,
        1000,
        5,
        True
    )

    eletrico1 = Eletrico(
        6,
        "BYD",
        "Dolphin",
        250.00,
        400,
        8
    )

    return [
        carro1,
        carro2,
        moto1,
        moto2,
        caminhonete1,
        eletrico1
    ]


def listar_veiculos(veiculos):
    """
    Exibe todos os veículos.

    O mesmo método exibir_dados() é chamado para objetos
    de classes diferentes, outro exemplo de polimorfismo.
    """
    print("\n--- VEÍCULOS CADASTRADOS ---")

    for veiculo in veiculos:
        veiculo.exibir_dados()


def buscar_veiculo(veiculos, codigo):
    """Procura um veículo pelo código."""
    for veiculo in veiculos:
        if veiculo.codigo == codigo:
            return veiculo

    return None


def solicitar_quantidade_dias():
    """Solicita uma quantidade de dias válida."""
    while True:
        try:
            quantidade = int(
                input("\nInforme a quantidade de dias da locação: ")
            )

            if quantidade > 0:
                return quantidade

            print("A quantidade deve ser maior que zero.")

        except ValueError:
            print("Digite somente números inteiros.")


def escolher_veiculo(veiculos):
    """
    Permite que o usuário escolha um veículo disponível.
    """
    while True:
        try:
            codigo = int(
                input("\nDigite o código do veículo desejado: ")
            )
        except ValueError:
            print("Digite um código numérico.")
            continue

        veiculo = buscar_veiculo(veiculos, codigo)

        if veiculo is None:
            print("Veículo não encontrado.")
            continue

        if not veiculo.esta_disponivel():
            print("Este veículo não está disponível.")
            continue

        return veiculo


def main():
    """Função principal que coordena toda a execução do sistema."""
    print("====================================")
    print("   SISTEMA DE LOCAÇÃO DE VEÍCULOS")
    print("====================================")

    # 1. Criação do cliente.
    cliente = cadastrar_cliente()

    # 2. Criação dos veículos.
    veiculos = criar_veiculos()

    # 3. Exibição do estoque da locadora.
    listar_veiculos(veiculos)

    # 4. Escolha do veículo.
    veiculo_escolhido = escolher_veiculo(veiculos)

    # 5. Definição do período de locação.
    quantidade_dias = solicitar_quantidade_dias()

    # 6. Criação do objeto que relaciona cliente e veículo.
    aluguel = Aluguel(
        1,
        cliente,
        veiculo_escolhido,
        quantidade_dias
    )

    # 7. Finalização.
    if aluguel.finalizar():
        aluguel.exibir_resumo()

    # 8. Demonstração do novo estado do veículo.
    print("\nSituação atual do veículo:")
    veiculo_escolhido.exibir_dados()


# Esta condição garante que main() só será executada
# quando este arquivo for iniciado diretamente.
if __name__ == "__main__":
    main()
    