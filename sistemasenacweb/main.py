import tkinter as tk

from interface import SistemaInterface


# ==========================================
# LISTAS DO SISTEMA
# ==========================================

usuarios = []
salas = []
turmas = []
reservas = []


# ==========================================
# JANELA PRINCIPAL
# ==========================================

root = tk.Tk()


# ==========================================
# SISTEMA
# ==========================================

app = SistemaInterface(
    root,
    usuarios,
    salas,
    turmas,
    reservas
)


# ==========================================
# EXECUTAR
# ==========================================

root.mainloop()