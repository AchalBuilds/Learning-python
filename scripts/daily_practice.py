
name = input("What is your name?:")

if name == "Achal":
  code = int(input("Enter the secret code:"))
  attempts = 0
  if code == 1234:
      print("Access Granted. Welcome, Developer.")
  else: 
      attempts = 1
      access_granted = False
      while access_granted == False:
         print(f"Wrong Code. Try Again. {3 - attempts} attempts left.")
         code = int(input("Enter the secret code:"))
         attempts += 1

         if code == 1234:
            print("Access Granted! Finally.")
            access_granted = True
         if attempts == 3:
            print("Too many failed attempts! System Locked.")
            break
else:
  print("Identity unverified. Initializing standard visitor profile.")