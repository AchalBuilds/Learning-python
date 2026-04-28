
pin = int(input("Enter your PIN:"))

access_granted = False
attempts = 0

if pin == 1234:
    print("Access Granted.")
    access_granted = True
else:
    attempts = 1
    
    while access_granted == False:
        print(f"Wrong PIN. {3 - attempts} attempts remaining.")
        pin = int(input("Enter your PIN:"))
        attempts += 1

        if pin == 1234:
            access_granted = True
            print("Access Granted.")
            attempts = 0

        if attempts == 3:
            print("Too many wrong attempts. Card Blocked.")
            break

if access_granted == True:
    a = 1000
    print(f"Your current balance is: ${a}")
    withdrawal_amount = int(input("How much would you like to withdraw: $"))

    if withdrawal_amount <= a:
        print("Withdrawal Successful.")
        print(f"Your new balance is: ${a - withdrawal_amount}")
    else:
        print(f"Insufficient Funds! You only have ${a}.")