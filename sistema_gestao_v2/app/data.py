from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

DAYS = ["segunda", "terça", "quarta", "quinta", "sexta"]
DAY_LABELS = dict(zip(DAYS, ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira"]))
SHIFTS = {
    "manhã": "08:00 às 12:00",
    "tarde": "13:00 às 17:00",
    "noite": "18:00 às 22:00",
}
STATUSES = ["PENDENTE", "ENVIADA", "ALTERADA_PELA_COORDENACAO", "CANCELADA"]

@dataclass
class User:
    id: int
    login: str
    password_hash: str
    role: str
    name: str
    active: bool = True
    teacher_id: int | None = None
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@dataclass
class Room:
    id: int
    name: str
    category: str
    capacity: int
    active: bool = True

@dataclass
class Teacher:
    id: int
    name: str
    email: str
    login: str
    active: bool = True

@dataclass
class ClassGroup:
    id: int
    course: str
    code: str
    teacher_id: int
    students: int
    room_id: int
    active: bool = True

@dataclass
class MatrixEntry:
    id: int
    class_id: int
    teacher_id: int
    room_id: int
    day: str
    shift: str
    active: bool = True

@dataclass
class Schedule:
    id: int
    week_start: str
    week_end: str
    class_id: int
    teacher_id: int
    room_id: int
    day: str
    shift: str
    status: str = "PENDENTE"
    matrix_id: int | None = None
    updated_by: int | None = None
    reason: str = ""
    updated_at: str = ""

@dataclass
class AuditLog:
    id: int
    user_id: int
    action: str
    entity: str
    entity_id: int
    old_value: str
    new_value: str
    reason: str
    timestamp: str

users = {}
rooms = {}
teachers = {}
classes = {}
matrix = {}
schedules = {}
audits = {}
conflicts = []

def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def monday_of(value=None):
    d = value or date.today()
    return d - timedelta(days=d.weekday())

def current_week():
    start = monday_of()
    return start.isoformat(), (start + timedelta(days=4)).isoformat()

def add_audit(user_id, action, entity, entity_id, old="", new="", reason=""):
    i = max(audits.keys(), default=0) + 1
    audits[i] = AuditLog(i,user_id,action,entity,entity_id,old,new,reason,now())

def init_demo_data():
    if users:
        return
    rooms.update({
        1: Room(1,"Laboratório de Informática 01","Informática",30),
        2: Room(2,"Laboratório de Informática 02","Informática",30),
        3: Room(3,"Laboratório de Enfermagem 01","Enfermagem",25),
        4: Room(4,"Laboratório de Enfermagem 02","Enfermagem",25),
        5: Room(5,"Laboratório de Estética e Beleza","Estética e Beleza",20),
        6: Room(6,"Sala de Técnico em Administração","Administração",40),
    })
    teachers.update({
        1: Teacher(1,"Ana Paula Souza","ana@instituicao.local","professor1"),
        2: Teacher(2,"Carlos Henrique Lima","carlos@instituicao.local","professor2"),
        3: Teacher(3,"Mariana Alves","mariana@instituicao.local","professor3"),
    })
    users.update({
        1: User(1,"coordenacao",generate_password_hash("coordenacao123"),"coordination","Coordenação"),
        2: User(2,"professor1",generate_password_hash("professor123"),"teacher","Ana Paula Souza",teacher_id=1),
        3: User(3,"professor2",generate_password_hash("professor123"),"teacher","Carlos Henrique Lima",teacher_id=2),
        4: User(4,"professor3",generate_password_hash("professor123"),"teacher","Mariana Alves",teacher_id=3),
    })
    classes.update({
        1: ClassGroup(1,"Técnico em Administração","ADM-01",1,32,6),
        2: ClassGroup(2,"Técnico em Informática","INF-01",28,1,2),
        3: ClassGroup(3,"Técnico em Enfermagem","ENF-01",22,3,3),
    })
    # corrected demo class for INF-01
    classes[2] = ClassGroup(2,"Técnico em Informática","INF-01",2,28,1)
    matrix.update({
        1: MatrixEntry(1,1,1,6,"segunda","tarde"),
        2: MatrixEntry(2,2,2,1,"segunda","manhã"),
        3: MatrixEntry(3,3,3,3,"terça","noite"),
        4: MatrixEntry(4,2,2,1,"quarta","tarde"),
        5: MatrixEntry(5,1,1,6,"quinta","manhã"),
    })
    generate_week()

def generate_week(week_start=None):
    ws = week_start or current_week()[0]
    we = (date.fromisoformat(ws) + timedelta(days=4)).isoformat()
    # regenerate only if this week does not exist
    if any(s.week_start == ws for s in schedules.values()):
        return
    next_id = max(schedules.keys(), default=0) + 1
    for m in matrix.values():
        if not m.active:
            continue
        schedules[next_id] = Schedule(next_id,ws,we,m.class_id,m.teacher_id,m.room_id,m.day,m.shift,
                                      "PENDENTE",m.id,None,"",now())
        next_id += 1
