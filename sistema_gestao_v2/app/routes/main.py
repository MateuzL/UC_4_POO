from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.data import schedules, classes, rooms, teachers, DAYS, DAY_LABELS, SHIFTS, current_week, generate_week
from app.services.weekly_cycle_service import WeeklyCycleService

main_bp = Blueprint("main", __name__)

def teacher_items():
    ws,_ = current_week()
    generate_week(ws)
    return [s for s in schedules.values() if s.week_start == ws and s.teacher_id == current_user.teacher_id]

@main_bp.get("/")
def index():
    return redirect(url_for("main.dashboard"))

@main_bp.get("/dashboard")
@login_required
def dashboard():
    ws,_=current_week()
    items = teacher_items() if current_user.role=="teacher" else [s for s in schedules.values() if s.week_start==ws]
    return render_template("dashboard.html", items=items, classes=classes, rooms=rooms, teachers=teachers, week_start=ws)

@main_bp.get("/schedule/week/<date>")
@login_required
def week(date):
    items = [s for s in schedules.values() if s.week_start == date]
    if current_user.role=="teacher":
        items=[s for s in items if s.teacher_id==current_user.teacher_id]
    return render_template("professor_week.html", items=items, classes=classes, rooms=rooms, teachers=teachers,
                           day_labels=DAY_LABELS, shifts=SHIFTS, week_start=date)

@main_bp.post("/schedule/<int:schedule_id>/submit-week")
@login_required
def submit_week(schedule_id):
    if current_user.role!="teacher":
        return redirect(url_for("main.dashboard"))
    s=schedules.get(schedule_id)
    try:
        WeeklyCycleService.submit_teacher_week(current_user.teacher_id,s.week_start,current_user.id)
        flash("Semana enviada com sucesso. A agenda agora está bloqueada para alterações pelo professor.","success")
    except ValueError as e:
        flash(str(e),"error")
    return redirect(url_for("main.week",date=s.week_start))
