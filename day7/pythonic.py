from functools import reduce

double = [x*2 for x in range(1, 11)]
triple = [x*3 for x in range(1, 11)]
square = [x*x for x in range(1, 21)]

print("double:", double)
print("triple:", triple)
print("square:", square)

values = [1, 2, -3, 4, -6, 5]
positive_nums = [n for n in values if n >= 0]
negative_nums = [n for n in values if n < 0]
even_nums = [n for n in values if n % 2 == 0]
odd_nums = [n for n in values if n % 2 != 0]

print("\npositive:", positive_nums)
print("negative:", negative_nums)
print("even:", even_nums)
print("odd:", odd_nums)

details = {"name": "abdullah", "friend": "ali", "friend2": "ahmed"}
upper_details = {k: v.upper() for k, v in details.items()}
print("\nupper details:", upper_details)



cube = lambda x: x*x*x
nums = [1, 2, 3, 4, 5, 6]

cubed = list(map(cube, nums))
filtered = list(filter(lambda x: x > 2, nums))
total = reduce(lambda x, y: x+y, nums)

print("\ncubed:", cubed)
print("filtered (>2):", filtered)
print("total (reduce):", total)



fruits = {"apple": 56, "mango": 65, "orange": 75}
sorted_by_key = dict(sorted(fruits.items(), key=lambda item: item[0]))
sorted_by_value = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

print("\nsorted by key:", sorted_by_key)
print("sorted by value:", sorted_by_value)


names = ("apple", "mango", "orange")
prices = [56, 65, 75]
zipped = dict(zip(names, prices))
print("\n", zipped)



fruit_list = ["apple", "mango", "orange"]
for i, fruit in enumerate(fruit_list):
    print(f"{i}: {fruit}")


try:
    x = int(input("\nenter a number: "))
    result = 10 / x
except ValueError:
    print("that's not a number!")
except ZeroDivisionError:
    print("can't divide by zero!")
else:
    print(f"result: {result}")
finally:
    print("done.")


class NegativeValueError(Exception):
    pass

try:
    age = int(input("enter your age: "))
    if age < 0:
        raise NegativeValueError("age can't be negative!")
    print(f"your age is {age}")
except NegativeValueError as e:
    print(e)