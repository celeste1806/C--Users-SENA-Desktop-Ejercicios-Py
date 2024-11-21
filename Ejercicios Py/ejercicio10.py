tiempo_dia1 = float(input("Ingresa el tiempo de entrenamiento del día 1 en minutos: "))
distancia_dia1 = float(input("Ingresa la distancia recorrida el día 1 en metros: "))

tiempo_dia2 = float(input("Ingresa el tiempo de entrenamiento del día 2 en minutos: "))
distancia_dia2 = float(input("Ingresa la distancia recorrida el día 2 en metros: "))

tiempo_dia3 = float(input("Ingresa el tiempo de entrenamiento del día 3 en minutos: "))
distancia_dia3 = float(input("Ingresa la distancia recorrida el día 3 en metros: "))

tiempo_total = tiempo_dia1 + tiempo_dia2 + tiempo_dia3
distancia_total = distancia_dia1 + distancia_dia2 + distancia_dia3

promedio_tiempo = tiempo_total / 3
promedio_distancia = distancia_total / 3

print(f"El tiempo total de entrenamiento es: {tiempo_total} minutos.")
print(f"La distancia total recorrida es: {distancia_total} metros.")
print(f"El promedio de tiempo por día es: {promedio_tiempo:.2f} minutos.")
print(f"El promedio de distancia por día es: {promedio_distancia:.2f} metros.")
