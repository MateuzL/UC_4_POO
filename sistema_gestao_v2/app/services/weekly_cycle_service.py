from app.data import generate_week, schedules
from app.services.audit_service import AuditService

class WeeklyCycleService:
    @staticmethod
    def ensure_week(week_start=None):
        generate_week(week_start)

    @staticmethod
    def validate_teacher_week(teacher_id, week_start):
        return [s for s in schedules.values() if s.teacher_id == teacher_id and s.week_start == week_start and s.status != "CANCELADA"]

    @staticmethod
    def submit_teacher_week(teacher_id, week_start, user_id):
        items = WeeklyCycleService.validate_teacher_week(teacher_id, week_start)
        if not items:
            raise ValueError("Nenhum horário encontrado para esta semana.")
        for s in items:
            s.status = "ENVIADA"
            s.updated_by = user_id
        AuditService.record(user_id,"ENVIO_SEMANA","WeeklySchedule",items[0].id,"","ENVIADA","Semana enviada pelo professor.")
