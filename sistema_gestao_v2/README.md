# Sistema Web de Gestão e Reserva de Salas — V2

Aplicação Flask responsiva para gestão acadêmica de salas, professores, turmas,
matriz e agenda semanal.

## Observação sobre esta versão

Esta entrega contém a aplicação funcional com persistência em memória durante a execução.
O banco SQLite/SQLAlchemy foi deliberadamente deixado para uma etapa posterior,
conforme solicitado. Assim, os dados demo são recriados ao iniciar a aplicação.

## Requisitos

- Python 3.10+
- pip

## Instalação

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python run.py
```

Acesse: http://127.0.0.1:5000

## Usuários demo

- Coordenação: `coordenacao` / `coordenacao123`
- Professor 1: `professor1` / `professor123`
- Professor 2: `professor2` / `professor123`

As senhas são armazenadas como hash no estado da aplicação.

## Regras implementadas nesta etapa

- 6 salas fixas.
- Segunda a sexta.
- Turnos fixos: manhã, tarde e noite.
- Conflito de professor por dia + turno.
- Conflito de sala por dia + turno.
- Validação de capacidade.
- Sala/turma inativa não pode ser utilizada.
- Professor envia a semana inteira.
- Semana enviada fica bloqueada para professor.
- Coordenação pode alterar/cancelar/reabrir.
- Alterações da coordenação exigem motivo.
- Histórico de auditoria em memória.
- Matriz separada da agenda semanal.
- Nova semana pode ser gerada a partir da matriz.

## Estrutura

```text
app/
  __init__.py
  data.py
  services/
    conflict_service.py
    weekly_cycle_service.py
    audit_service.py
  routes/
    auth.py
    main.py
    coordination.py
  templates/
    base.html
    login.html
    dashboard.html
    professor_week.html
    coordination.html
    rooms.html
    teachers.html
    classes.html
    matrix.html
    conflicts.html
    audit.html
  static/
    css/style.css
tests/
  test_rules.py
```

## Próxima etapa

Implementar SQLAlchemy + SQLite, migrations, repositórios e persistência definitiva,
sem alterar as regras de negócio já definidas.
