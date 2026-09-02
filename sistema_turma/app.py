from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "senac-apresentacao-2026"

usuarios = [
    {"id": 1, "nome": "Administrador", "email": "admin@escola.com", "senha": "1234", "tipo": "coordenador"},
    {"id": 2, "nome": "Professor Demo", "email": "professor@escola.com", "senha": "1234", "tipo": "professor"},
]

salas = [
    {"id": 1, "numero": "Sala 01", "capacidade": 30, "localizacao": "Bloco A", "disponivel": True},
    {"id": 2, "numero": "Sala 02", "capacidade": 40, "localizacao": "Bloco A", "disponivel": False},
    {"id": 3, "numero": "Sala 03", "capacidade": 25, "localizacao": "Bloco B", "disponivel": True},
    {"id": 4, "numero": "Laboratório 01", "capacidade": 35, "localizacao": "Bloco B", "disponivel": True},
    {"id": 5, "numero": "MULTIUSO 01", "capacidade": 45, "localizacao": "Bloco C", "disponivel": True},
    {"id": 6, "numero": "MULTIUSO 02", "capacidade": 45, "localizacao": "Bloco C", "disponivel": True},
]

turmas = [
    {"id": 1, "nome": "INFOR 01", "curso": "Técnico em Desenvolvimento de Sistemas", "quantidade_alunos": 30, "turno": "Matutino", "sala": "Sala 01"},
    {"id": 2, "nome": "INFOR 02", "curso": "Técnico em Desenvolvimento de Sistemas", "quantidade_alunos": 32, "turno": "Vespertino", "sala": "Sala 02"},
    {"id": 3, "nome": "APREND. T1/26", "curso": "Aprendizagem Profissional", "quantidade_alunos": 28, "turno": "Matutino", "sala": "Sala 03"},
    {"id": 4, "nome": "APREND. T2/26", "curso": "Aprendizagem Profissional", "quantidade_alunos": 26, "turno": "Vespertino", "sala": "Laboratório 01"},
    {"id": 5, "nome": "T.ADMINISTRAÇÃO", "curso": "Técnico em Administração", "quantidade_alunos": 30, "turno": "Noturno", "sala": "MULTIUSO 01"},
    {"id": 6, "nome": "A.NEONATOLOGIA", "curso": "Aperfeiçoamento em Neonatologia", "quantidade_alunos": 25, "turno": "Noturno", "sala": "MULTIUSO 02"},
]

reservas = [
    {"id": 1, "professor": "Professor Demo", "sala": "Sala 01", "turma": "INFOR 01", "data": "02/09/2026", "horario": "08:00 - 10:00", "status": "Confirmada"},
    {"id": 2, "professor": "Professor Demo", "sala": "Sala 02", "turma": "INFOR 02", "data": "02/09/2026", "horario": "14:00 - 16:00", "status": "Confirmada"},
    {"id": 3, "professor": "Professor Demo", "sala": "MULTIUSO 01", "turma": "T.ADMINISTRAÇÃO", "data": "02/09/2026", "horario": "19:00 - 21:00", "status": "Pendente"},
]

def logado():
    return "usuario_id" in session

def proximo_id(lista):
    return max((x["id"] for x in lista), default=0) + 1

