from app.data import add_audit

class AuditService:
    @staticmethod
    def record(user_id, action, entity, entity_id, old="", new="", reason=""):
        add_audit(user_id, action, entity, entity_id, old, new, reason)
