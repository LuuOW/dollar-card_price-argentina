import sys

print("Bienvenido")

x = float(input("Ingrese el precio del dolar hoy: "))

def calculate():

	m = float(input("Desea comprar/importar algo fisico(1*) , un servicio digital(2*) , divisa(3*) ?: "))
	if m == 1:
		h = input("El producto que desea comprar supera el precio de 50 dolares? si/no: ")
		y = float(input("Ingrese el valor total en >dolares< del producto que desea: "))
		if h == "si":
			print("En total, con todos los impuestos pagaras: ")
			print("$",((x*3/10+x)*21/100+(x*3/10+x)*y)*(5/10)+(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")
		if h == "no":
			print("En total, con todos los impuestos pagaras: ")
			print("$",(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")
			pass 

	if m == 2:
		y = float(input("Ingrese el valor en >dolares< del producto que desea: "))
		print("En total, con todos los impuestos pagaras: ")
		print("$",(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")
		pass

	if m == 3:
		y = float(input("Ingrese el monto de dolares que desea comprar: "))
		print("En total, con todos los impuestos pagaras: ")
		print("$",(x*3/10+x)*y , "Pesos Argentinos")
		pass
	z = input("Desea volver a calcular? s/n: ")

#start the program 

def run():
	calculate()

	while z == "s":
		calculate()
	pass

run()