@app.context_processor
def dados_globais():
    return {"salas": salas, "turmas": turmas, "reservas": reservas}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "")
        usuario = next((u for u in usuarios if u["email"] == email and u["senha"] == senha), None)
        if usuario:
            session["usuario_id"] = usuario["id"]
            session["nome"] = usuario["nome"]
            session["tipo"] = usuario["tipo"]
            return redirect(url_for("dashboard"))
        return render_template("login.html", erro="E-mail ou senha incorretos.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if not logado():
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/salas")
def consultar_salas():
    if not logado():
        return redirect(url_for("login"))
    return render_template("salas.html")

@app.route("/salas/cadastrar", methods=["POST"])
def cadastrar_sala():
    if not logado():
        return redirect(url_for("login"))
    try:
        capacidade = int(request.form.get("capacidade", 0))
    except ValueError:
        capacidade = 0
    salas.append({
        "id": proximo_id(salas),
        "numero": request.form.get("numero", "").strip(),
        "capacidade": capacidade,
        "localizacao": request.form.get("localizacao", "").strip(),
        "disponivel": request.form.get("disponivel") == "true",
    })
    flash("Sala cadastrada com sucesso!", "success")
    return redirect(url_for("consultar_salas"))

@app.route("/salas/editar/<int:id>", methods=["POST"])
def editar_sala(id):
    if not logado():
        return redirect(url_for("login"))
    sala = next((s for s in salas if s["id"] == id), None)
    if sala:
        sala["numero"] = request.form.get("numero", "").strip()
        sala["capacidade"] = int(request.form.get("capacidade", 0))
        sala["localizacao"] = request.form.get("localizacao", "").strip()
        sala["disponivel"] = request.form.get("disponivel") == "true"
        flash("Sala alterada com sucesso!", "success")
    return redirect(url_for("consultar_salas"))

@app.route("/salas/excluir/<int:id>", methods=["POST"])
def excluir_sala(id):
    if not logado():
        return redirect(url_for("login"))
    global salas
    sala = next((s for s in salas if s["id"] == id), None)
    if sala:
        salas = [s for s in salas if s["id"] != id]
        flash("Sala excluída com sucesso!", "success")
    return redirect(url_for("consultar_salas"))

@app.route("/turmas")
def consultar_turmas():
    if not logado():
        return redirect(url_for("login"))
    return render_template("turmas.html")

@app.route("/turmas/cadastrar", methods=["POST"])
def cadastrar_turma():
    if not logado():
        return redirect(url_for("login"))
    turmas.append({
        "id": proximo_id(turmas),
        "nome": request.form.get("nome", "").strip(),
        "curso": request.form.get("curso", "").strip(),
        "quantidade_alunos": int(request.form.get("quantidade_alunos", 0)),
        "turno": request.form.get("turno", ""),
        "sala": request.form.get("sala", ""),
    })
    flash("Turma cadastrada com sucesso!", "success")
    return redirect(url_for("consultar_turmas"))

@app.route("/turmas/editar/<int:id>", methods=["POST"])
def editar_turma(id):
    if not logado():
        return redirect(url_for("login"))
    turma = next((t for t in turmas if t["id"] == id), None)
    if turma:
        turma["nome"] = request.form.get("nome", "").strip()
        turma["curso"] = request.form.get("curso", "").strip()
        turma["quantidade_alunos"] = int(request.form.get("quantidade_alunos", 0))
        turma["turno"] = request.form.get("turno", "")
        turma["sala"] = request.form.get("sala", "")
        flash("Turma alterada com sucesso!", "success")
    return redirect(url_for("consultar_turmas"))

@app.route("/turmas/excluir/<int:id>", methods=["POST"])
def excluir_turma(id):
    if not logado():
        return redirect(url_for("login"))
    global turmas
    turmas = [t for t in turmas if t["id"] != id]
    flash("Turma excluída com sucesso!", "success")
    return redirect(url_for("consultar_turmas"))

@app.route("/reservas")
def consultar_reservas():
    if not logado():
        return redirect(url_for("login"))
    return render_template("reservas.html")

@app.route("/professores")
def consultar_professores():
    if not logado():
        return redirect(url_for("login"))
    professores = [u for u in usuarios if u["tipo"] == "professor"]
    return render_template("professores.html", professores=professores)

@app.route("/reservas/cadastrar", methods=["POST"])
def cadastrar_reserva():
    if not logado():
        return redirect(url_for("login"))
    reservas.append({
        "id": proximo_id(reservas),
        "professor": session.get("nome"),
        "sala": request.form.get("sala", ""),
        "turma": request.form.get("turma", ""),
        "data": request.form.get("data", ""),
        "horario": request.form.get("horario", ""),
        "status": "Pendente",
    })
    flash("Solicitação de reserva enviada!", "success")
    return redirect(url_for("consultar_reservas"))

@app.route("/reservas/excluir/<int:id>", methods=["POST"])
def cancelar_reserva(id):
    if not logado():
        return redirect(url_for("login"))
    global reservas
    reservas = [r for r in reservas if r["id"] != id]
    flash("Reserva cancelada.", "success")
    return redirect(url_for("consultar_reservas"))

if __name__ == "__main__":
    app.run(debug=True)
