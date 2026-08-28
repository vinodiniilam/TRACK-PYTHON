n=int(input("enter the number: "))
if n%3==0 and n%5==0:
    print("the number is divisible by both")
else:
    print("the number is not divisible by both")  
#divisible by 3 0r 5  
if n%3==0 or n%5==0:
    print("the number is divisible by 3 or 5")
else:
    print("the number is not divisible by 3 or 5") 
#nested conditions
percentage=float(input("enter the percentage: "))
attendance=float(input("enter the attendance percentage: "))
if percentage>=75 and attendance>=75:
    print("eligible for the exam")
else:
    print("not eligible for the exam") 
#if number is divisible by but not 10
n=int(input("enter the number: ")) 
if n%5==0 and n%10!=0: 
    print("divisible by 5 and not 10")



