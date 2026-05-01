
rates = {
    "USD" : 1.0,
    "INR" : 94.84,
    "EUR" : 0.85,
    "JPY" : 156.40,
    "RUB" : 75.0
         }

print("------Global Exchange Converter------")

amount = float(input("Enter amount: "))

while amount <0 :
    print("Error: Transaction Cancelled. Amount cannot be negative.")
    amount = float(input("Please enter a valid amount: "))

from_cur = input("From (USD/INR/EUR/JPY/RUB): ").upper()
to_cur = input("To (USD/INR/EUR/JPY/RUB): ").upper()

print()

if from_cur in rates and to_cur in rates:
    print("Processing conversion... \n--------------------------")
    result = round((amount/ rates[from_cur])* rates[to_cur], 2)
    exchange_rate = round(rates[to_cur]/rates[from_cur], 2)
    print(f"Starting: {amount} {from_cur}")
    print(f"Exchange rate: {exchange_rate}") 
    print(f"Result: {result} {to_cur}")
else:
    print("Invalid currency entered! Please check the codes.")