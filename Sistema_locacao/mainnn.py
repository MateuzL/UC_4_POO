from cliente import Cliente
from carro import Carro
from moto import Moto
from aluguel import Aluguel

def cadastrar_cliente():
    print("\n--- CADASTRO DO CLIENTE ---")

    while True:
        try:
            codigo = int(input("Informe o codigo do cliente: "))
            break
        except ValueError:
            print("Digite um código numérico.")
        
    while True:
        nome = input("Informe o nome do cliente: ")
        if len(nome.strip()) >= 3:
            break
        print("O nome deve possuir pelo menos três caracteres.")
    
    while True:
        cpf = input("Informe o CPF com 11 numeros: ")
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            break
        print("Cpf inválido. Informe exatamente os 11 numeros.")
    
    return Cliente(codigo, nome, cpf)

def cadastrar_veiculos():
    carro1 = Carro(
        1,
        "Volskvagem",
        "Fusca",
        300.00,
        2
    )
    carro2 = Carro(
        2,
        "Fiat",
        "Uno",
        100.00,
        4
    )
    moto1 = Moto(
        3,
        "Honda",
        "Cg 160",
        50.00,
        160
    )
    moto2 = Moto(
        4,
        "Kawasaki",
        "Rh2",
        250.00,
        850
    )

    return [carro1, carro2, moto1, moto2]

def listar_veiculos(veiculos):
    print("\n--- VEICULOS CADSATRADOS ---")
    for veiculo in veiculos:
        print("\n-----------")
        veiculo.exibir_dados()

def buscar_veiculos(veiculos, codigo):
    for veiculo in veiculos:
        if veiculo.codigo == codigo:
            return veiculo
    return None

def solicitar_quantidade_dias():
    while True:
        try:
            quantidade = int(input("Informe a quantidade de dias: "))
            if quantidade > 0:
                return quantidade
            print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Digite somente numeros inteiros.")

def main():
    print("\n--- SISTEMA DE LOCAÇÃO ---")
    cliente = cadastrar_cliente()
    veiculos = cadastrar_veiculos()
    listar_veiculos(veiculos)
    
    while True:
        try:
            codigo_veiculo = int(input("\nDigite o código do veiculo desejado: "))
        except ValueError:
            print("Digite um código numérico.")
            continue

        veiculo_escolhido = buscar_veiculos(veiculos, codigo_veiculo)

        if veiculo_escolhido is None:
            print("Veiculo não encontrado.")
            continue
        if not veiculo_escolhido.esta_disponivel():
            print("Este veiculo não está disponivel.")
            continue
        break
    
    quantidade_dias = solicitar_quantidade_dias()

    aluguel = Aluguel(
        1,
        cliente,
        veiculo_escolhido,
        quantidade_dias
    )

    if aluguel.finalizar():
        aluguel.exibir_resumo()
    
    print("\nSituação atual do veiculo:")
    veiculo_escolhido.exibir_dados()

if __name__ == "__main__":
    main()