taller1 = float(input("Ingresa la nota del primer taller: "))
taller2 = float(input("Ingresa la nota del segundo taller: "))
nota_1 = (taller1 + taller2) / 2 

evaluacion1 = float(input("Ingresa la nota de la primera evaluación: "))
evaluacion2 = float(input("Ingresa la nota de la segunda evaluación: "))
evaluacion3 = float(input("Ingresa la nota de la tercera evaluación: "))
nota_2 = (evaluacion1 + evaluacion2 + evaluacion3) / 3 

nota_3 = float(input("Ingresa la nota del trabajo final: "))

quiz1 = float(input("Ingresa la nota del primer quiz: "))
quiz2 = float(input("Ingresa la nota del segundo quiz: "))
quiz3 = float(input("Ingresa la nota del tercer quiz: "))
quiz4 = float(input("Ingresa la nota del cuarto quiz: "))
nota_4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4 

nota_definitiva = (nota_1 * 0.15) + (nota_2 * 0.30) + (nota_3 * 0.30) + (nota_4 * 0.25)

print(f"La nota definitiva del estudiante es: {nota_definitiva:.2f}")
