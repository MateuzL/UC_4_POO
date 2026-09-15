from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from ..data import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = next(
            (u for u in users.values()
             if u.username == username and u.password == password),
            None,
        )
        if user:
            login_user(user)
            if user.role == "coord":
                return redirect(url_for("coord.dashboard"))
            return redirect(url_for("main.week", date="2026-09-07"))
        flash("Usuário ou senha inválidos.", "error")
    return render_template("login.html")

@auth_bp.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
