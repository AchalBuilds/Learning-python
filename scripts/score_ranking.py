
while True:
    score = float(input("Enter score: "))

    if score == -1:
        print("Program quitted successfully.")
        break

    if score > 100 or score <0 :
        print("Invalid Score. Try Again")
    elif score >= 90:
        print("Rank: Legend")
    elif score >=70:
        print("Rank: Warrior")
    elif score >= 50:
        print("Rank: Noob")
    else:
        print("Rank: Recruit")