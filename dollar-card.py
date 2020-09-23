import os
import sys
import json
import requests


url = 'https://api.exchangerate-api.com/v4/latest/USD'
class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        
    def convert(self, from_currency, to_currency, amount):
        
        if from_currency != 'USD':
            
            amount = amount / self.currencies[from_currency]
        
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
converter = CurrencyConverter(url)
#print(converter.convert('USD', 'ARS', 1))

x = converter.convert('USD', 'ARS', 1)

#x = float(input("Ingrese el valor del dolar hoy: "))

#Choose beetwen digital, phisycal or currency purchases
m = int(input("Que tipo de producto desea comprar: \n"
"1. Digital \n"
"2. Fisico \n"
"3. Divisa \n"))

y = float(input("Ingrese el precio del producto que desea: "))

#Table of all the taxes
imp30 = (x*y)*(3/10)
imp21 = (x*y)*(21/100)
imp50 = (x*y)*(5/10)
imp35 = (x*y)*(35/100)

#Full tax for foreign purcheses
ffTax = imp30 + imp21 + imp50 + imp35
totalFfTax = ffTax + x*y

#Foreign purcheses tax that doesn't overise 50 USD
fsTax = imp35 + imp21 + imp35
totalFsTax = fsTax + x*y

#Digital purcheses tax
digTax = imp30 + imp21 + imp35
totalDigTax = digTax + x*y

#Currency exchange tax
currTax = imp35 + imp30
totalCurrTax = currTax + x*y

if m == 1:
    print("En total, con todos los impuestos pagaras: \n",
    totalDigTax, "Pesos Argentinos")

if m == 2 and y <= 50:
    print("En total, con todos los impuestos pagaras: \n",
    totalFsTax, "Pesos Argentinos") 
if m == 2 and y > 50:
        print("En total, con todos los impuestos pagaras: \n",
    totalFfTax, "Pesos Argentinos")

if m == 3:
    print("En total, con todos los impuestos pagaras: \n",
    totalCurrTax, "Pesos Argentinos")
	
