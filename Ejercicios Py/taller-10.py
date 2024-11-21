nombre = input("ingrese su nombre:")
edad = int(input("ingrese su edad: "))
sexo =input("ingrese su sexo (F: femenino, M: masculino):")
estado_civil = int(input("ingrese su estado civil (1:casado, 2:soltero, 3:separado, 4:otros):"))

if edad < 18:
    print(f"{nombre},no puede votar porque es menor de edad")
elif edad > 18 and sexo =="F" and estado_civil==1:
    print(" puedes votar en la mesa 1")
elif  edad > 18 and sexo=="F" and estado_civil==2:
    print(" puedes votar en la mesa 2")
elif edad > 18 and sexo=="F" and estado_civil==3:
    print(" puedes votar en la mesa 3")
elif edad > 18 and sexo =="F" and estado_civil==4:
    print(" puedes votar en la mesa 4")
elif edad > 18 and sexo=="F" and estado_civil==1:
    print(" puedes votar en la mesa 5")
elif edad > 18 and sexo=="F" and estado_civil==2:
    print(" puedes votar en la mesa 5")
elif edad > 18 and sexo =="F" and estado_civil==3:
    print(" puedes votar en la mesa 7")
elif edad > 18 and sexo=="F" and estado_civil==4:
    print(" puedes votar en la mesa 8")
