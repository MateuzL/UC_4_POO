from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..data import schedules, classes, rooms, teachers, DAY_LABELS, SHIFTS, validate_schedule

main_bp = Blueprint("main", __name__)

@main_bp.get("/dashboard")
@login_required
def dashboard():
    return redirect(url_for("main.week", date="2026-09-07"))

@main_bp.get("/schedule/week/<date>")
@login_required
def week(date):
    selected_day = request.args.get("day", "")
    selected_shift = request.args.get("shift", "")

    items = [
        item for item in schedules.values()
        if item.week_start == date
        and (current_user.role != "teacher" or item.teacher_id == current_user.teacher_id)
    ]

    if selected_day:
        items = [item for item in items if item.day == selected_day]
    if selected_shift:
        items = [item for item in items if item.shift == selected_shift]

    return render_template(
        "professor_week.html",
        items=items,
        classes=classes,
        rooms=rooms,
        teachers=teachers,
        day_labels=DAY_LABELS,
        shifts=SHIFTS,
        week_start=date,
        selected_day=selected_day,
        selected_shift=selected_shift,
    )

@main_bp.post("/schedule/submit/<int:schedule_id>")
@login_required
def submit_week(schedule_id):
    if current_user.role != "teacher":
        flash("Somente professores podem enviar a própria agenda.", "error")
        return redirect(url_for("main.week", date="2026-09-07"))

    changed = 0
    for item in schedules.values():
        if (
            item.week_start == "2026-09-07"
            and item.teacher_id == current_user.teacher_id
            and item.status == "PENDENTE"
        ):
            item.status = "CONFIRMADA"
            changed += 1

    if changed:
        flash("Agenda semanal enviada e confirmada com sucesso.", "success")
    else:
        flash("Não existem horários pendentes para confirmar.", "info")
    return redirect(url_for("main.week", date="2026-09-07"))
