details={"name":"abdullah", "friend": "ali","friend2" :"ahmed"}
for key,value in details.items():
    print(f"{key} : {value}" ,end=" - ")


double=[x*2 for x in range(1,11)]
triple=[x*3 for x in range (1,11)]
square=[x*x for x in range (1,21)]

print(f"\n",double)
print(triple)
print(square)

fruit=["apple", "mango", "orange"]
fruit=[fruit[4] for fruit in fruit]
fruit=[fruit.upper() for fruit in fruit]

print(fruit)

values=[1,2,-3,4,-6,5]

positive_nums=[nums for nums in values if nums>=0]
negative_nums=[nums for nums in values if nums<0]
even_nums=[nums for nums in values if nums%2==0]
odd_nums=[nums for nums in values if nums%2!=0]

print(f"\n", positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

cube=lambda x: x*x*x

l=[1,2,3,4,5,6]
newl=list(map(cube, l))

print(newl)

filter_fun=lambda x:x>2

nnewl= list(filter(filter_fun, l) )
print(nnewl)


from functools import reduce

num=[1,2,3,4,5]

sum=lambda x,y: x+y
nnw=reduce(sum, num)
print(nnw)

fruits={"apple":"56", "mango":"65", "orange":"75"}

fruits=dict(sorted(fruits.items()))
fruits=dict(sorted(fruits.items(), key=lambda item:item[0], reverse=True))
fruits=dict(sorted(fruits.items(), key=lambda item:item[1], reverse=True))

print (fruits)

data= dict(zip(fruit,fruits))
print(data)

for fruit in enumerate(fruit):
    print(fruit)


try:
    x=int(input("enter a value:"))
    print(10/x)
except ValueError:
    print("insert correct value")
except ZeroDivisionError:
    print("please enter value other than zero")
else:
    print("No errors!")