import os
import sys

print("Bienvenido")

x = float(input("Ingrese el precio del dolar hoy: "))

def calculate():

	m = float(input("Desea comprar/importar algo fisico(1*) , un servicio digital(2*) , divisa(3*) ?: "))

	if m == 1:

		y = float(input("Ingrese el valor total en >dolares< del producto que desea: "))

		if y > "50":
			print("En total, con todos los impuestos pagaras: ")
			print("$",((x*3/10+x)*21/100+(x*3/10+x)*y)*(5/10)+(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")

		if y <= "50":
			print("En total, con todos los impuestos pagaras: ")
			print("$",(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos") 

	if m == 2:
		y = float(input("Ingrese el valor en >dolares< del producto que desea: "))
		print("En total, con todos los impuestos pagaras: ")
		print("$",(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")

	if m == 3:
		y = float(input("Ingrese el monto de dolares que desea comprar: "))
		print("En total, con todos los impuestos pagaras: ")
		print("$",(x*3/10+x)*y , "Pesos Argentinos")

def run():

	calculate()

	z = input("Desea calcular otra vez? Si(1*), No(2*): ")

	if z != "2":
		calculate()

run()
	
