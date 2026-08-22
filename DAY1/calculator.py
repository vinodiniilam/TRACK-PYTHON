def mini_calculator(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:    
        return "invailid operator"
print(mini_calculator(10,20,'+'))
