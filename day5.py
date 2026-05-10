'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth'''

'''Age=int(input("Enter Your Age="))
if Age >= 18 :
	print("Eligible to vaote.")
Id=input("Do you have ID (yes/no):")
if Id == "yes" :
	print("Allowed inside booth.")'''

'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction'''

'''Marks=int(input("Enter your marks:"))
if Marks >= 40 :
	print("Pass")
if Marks >= 75 :
	print("Distinction")'''

'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked'''

'''Price=int(input("Enter cart value="))
if Price >= 500 :
	print("Free delivery")
if Price >= 1000 :
	print("10% discount coupon.")'''

'''4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program'''

'''Age=int(input("Enter Age="))
BMI=int(input("Enter BMI="))
if Age >= 18 :
	print("Allowed for gym.")
if BMI > 25 :
	print("Enroll in weight loss program.")'''

'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password'''

'''username=input("Enter Username:")
password=input("Enter password:")
if username == "admin" :
	print("Valid user")
if len(password) >= 8 :
	print("Strong password")'''

'''6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert'''

'''Temp=int(input("Enter Temperature="))
Hum=int(input("Enter Humidity="))
if Temp >= 30 :
	print("Hot Day")
if Hum >= 75 :
	print("High humidity alert")'''

'''7. Salary Benefits System
   A company provides benefits:

* If salary = 30000 ? Eligible for PF
* If salary = 50000 ? Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable'''

'''Salary=int(input("Enter Your Salary=")) 
if Salary >= 30000 :
	print("Eligible for PF.")
if Salary >= 50000 :
	print("Eligible for bonus.")'''

'''8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 ? Even number
* If number % 5 == 0 ? Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5'''

'''Num=int(input("Enter Number="))

if Num%2 == 0 :
	print("Even Number")
if Num%5 == 0 :
	print("Divisible by 5")'''

'''9. Library Access System
   A library checks:

* If membership is active ? Entry allowed
* If books issued < 3 ? Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''

'''Check=input("Membership active (yes/no)=")
Book_Issue=int(input("Books issued="))
if Check == "yes" :
	print("Entry allowed.")
if Book_Issue < 3 :
	print("Can issue more books.")'''

'''10. Online Exam System
    System evaluates exam conditions:

* If marks >= 40 ? Pass
* If attendance >= 75 ? Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate'''

Marks=int(input("Enter Marks="))
Attendance=int(input("Enter Attendance="))
if Marks >= 40 :
	print("Pass")
if Attendance >= 75 :
	print("Eligible for certificate.")





