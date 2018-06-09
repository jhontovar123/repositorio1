print("Seleccione su medida")
print("1. metros")
print("2. kilometros")
print("3. centimetros")
medida = int(input("Escriba el número de la medida que ha seleccionado:"))
if medida == 1:
  medida2 = "metros"
elif medida == 2:
  medida2 = "kilometros"
elif medida == 3:
  medida2 = "centimetros"
valor = float(input("Escriba la cantidad que desee: "))
print("Ha seleccionado", medida2)
if medida == 1:
  valor = valor * 1
elif medida == 2:
  valor = valor * 1000
elif medida == 3:
  valor = valor * 0.01
print("Seleccione su medida")
print("1. metros")
print("2. kilometros")
print("3. centimetros")
medida = int(input("Escriba el número de la medida que ha seleccionado: "))
if medida == 1:
  valor = valor * 1
  medida2 = "m"
elif medida == 2:
  valor = valor * 0.001
  medida2 = "km"
elif medida == 3:
  valor = valor *100
  medida2 = "cm"

print("El valor es: ", valor, medida2)
