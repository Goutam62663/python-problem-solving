'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.'''

'''amt=int(input("Enter Amount="))
type=input("Enter customer type=").lower()
disc=(0.20 if amt > 5000 else 0.10) if type == "premium" else (0.10 if amt > 3000 else 0.05)
payable=amt-(amt*disc)
print("Payable Amount=",payable)'''


'''2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.'''

'''marks=int(input("Enter Marks="))
grade="A+" if marks >= 90 else "A" if marks >= 75 else "B" if marks >= 60 else "C" if marks >= 50 else "Fail"
print("Grade=",grade)'''

'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.'''

'''salary=int(input("Enter your salary="))
exp=int(input("Enter year of experience="))
bonus=salary*0.30 if exp > 10 else (salary*0.20 if exp > 5 else salary*0.10)
print("Total Salary=",salary+bonus)'''

'''4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.'''

'''units=int(input("Enter Units of consumed="))
pu=units*5 if units<=100 else (units*7 if units>100 and units<=300 else units*10)
print("Total Bill=₹",pu)'''

'''5.Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.'''

yr=int(input("Enter the year="))
print("Leap Year" if (yr%4==0 or yr%400==0 or yr%100==0) else "Not Leap year")

'''6.Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''
#1
'''amount = float(input("Enter purchase amount: "))
customer = input("Enter customer type (premium/regular): ").lower()

discount = (0.20 if amount > 5000 else 0.10) if customer == "premium" else (0.10 if amount > 3000 else 0.05)

final_amount = amount - (amount * discount)

print("Final Payable Amount =", final_amount)

#2
marks = int(input("Enter marks: "))

grade = "A+" if marks >= 90 else "A" if marks >= 75 else "B" if marks >= 60 else "C" if marks >= 50 else "Fail"

print("Grade =", grade)

#3
salary = float(input("Enter salary: "))
experience = int(input("Enter years of experience: "))

bonus = 0.30 if experience > 10 else 0.20 if experience > 5 else 0.10

total_salary = salary + (salary * bonus)

print("Total Salary After Bonus =", total_salary)

#4
units = int(input("Enter electricity units: "))

bill = units * 5 if units <= 100 else units * 7 if units <= 300 else units * 10

print("Total Electricity Bill = ₹", bill)

#5
year = int(input("Enter year: "))

result = "Leap Year" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "Not a Leap Year"

print(result)

#6
ch = input("Enter a character: ")

result = "Alphabet" if ch.isalpha() else "Digit" if ch.isdigit() else "Special Character"

print(result)'''