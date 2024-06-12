import math 
def line():
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
	print()

	print(f"""Para la siguiente ecuación:
	\tY = {Coeficiente_A}X + {Coeficiente_B}""")
	print()
	print(f"""Dados los siguientes puntos:
	\tP1 ({Coeficiente_C}, {Y1})
	\tP2 ({Coeficiente_D}, {Y2})""")
	print()
	P1 = Coeficiente_C, Y1
	P2 = Coeficiente_D, Y2

	distancia = math.dist(P1,P2)
	print(f"La distancia entre ellos es: {distancia}")
line()
