from paciente import Paciente
from medico import Medico
from consulta import Consulta

def main():
    paciente1 = Paciente(
        1,
        "Marcos",
        "123.456.789-00",
        "20 anos"
    )
    medico1 = Medico(
        1,
        "Dr. Marcelo",
        "CRM-MS 99988",
        "Cardiologista"
    )

    consulta1 = Consulta(
        1001,
        paciente1,
        medico1,
        "29/07/2026",
        "20:00"
    )

    paciente1.exibir_dados()
    medico1.exibir_dados()
    consulta1.exibir_dados()

    print("--- CONFIRMANDO CONSULTA ---")
    consulta1.confirmar_consulta()

    consulta1.exibir_dados()
    medico1.exibir_dados()

    print("--- REALIZANDO CONSULTA ---")
    consulta1.realizar_consulta()
    consulta1.exibir_dados()

    medico1.exibir_dados()

    paciente1.desativar()
    consulta1.confirmar_consulta()

    medico1.alterar_disponibilidade()
    consulta1.confirmar_consulta()


    #medico1.exibir_dados()
    #paciente1.exibir_dados()


if __name__ == "__main__":
    main()
    