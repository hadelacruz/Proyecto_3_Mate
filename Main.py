
from Operaciones import evaluar_expresion
from sympy import SympifyError

#Funcion para validar operadores como + - / * que sean correctos
def es_expresion_valida(expresion):
    # Conjunto de operadores válidos
    operadores = set("+-*/()^")
    valido = True
    paren_count = 0
    # Iterar sobre cada carácter en la expresión
    for i, char in enumerate(expresion):
        if not (char.isdigit() or char in operadores or char.isspace()):
            valido = False
            break
        # Contar los paréntesis
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
        # Verificar operadores consecutivos
        if i > 0 and char in operadores and expresion[i - 1] in operadores and expresion[i - 1] != '(' and char != ')':
            valido = False
            break
    # Comprobar que los paréntesis están balanceados
    if paren_count != 0:
        valido = False

    return valido


# Función principal que controla el menú de la calculadora
def menu():
    while True:
        print("\n-------------Calculadora de Aritmética Modular-------------")
        print("1. Evaluar expresión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Operadores aceptados: + - / * () ^")
            expresion = input("Ingrese la expresión a evaluar: ")
            
            # Validar la expresión antes de continuar
            if not es_expresion_valida(expresion):
                print("Error: La expresión ingresada no es válida. Verifique la sintaxis.")
                continue
        
            # Verificar que el módulo sea un número entero válido
            try:
                modulo = int(input("Ingrese el módulo: "))
                if modulo <= 0:
                    raise ValueError("El módulo debe ser un número entero positivo.")
            except ValueError:
                print("Error en el módulo: Debe ser un número entero positivo.")
                continue  # Regresar al menú si el módulo es inválido
            
            # Verificacion de multiples validaciones
            try:
                resultado = evaluar_expresion(expresion, modulo)
                print(f"Resultado final (después del módulo): {resultado}")
            except SympifyError:
                print("Error: La expresión ingresada no es válida. Verifique la sintaxis.")
            except ZeroDivisionError:
                print("Error: División por cero en la expresión.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == '2':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()




