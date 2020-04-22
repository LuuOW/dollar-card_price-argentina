import sys
x = float(input("Ingrese el precio del dolar hoy: "))
y = float(input("Ahora ingrese el valor en dolares del producto que desea: "))
print("En total, con todos los impuestos pagaras: ")
print("$",(x*3/10+x)*21/100+(x*3/10+x)*y , "Pesos Argentinos")
input("Presione enter para salir: ")
sys.exit()