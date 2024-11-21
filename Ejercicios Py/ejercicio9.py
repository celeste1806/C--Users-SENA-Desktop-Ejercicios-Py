alto = float(input("Ingresa el alto de los muros en metros: "))
ancho = float(input("Ingresa el ancho de los muros en metros: "))
num_muros = int(input("Ingresa la cantidad de muros que deseas enchapar: "))

area_total = alto * ancho * num_muros

caja_cobertura = 3.5
cajas_necesarias = area_total / caja_cobertura

import math
cajas_necesarias = math.ceil(cajas_necesarias)

print(f"El área total de los muros del baño es: {area_total:.2f} metros cuadrados.")
print(f"El número de cajas de baldosas necesarias es: {cajas_necesarias}")
