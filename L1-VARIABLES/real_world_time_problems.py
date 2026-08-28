# time splitting
n=int(input("enter the time: "))
if n>=5 and n<=11:
    print("Morning")
elif n>=12 and n<=16:
    print("Afternonn")
elif n>=17 and n<=20:
    print("Evening")    
else:
    print("night")  
n=int(input("enter the day no: "))
if n>=1 and n<=5:
    print("working day")
elif n>=6 and n<=7:
    print("week end")
else:
    print("invalid input")    
#triangle problems 
# valid triangle
a=int(input("enter the value: ")) 
b=int(input("enter the value: "))
c=int(input("enter the value: "))
if a+b>c and b+c>a and c+a>b:
    print("valid triangle")
else:
    print("invalid triangle") 
a=int(input("enter the side value: ")) 
b=int(input("enter the side value: "))
c=int(input("enter the side value: "))
if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
#right angle traingle
a=int(input("enter the value: "))
b=int(input("enter the value: "))
c=int(input("enter the value: "))
if a**2+b**2==c**2:
    print("right angle triangle")
else:
    print("not a right angle triangle")


