SISTEMA ESCOLAR - PYTHON POO

Estrutura:
- pessoa.py       -> classe base Pessoa
- aluno.py        -> classe Aluno, herda de Pessoa
- professor.py    -> classe Professor, herda de Pessoa
- escola.py       -> classe Escola
- main.py         -> programa principal

Conceitos utilizados:
1. Orientação a objetos
2. Herança
3. Encapsulamento
4. Getters e Setters
5. Métodos
6. Regras de negócio

REGRAS DE NEGÓCIO:
1. As notas do aluno devem estar entre 0 e 10.
2. O aluno precisa ter média maior ou igual a 6 para ser aprovado.

COMO EXECUTAR:
1. Extraia o arquivo ZIP.
2. Abra a pasta no VS Code ou outro editor.
3. Execute:
   python main.py

HERANÇA:
Pessoa
  ├── Aluno
  └── Professor

ENCAPSULAMENTO:
Os atributos principais foram definidos como privados usando __.
O acesso é feito por getters e setters.
