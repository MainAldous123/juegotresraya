import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Juego Tres en Raya")
ventana.geometry("300x350")

# Variables globales
turno = "X"
tablero = [["" for _ in range(3)] for _ in range(3)]
botones = []

# Función cuando se hace clic en un botón
def click(fila, columna):
    global turno
    
    if tablero[fila][columna] == "":
        tablero[fila][columna] = turno
        botones[fila][columna]["text"] = turno
        
        if verificar_ganador():
            messagebox.showinfo("Ganador", f"El jugador {turno} ha ganado!")
            desactivar_botones()
            return
        
        turno = "O" if turno == "X" else "X"

# Función para verificar ganador
def verificar_ganador():
    # Filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != "":
            return True
    
    # Columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != "":
            return True
    
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return True
    
    return False

# Desactivar botones después de ganar
def desactivar_botones():
    for fila in botones:
        for boton in fila:
            boton.config(state="disabled")

# Crear botones del tablero
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(
            ventana,
            text="",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda f=fila, c=columna: click(f, c)
        )
        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)
    botones.append(fila_botones)

ventana.mainloop()