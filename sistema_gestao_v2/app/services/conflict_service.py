from app.data import schedules, rooms, classes, teachers, DAYS, SHIFTS

class ConflictError(ValueError):
    pass

def validate_values(teacher_id, room_id, class_id, day, shift, exclude_id=None):
    if day not in DAYS:
        raise ConflictError("Dia inválido.")
    if shift not in SHIFTS:
        raise ConflictError("Turno inválido.")
    room = rooms.get(room_id)
    group = classes.get(class_id)
    if not room or not room.active:
        raise ConflictError("Sala inativa ou inexistente.")
    if not group or not group.active:
        raise ConflictError("Turma inativa ou inexistente.")
    if group.students > room.capacity:
        raise ConflictError(f"Capacidade insuficiente: a turma possui {group.students} alunos e a sala comporta no máximo {room.capacity} alunos.")
    for s in schedules.values():
        if exclude_id and s.id == exclude_id:
            continue
        if s.status == "CANCELADA":
            continue
        if s.day == day and s.shift == shift:
            if s.teacher_id == teacher_id:
                raise ConflictError("Conflito de professor: o professor já possui um agendamento neste dia e turno.")
            if s.room_id == room_id:
                raise ConflictError("Conflito de sala: esta sala já está ocupada neste dia e turno.")
    return True

def check_swap(a, b):
    if a.day != b.day or a.shift != b.shift:
        raise ConflictError("A troca de sala deve ocorrer no mesmo dia e turno.")
    validate_values(a.teacher_id,b.room_id,a.class_id,a.day,a.shift,a.id)
    validate_values(b.teacher_id,a.room_id,b.class_id,b.day,b.shift,b.id)
    return True
