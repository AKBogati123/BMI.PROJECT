height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (weight / (height**2))
a = round(bmi)
if bmi<18.5 :
    print(f"your BMI is{a} ,you have a underweight")
elif bmi<25:
    print(f"your BMI is {a},you have a Normal weight")
elif bmi<30:
    print(f"your BMI is {a},you are slightly overweight.")
elif bmi<35 :
    print(f"your BMI is {a},you have a obese")
else:
    print(f"your BMI is {a},you have a Clinically obese.")