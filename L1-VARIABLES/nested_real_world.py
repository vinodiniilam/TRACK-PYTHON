amount=int(input("enter the amount: "))
withdrwal=int(input("ebter the withdrawl amount: "))
balance_amount=0
if withdrwal<=amount:
    if withdrwal>0:
        balance_amount=amount-withdrwal
        print("the balace amount is",balance_amount)
        if balance_amount>=500:
            print("withdrawl successful")
        else:
            print("the minimum balance should be equal to 500,try another withdrawl amount")
    else:
        print("invalid amount")
else:
    print("insufficient balance")
#ATM WITHDRAWL
pin=int(input("enter the pin: "))
amount=int(input("enter the amount"))
balance_amount=int(input("enter the balance_amount"))
if pin=="1234":
    if balance_amount%100==0:
        if amount<=balance_amount:
            print("Withdrawl Successfull")
        else:
            print("Insufficient Balance")
    else:
        print("Please enter the amount in multiple of 100")
else:
    print("Invalid Pin")
#collage admission
percentage=int(input("enter the percentage: "))
score=int(input("enter the score: "))
if score>=60:
    if percentage>=75:
        print("Admission Eligible")
    else:
        print("required percentage not obtained")
else:
    print("score is insufficient")

degree=input("enter the qualification degree: ")
percentage=int(input("enter the percentage: "))
YOP=int(input("enter the year of passing: "))
if degree=="B.Tech":
    if percentage>=75:
        if YOP>=2025:
            print("Shortlisted")
        else:
            print("Not short listed")
    else:
        print("percentage does not meet") 
else:
    print("Qualification is not eligible")   



    
