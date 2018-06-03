import math
nombre = str(input("Coloque su nombre: "))
print("Buenos días")
print("Oraculo empieza su funcionamiento, ¿qué es lo que desea", nombre, "?")

print("Escoja su orden")
print("1. Función calculadora")
print("2. Función navegador")
print("3. Función asistente personal")

orden = str(input(""))
if orden == "1":
    print("¿Cúal desea?")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print("5.Potenciación")
    print("6.Radicación")
    orden = str(input("Escriba su opción:"))
    n = 0
    a = 0
    if orden == "1":
        n = int(input("Coloque el número de sumandos"))
        a = int(input("Escriba el sumando"))
        for i in range(n-1):
            b = int(input("Escriba el sumando"))
            a = a + b
        print("La suma es:", a)
    if orden == "2":
        n = int(input("Escriba la cantidad de números a efectuar"))

        a = int(input("Escriba el primer minuendo"))

        for i in range(n-1):
            b = abs(int(input("Escriba el sustraendo")))
            a = a - b
        print("El resto es:", a)
    if orden == "3":
        n = int(input("Coloque el número de factores"))
        a = int(input("Escriba el primer factor"))
        for i in range(n-1):
            b = int(input("Escriba el siguente factor"))
            a = a * b
        print("El producto es", a)
    if orden == "4":
        a = int(input("Escriba el dividiendo"))
        b = int(input("Escriba el divisor"))
        a = a / b
        print("El cociente es", a)
    if orden == "5":
        a = int(input("Escriba la base"))
        b = int(input("Escriba el exponente"))
        a = a**b
        print("La potencia es", a)
    if orden == "6":
        print("Solo funciona con raíz cuadrada")
        a = int(input("Escriba el radicando:"))
        a = math.sqrt(a)
        print("La raíz es:", a)
