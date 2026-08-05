from funcionario import Funcionario

funcionario1 = Funcionario(
    12345,
    "José",
    "Auxiliar Administrativo",
    1000
)

funcionario1.exibir_dados()

print("\n Tentando altear o salário para negativo")
funcionario1.set_salario(10001)

funcionario1.exibir_dados()