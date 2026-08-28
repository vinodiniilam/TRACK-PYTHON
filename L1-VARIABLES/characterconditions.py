#alphabet or not
n=input("enter the character: ")
if n>="a" and n<="z" or n>="A" and n<="Z":
    print("the character is an alphabet")
else:
    print("the character is not an alphabet") 
#digit or not
if n>='0' and n<='9':
    print("it is a digit")
#findig special character
n=input("enter the character: ")
if n>="a" and n<="z" or n>="A" and n<="Z" or n>="0" and n<="9":
    print("the character is not a special character")
else:
    print("the character is a special character")
#uppercase or not
n=input("enter the character: ")
if n=='A' and n<='Z':
    print("UPPERCASE")
elif n<='a' and n<='z':
    print("lowercase")
else:
    print("it is a number")
n=input("enter the character: ")
if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
    print("it is vowel")
else:
    print("it is not vowel")   
n=input("enter the charcater: ") 
if n>='A' and n<='Z':
    print("uppercase")
elif n>='a' and n<='z':
    print("lowercase")
elif n>='0' and n<='9':
    print("it is a number")    
else:
    print("it is a special characcter")




 