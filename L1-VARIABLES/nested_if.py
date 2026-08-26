"""#finding largest among three
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print(largest)
#finding the smallest among  three
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c
print(smallest) 
#student eligibilty
marks=int(input("enter the marks: "))
attendence=int(input("enter the attendence percentage: "))
if attendence>=75:
    if marks>=60:
        print("eligible for the exam")
    else:
        print("not eligible for the exam")    
else:
    print("attendence has to be improved") 
#driving license
age=int(input("enter the age: "))
license=input("have you have license:")
if age>=18:
    if license=="yes":
        print("eligible for driving license")
    elif license=="no":
        print("not eligible for driving license")
    else:
        print("invalid input")
else:
    print(" age is below 18 so not eligible for driving license")"""
#job eligibilty
age=int(input("enter the age: "))
qualification=input("enter the qualification: ")
percentage=int(input("Enter the percentage: "))
if age>=21:
    if qualification=="B.tech":
        if percentage>=60:
            print("elgible for job")
        else:
            print("not eligible")
    else:
        print("the qualification does not met")   
else:
    print("age is not elgible")             
    

