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

paragraph = input("Enter a paragraph: ")

word_count = {}

for word in paragraph.lower().split():
    cleaned = word.strip('.,!?";:()[]{}')
    if cleaned in word_count:
        word_count[cleaned] += 1
    else:
        word_count[cleaned] = 1

print("\nWord Count:")
for word, count in word_count.items():
    print(f"{word}: {count}")