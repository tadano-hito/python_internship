num1= float(input("enter first value "))
sign=input("enter sign ")
num2= float(input("enter second value "))

if sign == "+":
    result = num1+num2
elif sign == "-":
    result= num1-num2
elif sign == "*":
    result = num1*num2
elif sign == "/":
        if num2!=0:
         result = num1/num2
        else: result=print("enter another value except zero")
else:
    result= "invaled sign"

print("Answer:",result)