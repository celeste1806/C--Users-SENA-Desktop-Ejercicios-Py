A =float(input("ingrese lado A:"))
B =float(input("ingrese lado B:"))
C =float(input("ingrese lado C:"))

if  A + B > C and A + C > B and B + C > A:


 if A ==B == C: 
    print ("triangulo equilatero")
 elif A != B and B != C and A != C:
   print("triangulo escaleno")
 else:
    print("triangulo isosceles")
else:
  print("los lados no forman un triangulo")   


