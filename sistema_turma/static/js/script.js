function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    if (sidebar) sidebar.classList.toggle("open");
}

function mostrarAviso(event) {
    event.preventDefault();
    alert("Configurações: módulo demonstrativo para a apresentação.");
}

function abrirModal(id) {
    const modal = document.getElementById(id);
    if (modal) modal.classList.add("show");
}
function fecharModal(id = "modalSala") {
    const modal = document.getElementById(id);
    if (modal) modal.classList.remove("show");
}
function abrirModalSala() {
    const form = document.getElementById("formSala");
    document.getElementById("tituloModal").textContent = "Nova sala";
    form.action = "/salas/cadastrar";
    form.reset();
    abrirModal("modalSala");
}
function editarSala(id, numero, capacidade, localizacao, disponivel) {
    document.getElementById("tituloModal").textContent = "Editar sala";
    document.getElementById("formSala").action = "/salas/editar/" + id;
    document.getElementById("numero").value = numero;
    document.getElementById("capacidade").value = capacidade;
    document.getElementById("localizacao").value = localizacao;
    document.getElementById("disponivel").value = disponivel ? "true" : "false";
    abrirModal("modalSala");
}
function abrirModalTurma() {
    document.getElementById("tituloTurma").textContent = "Nova turma";
    document.getElementById("formTurma").action = "/turmas/cadastrar";
    document.getElementById("formTurma").reset();
    abrirModal("modalTurma");
}
function editarTurma(id, nome, curso, qtd, turno, sala) {
    document.getElementById("tituloTurma").textContent = "Editar turma";
    document.getElementById("formTurma").action = "/turmas/editar/" + id;
    document.getElementById("turmaNome").value = nome;
    document.getElementById("turmaCurso").value = curso;
    document.getElementById("turmaQtd").value = qtd;
    document.getElementById("turmaTurno").value = turno;
    document.getElementById("turmaSala").value = sala;
    abrirModal("modalTurma");
}
function abrirModalReserva() { abrirModal("modalReserva"); }

function filtrarCards(inputId, selectId, selector) {
    const q = document.getElementById(inputId)?.value.toLowerCase() || "";
    const f = document.getElementById(selectId)?.value || "";
    const cards = document.querySelectorAll(selector);
    let visible = 0;
    cards.forEach(card => {
        const okText = (card.dataset.search || "").includes(q);
        const okFilter = !f || card.dataset.filter === f;
        card.style.display = okText && okFilter ? "" : "none";
        if (okText && okFilter) visible++;
    });
    const empty = document.getElementById("semSalas");
    if (empty) empty.style.display = visible ? "none" : "block";
}

document.addEventListener("click", e => {
    if (e.target.classList.contains("modal-overlay")) e.target.classList.remove("show");
});
