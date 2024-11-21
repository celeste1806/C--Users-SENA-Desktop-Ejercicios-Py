desempleo_inicial = float(input("Ingresa el valor inicial del desempleo en porcentaje: "))
desempleo_tras_primero = desempleo_inicial * 1.095
desempleo_actual = desempleo_tras_primero * 0.985
print(f"El valor actual del desempleo es: {desempleo_actual:.2f}%")
