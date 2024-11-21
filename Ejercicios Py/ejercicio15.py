numero_inicial = int(input("Ingresa el número de la registradora al inicio del día: "))
numero_final = int(input("Ingresa el número de la registradora al final del día: "))

numero_pasajeros = numero_final - numero_inicial

valor_pasaje = float(input("Ingresa el valor del pasaje: "))

total_generado = numero_pasajeros * valor_pasaje

valor_conductor = total_generado / 4 
valor_empresa = total_generado * 3 / 4 

print(f"Total de pasajeros transportados: {numero_pasajeros}")
print(f"Valor liquidado al conductor: {valor_conductor:.2f} unidades de dinero.")
print(f"Total liquidado a la empresa: {valor_empresa:.2f} unidades de dinero.")
