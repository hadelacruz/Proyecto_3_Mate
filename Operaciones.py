from sympy import sympify, Mod

#Funcion para evaluar los valores de la expresion
def evaluar_expresion(expresion, modulo):
    # Eliminar espacios en blanco
    expresion = expresion.replace(" ", "")
    
    # Reemplazar ^ por ** para potencias
    expresion = expresion.replace("^", "**")
    
    # Evaluar la expresión usando sympy
    resultado = sympify(expresion)
    
    # Mostrar el resultado antes de aplicar el módulo
    print(f"Resultado antes del módulo: {resultado}")
    
    # Si el resultado es una fracción, se maneja la división en aritmética modular
    if isinstance(resultado, (int, float)) or resultado.q == 1:  # Solo un número entero
        # Aplicar el módulo y convertir a entero
        resultado_final = int(Mod(resultado, modulo))
    else:  # Es una fracción
        numerador = resultado.p
        denominador = resultado.q
        
        # Calcular el inverso multiplicativo del denominador
        inverso = inverso_multiplicativo(denominador, modulo)
        
        # Multiplicar el numerador por el inverso y aplicar el módulo
        resultado_final = int(Mod(numerador * inverso, modulo))
    
    return resultado_final

def inverso_multiplicativo(a, m):
    # Encontrar el inverso de 'a' módulo 'm' usando el algoritmo extendido de Euclides
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0

    a = a % m  # Asegurar que a es positivo
    while a > 1:
        # q es el cociente
        q = a // m
        m, a = a % m, m  # m se convierte en el resto
        x0, x1 = x1 - q * x0, x0  # Actualizar x0 y x1

    # Asegurarse de que el resultado sea positivo
    if x1 < 0:
        x1 += m0

    return x1

#Funcion Suma
def suma(a, b):
    return a + b

#Funcion Resta
def resta(a, b):
    return a - b

#Funcion Multiplicacion
def multiplicacion(a, b):
    return a * b

#Funcion Division
def division(a, b):
    if b == 0:
        raise ValueError("División por cero")
    return a / b

#Funcion Potencia
def potencia(a, b):
    return a ** b
