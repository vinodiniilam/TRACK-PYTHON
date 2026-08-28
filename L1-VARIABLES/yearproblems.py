year=int(input("enter the year: "))
if year%400!=0 and year%4!=0 and year%100!=0:
    print("the year is not a leap year")
else:
    print("the year is a leap year")    
#finding month days by using month number
n=int(input("enter the month number: "))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("the month has 31 days")
elif n==4 or n==6 or n==9 or n==11:
    print("the month has 30 days")
elif n==2:
    print("the month has 28 or 29 days")
else:
    print("invalid month number") 
#finding name by using number of month
n=int(input("enter the no of month: "))
if n==1:
    print("january")
elif n==2:
    print("february")
elif n==3:
    print("march")
elif n==4:
    print("april")
elif n==5:
    print("may")
elif n==6:
    print("june")
elif n==7:
    print("july")
elif n==8:
    print("august")
elif n==9:
    print("september")
elif n==10:
    print("october")
elif n==11:
    print("november")
elif n==12:
    print("december")
else:
    print("invalid month number") 