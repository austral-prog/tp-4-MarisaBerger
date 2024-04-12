def line():
    import math 
Coeficiente_A = float(input("Ingrese el coeficiente A: "))
Coeficiente_B = float(input("Ingrese el coeficiente B: "))
Coeficiente_C = float(input("Ingrese el coeficiente X1: "))
Coeficiente_D = float(input("Ingrese el coeficiente X2: "))

print(f"El coeficiente A de su ecuación de la recta es: {Coeficiente_A}")
print(f"El coeficiente B de su ecuación de la recta es: {Coeficiente_B}")
print(f"El coeficiente X1 de su ecuación de la recta es: {Coeficiente_C}")
print(f"El coeficiente X2 de su ecuación de la recta es: {Coeficiente_D}")

Y1 = Coeficiente_A*Coeficiente_C + Coeficiente_B
Y2 = Coeficiente_A*Coeficiente_D + Coeficiente_B


print(f"""Para la siguiente ecuación: 
	Y = {Coeficiente_A}x + {Coeficiente_B}""")

print(f"""Dados los siguientes puntos:
	P1({Coeficiente_A}, {Y1}))
	P2({Coeficiente_B}, {Y2}""")

P1 = Coeficiente_C, Y1
P2 = Coeficiente_D, Y2

Distancia = math.dist(P1,P2)
print(f"la distancia entre ellos es: {Distancia}")
