
print("------Global Exchange Converter------")

amount = float(input("Enter amount: "))

while (amount < 0):
    print("Error: Transaction Cancelled. Amount cannot be negative.")
    amount = float(input("Please enter a valid amount: "))

converted_from = input("From (USD/INR):").upper()
converted_to = input("To (USD/INR):").upper()

print("Processing conversion... \n--------------------------")


if (converted_from == "USD") and (converted_to == "INR"):
    print(f"Starting: {amount} USD")
    print("Exchange rate: 94.9")
    print(f"Result: {amount*94.9} INR")
    print("--------------------------")

elif (converted_from == "USD") and (converted_to == "USD"):
    print(f"Starting: {amount} USD")
    print("Exchange rate: 1.0")
    print(f"Result: {amount} USD")
    print("--------------------------")

elif (converted_from == "INR") and (converted_to == "USD"):
    print(f"Starting: {amount} INR")
    print("Exchange rate: 0.011")
    print(f"Result: {amount*0.011} USD")
    print("--------------------------")

elif (converted_from == "INR") and (converted_to == "INR"):
    print(f"Starting: {amount} INR")
    print("Exchange rate: 1.0")
    print(f"Result: {amount} INR")
    print("--------------------------")

else:
    print("Invalid details.")