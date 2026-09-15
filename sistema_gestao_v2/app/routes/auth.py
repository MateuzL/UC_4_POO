from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.data import users, User
from app import login_manager

auth_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    u = users.get(int(user_id))
    if not u:
        return None
    class LoginUser:
        def __init__(self, data):
            self.data=data
            self.id=data.id
            self.role=data.role
            self.teacher_id=data.teacher_id
            self.name=data.name
        @property
        def is_authenticated(self): return True
        @property
        def is_active(self): return self.data.active
        @property
        def is_anonymous(self): return False
        def get_id(self): return str(self.id)
    return LoginUser(u)

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        login = request.form.get("login","").strip()
        password = request.form.get("password","")
        u = next((x for x in users.values() if x.login == login and x.active), None)
        if not u or not u.check_password(password):
            flash("Login ou senha inválidos.","error")
            return render_template("login.html")
        login_user(load_user(u.id))
        return redirect(url_for("main.dashboard"))
    return render_template("login.html")

@auth_bp.post("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
