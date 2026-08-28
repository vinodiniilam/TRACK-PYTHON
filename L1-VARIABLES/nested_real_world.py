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


    
