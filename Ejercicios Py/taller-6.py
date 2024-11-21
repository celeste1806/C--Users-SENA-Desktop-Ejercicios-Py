bonificacion= float(input("ingrese monto de bonificacion:"))

if bonificacion < 50000: dispositivo ="camara web"
elif 50000 <= bonificacion <= 200000:
    dispositivo="subwoofer"
elif 200000 < bonificacion <= 500000:
    dispositivos="disco duro externo"
elif 500000 < bonificacion <= 1000000 :
    dispositivo="impresora multifuncional"
elif bonificacion > 1000000:
    dispositivos="proyector"
print (f"con una bonificacion de ${bonificacion:.2f}, puede comprar un(a) {dispositivo}.")