
from Operaciones import evaluar_expresion

def menu():
    while True:
        print("\nCalculadora de Aritmética Modular")
        print("1. Evaluar expresión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            expresion = input("Ingrese la expresión a evaluar: ")
            modulo = int(input("Ingrese el módulo: "))
            try:
                resultado = evaluar_expresion(expresion, modulo)
                print(f"Resultado final (después del módulo): {resultado}")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == '2':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
