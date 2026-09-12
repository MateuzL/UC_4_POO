# Sistema de Gestão de Salas V2

Sistema Flask demonstrativo, sem banco de dados nesta etapa.

## Atualizações desta versão

- Visualização semanal completa para Coordenação.
- Visualização semanal individual para cada Professor.
- Filtro por dia da semana.
- Filtro por turno/horário:
  - Manhã: 08:00–12:00
  - Tarde: 13:00–17:00
  - Noite: 18:00–22:00
- Ao enviar a agenda semanal, os horários pendentes do professor passam imediatamente para `CONFIRMADA`.
- 3 professores demo.
- 6 turmas demo.
- 6 salas demo.
- Não existe aba "Conflitos".
- As validações de conflito ficam no fluxo de agendamento/alteração.

## Contas

Coordenação:
`coordenacao` / `coordenacao123`

Professor 1:
`professor1` / `professor123`

Professor 2:
`professor2` / `professor123`

Professor 3:
`professor3` / `professor123`

## Instalação

No PowerShell, dentro da pasta do projeto:

```powershell
& "C:\Program Files\Python314\python.exe" -m pip install -r requirements.txt
& "C:\Program Files\Python314\python.exe" run.py
```

Acesse `http://127.0.0.1:5000`.

## Observação

Os dados são mantidos em memória e são reiniciados quando a aplicação é reiniciada. A integração com SQLite/SQLAlchemy pode ser feita posteriormente sem alterar a proposta da interface.
