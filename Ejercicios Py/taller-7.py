puntaje_matematica = float (input("ingrese puntaje de aptitud matematica:"))
puntaje_lenguaje = float (input("ingrese puntaje de puntaje_lenguaje:"))

if puntaje_matematica > puntaje_lenguaje :
  print (f"mayor puntaje en aptitud matematica:{puntaje_matematica}")
elif puntaje_lenguaje > puntaje_matematica:
  print(f"mayor puntaje en lenguaje:{puntaje_lenguaje}")
else:
  print(f" los puntaje son iguales:{puntaje_matematica} an ambas pruebas")