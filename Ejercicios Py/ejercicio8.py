costo_llamada1 = float(input("Ingresa el costo de la primera llamada al primer operador: "))
costo_llamada2 = float(input("Ingresa el costo de la segunda llamada al primer operador: "))
costo_llamada3 = float(input("Ingresa el costo de la primera llamada al segundo operador: "))
costo_llamada4 = float(input("Ingresa el costo de la segunda llamada al segundo operador: "))

costo_total_operador1 = costo_llamada1 + costo_llamada2
costo_total_operador2 = costo_llamada3 + costo_llamada4

costo_total_llamadas = costo_total_operador1 + costo_total_operador2

print(f"El costo de la primera llamada al primer operador es: {costo_llamada1}")
print(f"El costo de la segunda llamada al primer operador es: {costo_llamada2}")
print(f"El costo de la primera llamada al segundo operador es: {costo_llamada3}")
print(f"El costo de la segunda llamada al segundo operador es: {costo_llamada4}")
print(f"El costo total de las llamadas al primer operador es: {costo_total_operador1}")
print(f"El costo total de las llamadas al segundo operador es: {costo_total_operador2}")
print(f"El costo total de las cuatro llamadas es: {costo_total_llamadas}")
