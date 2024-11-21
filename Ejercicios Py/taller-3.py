goles_encuentro1 = 2
goles_encuentro2 = 3
goles_encuentro3= 2
goles_encuentro4= 3

def calcular_promedio_goles():

 int(input("goles encuentro 1:"))
 int(input("goles encuentro 2:"))
 int(input("goles encuentro 3:"))
 int(input("goles encuentro 4:"))  

suma_goles = goles_encuentro1 + goles_encuentro2 + goles_encuentro3 + goles_encuentro4

if suma_goles > 10:
    promedio_goles= suma_goles /4
    print(f"el promedio de goles es : {promedio_goles}")
else :
    print("no se puede determinar el promedio")
    calcular_promedio_goles
