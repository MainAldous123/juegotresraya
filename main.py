import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("🎮 Juego Tres en Raya Version FEATURE")
ventana.geometry("400x450")
ventana.config(bg="#1e1e2f")

turno = "X"
tablero = [["" for _ in range(3)] for _ in range(3)]
botones = []

def click(fila, columna):
    global turno
    
    if tablero[fila][columna] == "":
        tablero[fila][columna] = turno
        botones[fila][columna]["text"] = turno
        
        if verificar_ganador():
            messagebox.showinfo("🏆 Ganador", f"El jugador {turno} ha ganado!")
            desactivar_botones()
            return
        
        turno = "O" if turno == "X" else "X"

def verificar_ganador():
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != "":
            return True
    
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != "":
            return True
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return True
    
    return False

def desactivar_botones():
    for fila in botones:
        for boton in fila:
            boton.config(state="disabled")

# Frame para centrar tablero
frame = tk.Frame(ventana, bg="#1e1e2f")
frame.pack(expand=True)



def reiniciar_juego():
    global turno, tablero
    
    turno = "X"
    tablero = [["" for _ in range(3)] for _ in range(3)]
    
    for fila in botones:
        for boton in fila:
            boton.config(text="", state="normal")




for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(
            frame,
            text="",
            font=("Helvetica", 28, "bold"),
            width=4,
            height=2,
            bg="#2d2d44",
            fg="white",
            activebackground="#3c3c5c",
            activeforeground="white",
            relief="ridge",
            bd=4,
            command=lambda f=fila, c=columna: click(f, c)
        )
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        fila_botones.append(boton)
    botones.append(fila_botones)



boton_reset = tk.Button(
    ventana,
    text="🔄 Reiniciar Juego",
    font=("Helvetica", 14, "bold"),
    bg="#ff4d4d",
    fg="white",
    activebackground="#cc0000",
    activeforeground="white",
    command=reiniciar_juego
)

boton_reset.pack(pady=10)

ventana.mainloop()