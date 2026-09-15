from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from flask_login import login_required, current_user
from app.data import schedules, rooms, teachers, classes, matrix, audits, conflicts, current_week, DAYS, SHIFTS, DAY_LABELS, generate_week, Room
from app.services.conflict_service import validate_values, ConflictError, check_swap
from app.services.audit_service import AuditService
import csv, io

coord_bp=Blueprint("coord",__name__,url_prefix="/coordination")

def coord_only():
    return current_user.is_authenticated and current_user.role=="coordination"

@coord_bp.before_request
def guard():
    if not coord_only():
        return redirect(url_for("main.dashboard"))

@coord_bp.get("")
def dashboard():
    ws,_=current_week()
    items=[s for s in schedules.values() if s.week_start==ws]
    return render_template("coordination.html",items=items,rooms=rooms,teachers=teachers,classes=classes,week_start=ws)

@coord_bp.get("/rooms")
def rooms_page():
    return render_template("rooms.html",rooms=rooms)

@coord_bp.post("/rooms")
def create_room():
    name=request.form.get("name","").strip()
    capacity=int(request.form.get("capacity","0"))
    if not name or capacity<=0:
        flash("Informe nome e capacidade válidos.","error")
    else:
        i=max(rooms.keys(),default=0)+1
        rooms[i]=Room(i,name,"Geral",capacity,True)
        AuditService.record(current_user.id,"CRIAR","Room",i,"",name,"Cadastro de sala.")
        flash("Sala cadastrada com sucesso.","success")
    return redirect(url_for("coord.rooms_page"))

@coord_bp.post("/rooms/<int:room_id>/toggle")
def toggle_room(room_id):
    r=rooms[room_id]
    r.active=not r.active
    AuditService.record(current_user.id,"ALTERAR_STATUS","Room",room_id,str(not r.active),str(r.active),"Alteração de status.")
    flash("Status da sala atualizado.","success")
    return redirect(url_for("coord.rooms_page"))

@coord_bp.get("/teachers")
def teachers_page(): return render_template("teachers.html",teachers=teachers)

@coord_bp.get("/classes")
def classes_page(): return render_template("classes.html",classes=classes,teachers=teachers,rooms=rooms)

@coord_bp.get("/matrix")
def matrix_page(): return render_template("matrix.html",matrix=matrix,classes=classes,teachers=teachers,rooms=rooms,day_labels=DAY_LABELS,shifts=SHIFTS)

@coord_bp.get("/conflicts")
def conflicts_page(): return render_template("conflicts.html",conflicts=conflicts)

@coord_bp.get("/audit")
def audit_page(): return render_template("audit.html",audits=audits,users=__import__("app.data",fromlist=["users"]).users)

@coord_bp.get("/reports")
def reports():
    ws,_=current_week()
    items=[s for s in schedules.values() if s.week_start==ws]
    return render_template("reports.html",items=items,rooms=rooms,teachers=teachers,classes=classes)

@coord_bp.get("/reports/csv")
def report_csv():
    ws,_=current_week()
    out=io.StringIO()
    w=csv.writer(out)
    w.writerow(["Dia","Turno","Turma","Professor","Sala","Alunos","Capacidade","Status"])
    for s in schedules.values():
        if s.week_start!=ws: continue
        w.writerow([s.day,s.shift,classes[s.class_id].code,teachers[s.teacher_id].name,rooms[s.room_id].name,
                    classes[s.class_id].students,rooms[s.room_id].capacity,s.status])
    return Response(out.getvalue(),mimetype="text/csv",headers={"Content-Disposition":"attachment; filename=ocupacao_semanal.csv"})

@coord_bp.post("/schedule/<int:sid>/update")
def update_schedule(sid):
    s=schedules[sid]
    try:
        validate_values(int(request.form["teacher_id"]),int(request.form["room_id"]),s.class_id,
                        request.form["day"],request.form["shift"],s.id)
        reason=request.form.get("reason","").strip()
        if not reason: raise ConflictError("Informe o motivo da alteração.")
        old=f"{s.day}/{s.shift}/professor={s.teacher_id}/sala={s.room_id}"
        s.teacher_id=int(request.form["teacher_id"]); s.room_id=int(request.form["room_id"])
        s.day=request.form["day"]; s.shift=request.form["shift"]; s.reason=reason; s.updated_by=current_user.id; s.updated_at=__import__("app.data",fromlist=["now"]).now()
        s.status="ALTERADA_PELA_COORDENACAO" if s.status=="ENVIADA" else s.status
        new=f"{s.day}/{s.shift}/professor={s.teacher_id}/sala={s.room_id}"
        AuditService.record(current_user.id,"ALTERAÇÃO","WeeklySchedule",sid,old,new,reason)
        flash("Agendamento atualizado com sucesso.","success")
    except (ValueError,ConflictError,KeyError) as e: flash(str(e),"error")
    return redirect(url_for("coord.dashboard"))

@coord_bp.post("/schedule/<int:sid>/cancel")
def cancel(sid):
    s=schedules[sid]; reason=request.form.get("reason","").strip()
    if not reason: flash("Informe o motivo do cancelamento.","error")
    else:
        old=s.status; s.status="CANCELADA"; s.reason=reason; s.updated_by=current_user.id
        AuditService.record(current_user.id,"CANCELAMENTO","WeeklySchedule",sid,old,"CANCELADA",reason)
        flash("Horário cancelado com sucesso.","success")
    return redirect(url_for("coord.dashboard"))

@coord_bp.post("/schedule/<int:sid>/reopen")
def reopen(sid):
    s=schedules[sid]; reason=request.form.get("reason","").strip()
    if not reason: flash("Informe o motivo da reabertura.","error")
    else:
        old=s.status; s.status="PENDENTE"; s.reason=reason; s.updated_by=current_user.id
        AuditService.record(current_user.id,"REABERTURA","WeeklySchedule",sid,old,"PENDENTE",reason)
        flash("Semana reaberta com sucesso.","success")
    return redirect(url_for("coord.dashboard"))

@coord_bp.post("/swap-room")
def swap_room():
    a=schedules[int(request.form["a_id"])]; b=schedules[int(request.form["b_id"])]
    reason=request.form.get("reason","").strip()
    try:
        if not reason: raise ConflictError("Informe o motivo da troca.")
        check_swap(a,b)
        a.room_id,b.room_id=b.room_id,a.room_id
        a.updated_by=b.updated_by=current_user.id
        a.status=b.status="ALTERADA_PELA_COORDENACAO"
        AuditService.record(current_user.id,"TROCA_SALA","WeeklySchedule",a.id,"","sala trocada",reason)
        AuditService.record(current_user.id,"TROCA_SALA","WeeklySchedule",b.id,"","sala trocada",reason)
        flash("Salas trocadas com sucesso.","success")
    except (ValueError,ConflictError) as e: flash(str(e),"error")
    return redirect(url_for("coord.dashboard"))

@coord_bp.post("/generate-week")
def generate():
    generate_week()
    flash("Semana gerada a partir da matriz.","success")
    return redirect(url_for("coord.dashboard"))
