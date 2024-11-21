monto_herencia = float(input("Ingresa el monto total de la herencia: "))

porcentaje_esposa = 0.40
porcentaje_hijo1 = 0.30
porcentaje_hijo2 = 0.20
porcentaje_hijo3 = 0.40
porcentaje_hijo4 = 0.10

parte_esposa = monto_herencia * porcentaje_esposa

parte_hijo1 = monto_herencia * porcentaje_hijo1
parte_hijo2 = monto_herencia * porcentaje_hijo2
parte_hijo3 = monto_herencia * porcentaje_hijo3
parte_hijo4 = monto_herencia * porcentaje_hijo4

print(f"A la esposa le corresponde: {parte_esposa:,.2f} unidades de dinero.")
print(f"Al hijo 1 le corresponde: {parte_hijo1:,.2f} unidades de dinero.")
print(f"Al hijo 2 le corresponde: {parte_hijo2:,.2f} unidades de dinero.")
print(f"Al hijo 3 le corresponde: {parte_hijo3:,.2f} unidades de dinero.")
print(f"Al hijo 4 le corresponde: {parte_hijo4:,.2f} unidades de dinero.")
