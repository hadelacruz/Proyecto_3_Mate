import tkinter as tk
from tkinter import messagebox
from Operaciones import evaluar_expresion
from sympy import SympifyError

# Función para validar operadores como + - / * que sean correctos
def es_expresion_valida(expresion):
    operadores = set("+-*/()^")
    valido = True
    paren_count = 0
    for i, char in enumerate(expresion):
        if not (char.isdigit() or char in operadores or char.isspace()):
            valido = False
            break
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
        if i > 0 and char in operadores and expresion[i - 1] in operadores and expresion[i - 1] != '(' and char != ')':
            valido = False
            break
    if paren_count != 0:
        valido = False
    return valido

# Función para calcular el resultado de la expresión
def calcular():
    expresion = entrada_expresion.get()
    modulo = entrada_modulo.get()

    # Validar que la expresión sea válida
    if not es_expresion_valida(expresion):
        messagebox.showerror("Error", "La expresión ingresada no es válida. Verifique la sintaxis.")
        return
    
    # Validar que el módulo sea un número positivo
    try:
        modulo = int(modulo)
        if modulo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "El módulo debe ser un número entero positivo.")
        return
    
    # Calcular la expresión con el módulo
    try:
        resultado = evaluar_expresion(expresion, modulo)
        resultado_label.config(text=f"Resultado: {resultado}")
    except SympifyError:
        messagebox.showerror("Error", "La expresión ingresada no es válida. Verifique la sintaxis.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero en la expresión.")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Aritmética Modular")

# Crear widgets
label_instrucciones = tk.Label(ventana, text="Ingrese una expresión (use +, -, *, /, (), ^):")
label_instrucciones.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

entrada_expresion = tk.Entry(ventana, width=50)
entrada_expresion.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

label_modulo = tk.Label(ventana, text="Ingrese el módulo (número primo):")
label_modulo.grid(row=2, column=0, padx=10, pady=10)

entrada_modulo = tk.Entry(ventana, width=20)
entrada_modulo.grid(row=2, column=1, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
