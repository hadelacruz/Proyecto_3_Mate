
from sympy import sympify, Mod

def evaluar_expresion(expresion, modulo):
    # Eliminar espacios en blanco
    expresion = expresion.replace(" ", "")
    
    # Reemplazar ^ por ** para potencias
    expresion = expresion.replace("^", "**")
    
    # Evaluar la expresión usando sympy
    resultado = sympify(expresion)
    
    # Mostrar el resultado antes de aplicar el módulo
    print(f"Resultado antes del módulo: {resultado}")
    
    # Aplicar el módulo y convertir a entero
    resultado_final = int(Mod(resultado, modulo))
    
    return resultado_final

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("División por cero")
    return a / b

def potencia(a, b):
    return a ** b
