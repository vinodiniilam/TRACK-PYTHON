"""
#given number is in range or not using if condition
n=int(input("enter the number: "))
if n in range(10,51):
    print("the number is in the range of 10 to 50")
else:
    print("the number is not in the range of 10 to 50")
#given number is out of  range using if condition
n=int(input("enter the number: "))
if n not in range(10,51):
    print("the number is not in the range of 10 to 50")
else:
    print("the number is in the range of 10 to 50")
#checking digits in the given number
n=int(input("enter the number: "))
if n in range(10,100):
    print("two digit number")
else:
    print("three digit number")"""
n=int(input("enter a number: "))
if n<10:
    print("one digit number")
elif n<100:
    print("two digit number")
elif n<1000:
    print("three digit number")
else:
    print("More than three digit number")    
    

