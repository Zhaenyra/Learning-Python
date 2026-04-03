# Day  - Conditional Logic
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
    print("{name} you are eligible to vote")
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
totalprice=float(input("Enter total price: "))
print(f"Original price: #{totalprice}")
if totalprice>= 50,000:
    print(f"Discount:")