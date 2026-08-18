def is_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if i%2==0:
            return False
        else:
            return True
number=int(input("enter a number: "))      
print(is_prime(10))    
        

    