area_terreno = float(input("Ingresa el área total del terreno en metros cuadrados: "))

porcentaje_cultivos = 0.40
porcentaje_vivienda = 0.25
porcentaje_zonas_verdes = 0.15

area_cultivos = area_terreno * porcentaje_cultivos
area_vivienda = area_terreno * porcentaje_vivienda
area_zonas_verdes = area_terreno * porcentaje_zonas_verdes

area_disponible = area_terreno - (area_cultivos + area_vivienda + area_zonas_verdes)

print(f"Área destinada a cultivos: {area_cultivos:,.2f} metros cuadrados.")
print(f"Área destinada a vivienda: {area_vivienda:,.2f} metros cuadrados.")
print(f"Área destinada a zonas verdes: {area_zonas_verdes:,.2f} metros cuadrados.")
print(f"Área disponible para otros proyectos: {area_disponible:,.2f} metros cuadrados.")
