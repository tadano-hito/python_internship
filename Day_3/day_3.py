fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[::2]) 
print(fruits[0:3:2])
print(fruits[0:4:2])
print(fruits[0:5:2])
print(fruits[::-1])

contract={}

for i in range(5):
    name= input("enter ur name ")
    number=input("enter ur phone number ")
    contract[name]= number

for name, number in contract.items():
    print("contract info")
    print(f"{name} : {number}")

