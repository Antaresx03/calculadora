def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

print("Bienvenido a la calculadora!")

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Seleccione una operación (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("El resultado de la suma es:", sumar(num1, num2))
        elif opcion == '2':
            print("El resultado de la resta es:", restar(num1, num2))
        elif opcion == '3':
            print("El resultado de la multiplicación es:", multiplicar(num1, num2))
        elif opcion == '4':
            print("El resultado de la división es:", dividir(num1, num2))
        else:
            print("Opción no válida. Por favor seleccione una opción válida (1/2/3/4/5).")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")
