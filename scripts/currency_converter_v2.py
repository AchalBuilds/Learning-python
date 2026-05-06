
rates = {
    "USD" : 1.0,
    "INR" : 94.9,
    "EUR" : 0.85,
    "JPY" : 156.1,
    "RUB" : 75.0,
    "CNY" : 6.8,
    "CAD" : 1.35,
    "MXN" : 17.4,
    "BRL" : 4.95,
    "COP" : 3710,
    "ARS" : 1390,
    "CLP" : 910,
    "GBP" : 0.74,
    "CHF" : 0.78,
    "TRY" : 45.24,
    "PKR" : 278,
    "AUD" : 1.38,
    "SGD" : 1.27,
    "NZD" : 1.67,
    "PHP" : 61.3,
    "KRW" : 1453,
    "IDR" : 17390
         }

print("------Global Exchange Converter------")

amount = float(input("Enter amount: "))

while amount <0 :
    print("Error: Transaction Cancelled. Amount cannot be negative.")
    amount = float(input("Please enter a valid amount: "))

from_cur = input("From (a valid currency abbrevation): ").upper()
to_cur = input("To (a valid currency abbreviation): ").upper()

print()

if from_cur in rates and to_cur in rates:
    print("Processing conversion... \n--------------------------")
    result = round((amount/ rates[from_cur])* rates[to_cur], 2)
    exchange_rate = round(rates[to_cur]/rates[from_cur], 2)
    print(f"Starting: {amount} {from_cur}")
    print(f"Exchange rate: {exchange_rate}") 
    print(f"Result: {result} {to_cur}")
else:
    print("Invalid currency entered!")