myage = "5"
b= int (5)
c= b+b
print(c)

num1 = input("enter temperature in Celsius ")
convert= float(num1)
temperature = convert* 9/5 + 32

num2 = input ("enter km ")
km_convert=float(num2)
Miles=km_convert* 0.62137


num4= input("enter weight(kg) ")
num5= input ("enter height(m) ")

weight_convert= float(num4)
height_convert= float(num5)

bmi= weight_convert/(height_convert **2)

if bmi < 18.5:
    bmi_level = "Underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    bmi_level = "Normal"
elif bmi >= 25 and bmi <= 29.9:
    bmi_level = "Overweight"
else:
    bmi_level = "Obese"

if temperature <=32:
    temp_level ="Cold"
elif temperature >=32 and temperature <=50:
    temp_level = "Cold/Mid"
elif temperature  >=50 and temperature <=68:
    temp_level = "Mid/Mild"
elif temperature >=68 and temperature <=85:
    temp_level = "Warm/hot"
elif temperature >=85 and temperature <=105:
    temp_level = "Very hot"
elif temperature >= 105:
    temp_level = "Extermely hot"
else :print("enter a value")
convert= None

print(f"temperature in Fahrenheit: {temperature} F")
print(f"level of temperature is: {temp_level}")
print(f"distance in miles {Miles}")
print(f"bmi is {round(bmi, 1)} and ur classify bmi level is {bmi_level}")

