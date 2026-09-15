from dataclasses import dataclass
from flask_login import UserMixin

@dataclass
class User(UserMixin):
    id: int
    username: str
    password: str
    role: str
    teacher_id: int | None = None

@dataclass
class Teacher:
    id: int
    name: str

@dataclass
class Room:
    id: int
    name: str
    capacity: int
    active: bool = True

@dataclass
class ClassGroup:
    id: int
    course: str
    code: str
    teacher_id: int
    students: int
    room_id: int

@dataclass
class Schedule:
    id: int
    week_start: str
    day: str
    shift: str
    teacher_id: int
    class_id: int
    room_id: int
    status: str = "PENDENTE"

users = {
    1: User(1, "coordenacao", "coordenacao123", "coord"),
    2: User(2, "professor1", "professor123", "teacher", 1),
    3: User(3, "professor2", "professor123", "teacher", 2),
    4: User(4, "professor3", "professor123", "teacher", 3),
}

teachers = {
    1: Teacher(1, "Ana Paula Souza"),
    2: Teacher(2, "Carlos Henrique Lima"),
    3: Teacher(3, "Mariana Alves"),
}

rooms = {
    1: Room(1, "Sala de Informática", 30),
    2: Room(2, "Sala ADM", 35),
    3: Room(3, "Laboratório de Enfermagem", 25),
    4: Room(4, "Sala Multimídia", 40),
    5: Room(5, "Sala 05", 30),
    6: Room(6, "Sala 06", 25),
}

classes = {
    1: ClassGroup(1, "Técnico em Administração", "ADM-01", 1, 32, 2),
    2: ClassGroup(2, "Técnico em Informática", "INF-01", 2, 28, 1),
    3: ClassGroup(3, "Técnico em Enfermagem", "ENF-01", 3, 22, 3),
    4: ClassGroup(4, "Técnico em Informática", "INF-02", 1, 26, 4),
    5: ClassGroup(5, "Técnico em Administração", "ADM-02", 2, 30, 5),
    6: ClassGroup(6, "Técnico em Enfermagem", "ENF-02", 3, 20, 6),
}

DAY_LABELS = {
    "segunda": "Segunda-feira",
    "terça": "Terça-feira",
    "quarta": "Quarta-feira",
    "quinta": "Quinta-feira",
    "sexta": "Sexta-feira",
}

SHIFTS = {
    "manhã": "08:00 – 12:00",
    "tarde": "13:00 – 17:00",
    "noite": "18:00 – 22:00",
}

# Dados de demonstração para a semana 07/09/2026.
schedules = {}
_demo = [
    ("segunda", "manhã", 2, 2, 1),
    ("segunda", "tarde", 1, 1, 2),
    ("terça", "manhã", 1, 4, 4),
    ("terça", "noite", 3, 3, 3),
    ("quarta", "tarde", 2, 5, 5),
    ("quarta", "noite", 3, 6, 6),
    ("quinta", "manhã", 1, 1, 2),
    ("quinta", "tarde", 2, 2, 1),
    ("sexta", "manhã", 3, 3, 3),
    ("sexta", "tarde", 1, 4, 4),
]
for idx, (day, shift, teacher_id, class_id, room_id) in enumerate(_demo, 1):
    schedules[idx] = Schedule(
        idx, "2026-09-07", day, shift, teacher_id, class_id, room_id
    )

# Conflitos NÃO possuem uma aba própria. As regras são usadas durante o agendamento.
def validate_schedule(teacher_id, class_id, room_id, day, shift, ignore_id=None):
    errors = []
    turma = classes.get(class_id)
    sala = rooms.get(room_id)

    if not turma:
        errors.append("Turma inválida.")
    if not sala or not sala.active:
        errors.append("Sala inexistente ou inativa.")
    elif turma and turma.students > sala.capacity:
        errors.append(
            f"A sala comporta {sala.capacity} alunos, mas a turma possui {turma.students}."
        )

    for item in schedules.values():
        if ignore_id is not None and item.id == ignore_id:
            continue
        if item.week_start != "2026-09-07" or item.day != day or item.shift != shift:
            continue
        if item.teacher_id == teacher_id:
            errors.append("O professor já possui uma agenda neste dia e turno.")
        if item.room_id == room_id:
            errors.append("A sala já está ocupada neste dia e turno.")
        if item.class_id == class_id:
            errors.append("A turma já possui uma agenda neste dia e turno.")
    return errors
