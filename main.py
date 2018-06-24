n = str(input("Ingrese la cantidad a convertir: "))
m = 0
metros = ["metros", "m", "Metros", "metro"]
decimetros = ["decimetros", "decímetros", "Decimetros", "decímetros", "dm"]
centimetros = ["centimetros", "centímetros", "Centímetros", "centimetros", "cm"]
milimetros = ["milimetros", "Milimetros", "milímetros", "Milímetros", "mm"]
decametros = ["decámetros", "decametros", "Decametros", "Decámetros", "Dm"]
hectametros = ["hectametros", "hectámetros", "Hectametros", "Hectámetros", "Hm", "hm"]
kilometros = ["kilometros", "Kilometros", "kilómetros", "Kilómetros", "Km", "km"]
def conversor1(n):
  n = n.replace(" ", ",")
  n = n.split(",")
  m = n[0]
  n = n[1]
  m = int(m)
  if  n in metros:
    m = m*1
  elif n in decimetros:
    m = m*0.1
  elif n in centimetros:
    m = m*0.01
  elif n in milimetros:
    m = m*0.001
  elif n in decametros:
    m = m*10
  elif n in hectametros:
    m = m*100
  elif n in kilometros:
    m = m*1000
  llamar_conversor2(m)
  return m
def llamar_conversor2(m):
  x = str(input("Escriba a que valor desea convertir: "))
  if x in metros:
    m = m*1
    n = "metros"
  elif x in decimetros:
    m = m*10
    n = "decímetros"
  elif x in centimetros:
    m = m*100
    n = "centímetros"
  elif x in milimetros:
    m = m*1000
    n = "milímetros"
  elif x in decametros:
    m = m*0.1
    n = "decámetros"
  elif x in hectametros:
    m = m*0.01
    n = "hectámetros"
  elif x in kilometros:
    m = m*0.001
    n = "kilómetros"
  print(m, n)
  return m,n
conversor1(n)

kilogramos=["kilos", "kilógramos", "kg"]
libras=["libras","libra","lb"]
def conversor3(n):
   n=int(input("Ingrese el valor a convertir:"))
   if n in kilogramos:
   m= n*2.20462
   n= "Libras"
   print(m, n)
   return m,n
  
def conversor4(n):
   n=int(input("Ingrese el valor a convertir:"))
   if n in libras:
   m= n/2.20462
   n= "kilogramos"
   print(m, n)
   return m,n
°C=["C", "centígrados", "celcius","C"]
°K=["°K","K","kelvin"]
def conversor5(n):
   n=int(input("Ingrese el valor a convertir:"))
   if n in °C:
   m= n+273
   n= "°K"
   print(m, n)
   return m,n
  
def conversor6(n):
   n=int(input("Ingrese el valor a convertir:"))
   if n in °K:
   m=n-273
   n= "°C"
   print(m, n)
   return m,n

L=["Litros","Litro","L","litros","litro","l"]
Oz=["Onzas","Onza","Oz","onzas","onza","oz"]
def conversor7(n):
  n=int(input("Ingrese el valor a convertir:"))
   if n in L:
   m=n*33.814
   n= "Oz"
   print(m, n)
   return m,n
def conversor8(n):
   n=int(input("Ingrese el valor a convertir:"))
   if n in Oz:
   m=n/33.814
   n= "L"
   print(m, n)
   return m,n

  
