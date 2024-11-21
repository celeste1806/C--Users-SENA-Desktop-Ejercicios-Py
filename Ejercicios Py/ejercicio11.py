monto_herencia = float(input("Ingresa el monto total de la herencia: "))

parte_madre = monto_herencia * 0.50

parte_restante = monto_herencia * 0.50

parte_por_hijo = parte_restante / 4

print(f"La madre recibe: {parte_madre:.2f} unidades de dinero.")
print(f"Cada hijo recibe: {parte_por_hijo:.2f} unidades de dinero.")
