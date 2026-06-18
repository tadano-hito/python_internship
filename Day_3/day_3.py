fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[::2]) 
print(fruits[0:3:2])
print(fruits[0:4:2])
print(fruits[0:5:2])
print(fruits[::-1])
print(fruits[0:1:-1])

# contacts={}

# for i in range(5):
#     name= input("enter ur name ")
#     number=input("enter ur phone number ")
#     contacts[name]= number

# for name, number in contacts.items():
#     print("contacts info")
#     print(f"{name} : {number}")


# name_to_update = input("Enter name to update: ")
# if name_to_update in contacts:
#     new_number = input("Enter new number: ")
#     contacts[name_to_update] = new_number
#     print("Updated!")
# else:
#     print("contacts not found")

# name_to_delete = input("Enter name to delete: ")
# if name_to_delete in contacts:
#     del contacts[name_to_delete]
#     print("Deleted!")
# else:
#     print("Contact not found")

# print(contacts)

s=("hellomf")
print(s.upper(),
s.lower(),
s.split(" "),
s.capitalize(),
s.rstrip("!"),
s.center(20),
s.count("l"),
s.endswith("f"),
s.find("f"),
s.isalnum()
)
new_s = s[:5] + " " + s[5:]
print(new_s)