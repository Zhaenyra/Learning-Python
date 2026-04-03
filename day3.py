# Day3  - Conditional Logic
# Classwork — If Statements 
# Question 1 — Positive, Negative or Zero
num=float(input("Enter a number:"))
if num>0:
    print("This is a positive number")
elif num==0:
    print("This is zero")
else:
    print("This is a negative number")
# Question 2 — Voting Eligibility
name=input("What is your name? ")
age=int(input("How old are you? "))
if age>=18:
    print(f"{name} you are eligible to vote")
else:
    print(f"{name} you cannot vote yet, come back in {18-age} years!")
# Question 3 — Grade Calculator
score=float(input("What is your score?"))
if score>=90:
    print("Your grade is A")
elif score>=80:
    print("Your grade is B")
elif score>=70:
    print("Your grade is C")
elif score>=60:
    print("Your grade is D")
else:
    print("Your grade is F")
# Question 4 — Login System
username=input("Username ")
password=input("Password ")
if username == "admin":
    if password == "python123":
        print("Welcome back admin!")
    else:
        print("Wrong password!")
else:
    print("Username not found!")
# Question 5 — Shopping Discount  
totalprice=int(input("Enter total price: "))
if totalprice>= 50000:
    discount= 0.2*totalprice
elif totalprice>= 30000:
    discount= 0.1*totalprice
elif totalprice>= 10000:
    discount= 0.05*totalprice
else:
    discount= 0
print(f"Original price: ₦{totalprice}")
print(f"Discount:       ₦{discount}")
print(f"Final price:    ₦{totalprice-discount}")
# Question 6 — BMI Calculator with Category
name=input("Enter your name: ")
weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in m: "))
bmi=weight/(height**2)
if bmi<=18.5:
    category= "Underweight"
elif bmi<=24.9:
    category= "Normal weight"
elif bmi<=29.9:
    category= "Overweight"
else:
    category= "Obese"
print(f"{name} your BMI is {round(bmi,2)} and you are {category}.")