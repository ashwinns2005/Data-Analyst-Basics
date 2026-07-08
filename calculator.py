num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
operations=input("Enter operation (add, sub, mul, div): ")
if operations=="add":
    print(num1+num2)
elif operations=="sub":
    print(num1-num2)
elif operations=="mul": 
    print(num1*num2)
elif operations=="div":
    if num2!=0:
        print(num1/num2)
    else:
        print("Error: Division by zero is not allowed.")    
