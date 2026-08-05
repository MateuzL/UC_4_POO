from paciente import Paciente

paciente1 = Paciente(
    1,
    "Luiz",
    '12345678900',
    20 
)

print(f"\n Alterando nome para vazio")
paciente1.set_nome("Maria")

print(f"\n Alterando cpf para vazio")
paciente1.set_cpf("999.999.999-00")

print("\n Alterando IDADE")
paciente1.set_idade(29)

paciente1.exibir_dados()
