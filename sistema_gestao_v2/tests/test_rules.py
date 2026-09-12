import pytest
from app.data import rooms, classes, schedules, init_demo_data
from app.services.conflict_service import validate_values, ConflictError

def setup_module():
    init_demo_data()

def test_invalid_shift_rejected():
    with pytest.raises(ConflictError):
        validate_values(1,6,1,"segunda","09:30")

def test_invalid_day_rejected():
    with pytest.raises(ConflictError):
        validate_values(1,6,1,"sábado","manhã")

def test_capacity_rejected():
    with pytest.raises(ConflictError):
        validate_values(1,5,1,"sexta","manhã")

def test_room_conflict():
    s=next(iter(schedules.values()))
    with pytest.raises(ConflictError):
        validate_values(2,s.room_id,s.class_id,s.day,s.shift,s.id)

def test_teacher_conflict():
    s=next(iter(schedules.values()))
    with pytest.raises(ConflictError):
        validate_values(s.teacher_id,2,2,s.day,s.shift,s.id)
