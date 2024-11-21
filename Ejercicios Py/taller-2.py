def calcular_p(r):
  if r == 2:
    return "no se puede calcular ,r no puede ser igual a 2"
  else :
    p = (r-2)**3
    return p

r = float(input("ingrese el valor de r:"))
resultado =calcular_p(r)
print("el resultado es:",resultado)
