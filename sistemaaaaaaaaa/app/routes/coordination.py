from flask import Blueprint, render_template, request
from flask_login import login_required
from ..data import schedules, rooms, teachers, classes, DAY_LABELS, SHIFTS

coord_bp = Blueprint("coord", __name__)

@coord_bp.get("")
@login_required
def dashboard():
    selected_day = request.args.get("day", "")
    selected_shift = request.args.get("shift", "")

    items = [item for item in schedules.values() if item.week_start == "2026-09-07"]

    if selected_day:
        items = [item for item in items if item.day == selected_day]
    if selected_shift:
        items = [item for item in items if item.shift == selected_shift]

    return render_template(
        "coordination.html",
        items=items,
        rooms=rooms,
        teachers=teachers,
        classes=classes,
        week_start="2026-09-07",
        day_labels=DAY_LABELS,
        shifts=SHIFTS,
        selected_day=selected_day,
        selected_shift=selected_shift,
    )
