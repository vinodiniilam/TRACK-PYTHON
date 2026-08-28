bill=int(input("enter the bill amount: "))
if bill>=10000:
    print("the discount is 25%")
elif bill>=5000:
    print("the discount is 15%")
elif bill>=2000:
    print("the discount is 10%")
else:
    print("the discount is 0%")
#shopping eligibilty
purchase=int(input("enter the amount: ")) 
is_member=input("are you member (yes/no): ").lower()
if purchase>=10000 or is_member=="yes":
    print("free delivery")
else:
    print("paid delivery")    
