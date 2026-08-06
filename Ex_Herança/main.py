from paciente import Paciente
from medico import Medico

paciente1 = Paciente(
    "Luiz",
    "123.456.789-00",
    "(67)99988-0011",
    "America",
    20,
    "Unimed"
)

medico1 = Medico(
    "João",
    "111.222.333-00",
    "(67)98787-9923",
    "Frei Mariano",
    "01020304",
    "Clínico Geral"
)

print("--- PACIENTE ---")
paciente1.exibir_paciente()

print("--- MEDICO ---")
medico1.exibir_medico()