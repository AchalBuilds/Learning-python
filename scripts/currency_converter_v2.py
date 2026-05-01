
rates = {
    "USD" : 1.0,
    "INR" : 95.2,
    "EUR" : 0.85,
    "JPY" : 157.25,
    "RUB" : 75.0
         }

print("------Global Exchange Converter------")

amount = float(input("Enter amount: "))

while amount <0 :
    print("Error: Transaction Cancelled. Amount cannot be negative.")
    amount = float(input("Please enter a valid amount: "))

from_cur = input("From (USD/INR/EUR/JPY/RUB): ").upper()
to_cur = input("To (USD/INR/EUR/JPY/RUB): ").upper()

if from_cur and to_cur in rates:
    print("Processing conversion... \n--------------------------")
    result = (amount/ rates[from_cur])* rates(to_cur)
    print