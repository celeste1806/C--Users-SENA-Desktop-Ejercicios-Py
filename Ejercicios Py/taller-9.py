edad= int(input("ingrese edad de la persona:"))
  
if edad >= 1 and edad <= 4: 
 costo_dolares= 0
elif  edad >= 4 and edad <= 8:
 costo_dolares = 2
elif edad >= 9 and edad <= 16:
  costo_dolares=5
elif edad >= 17 and edad <=35:
  costo_dolares=6
elif edad >35:
   costo_dolares=10
else: 
  print("la edad no es valida")

tipo_cambio=4500 # COP/UDS

costo_pesos = costo_dolares * tipo_cambio

print (f"costo de entrada en dolares: ${costo_dolares: .2f} USD")
print(f"costo de entrada en pesos colombianos: ${costo_pesos:.2f} COP")