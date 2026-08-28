amount=int(input("enter the amount: "))
if amount>=5000:
    discount=(20/100)*amount
    print(discount)
    print("the amount after discount:",amount-discount)
elif amount>=2000:
    discount=(10/100)*amount
    print(discount)
    print("the amount after discount:",amount-discount) 
else:
    print("no discount")
    print("the amount after discount:",amount)    
#elctrity bill
units=int(input("enter the units: "))
if units<=0 and units<=100:
    cost=units*2
    print("the total bill paid is:",cost)
elif units>100 and units<=200: 
    cost=units*3
    print("the total bill paid is:",cost)
else:
    cost=units*5 
    print("the total bill paid is:",cost)
# salary bonus
experience=int(input("enter the experience: ")) 
salary=int(input("enter the salary: "))
if experience>=5:
    bonus=salary*(20/100)
    print(bonus)
    print("the total salary with bonus is:",salary+bonus)  
elif experience>=10:
    bonus=(10/100)*salary
    print("total salry with bonus: ",salary+bonus)   
else:
    bonus=(5/100)*salary
    print("the total salary is ",salary+bonus)     

    
    