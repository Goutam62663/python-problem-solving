"""1. Electricity Department Billing System

The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950"""


"""2. College Result Processing System

A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C """

"""marks=int(input("Enter Marks="))
if marks >= 90 :
	print("Grade A")
elif marks >= 75 and marks <= 89 :
	print("Grade B")
elif marks >= 60 and marks <= 74 :
	print("Grade C")

elif marks >= 50 and marks <= 59 :
	print("Grade D")
elif marks < 50 :
	print("Fail")"""

"""3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000"""
"""# Input from user
income = int(input("Enter annual income: "))

tax = 0

# Tax calculation based on slabs
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

# Output
print("Tax Payable: ₹", int(tax))"""

"""4. E-Commerce Discount Engine

An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050"""
"""PA=int(input("Enter purchase amount="))
if PA > 5000 :
	DC=PA*0.20
	FA=PA-DC
	print("Final Amount=",FA)
elif PA >= 2000 : 
	DC=PA*0.10
	FA=PA-DC
	print("Final Amount=",FA)
else : 	
	DC=PA*0.05
	FA=PA-DC
	print("Final Amount=",FA)"""

"""5. Cinema Ticket Booking System

A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100"""
"""age=int(input("Enter Age="))
if age < 12 :
	print("Ticket Price= ₹100")
elif age <= 60 :
	print("Ticket Price= ₹200")
else :
	print("Ticket Price= ₹150")"""

"""6. Company Bonus Distribution System
A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000"""

"""salary=int(input("Enter salary="))
exp=int(input("Enter years of experience="))
if exp < 2 :
	print("No Bonus")
elif exp <= 5 :
	bonus=salary*0.05
	print("Bonus Amount=",bonus)
elif exp <= 10 :
	bonus=salary*0.10
	print("Bonus Amount=",bonus)
else :
	bonus=salary*0.20
	print("Bonus Amount=",bonus)"""

"""7. Banking Withdrawal Limit System

A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000"""
"""amount=int(input("Enter account balance="))
if amount <= 1000 :
	print("Withdrawal not allowed")
elif amount <= 5000 :
	print("Maximum withdrawal ₹1000")
else : 
	print("Maximum withdrawal ₹5000")"""

"""8. Weather Monitoring System
A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot"""
"""temp=int(input("Enter temperature="))
if temp < 0 :
	print("Freezing")
elif temp <= 20 :
	print("Cold")
elif temp <= 35 :
	print("Warm")
else :
	print("Hot")"""

"""9. Student Attendance Eligibility System
A college determines whether a student is eligible to sit for exams based on attendance percentage:
* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible"""
"""attendance=int(input("Enter attendance percentage="))
if  attendance >= 75 :
	print("Eligible")
elif  attendance >= 60 :
	print("Eligible with warning")
else :
	print("Not eligible")"""

"""10. Mobile Data Plan Advisor
A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan"""
"""data=int(input("Enter daily data usage="))
if data >= 3 :
	print("Premium Plan")
elif data >= 1 :
	print("Standard Plan")
else :
	print("Basic Plan")"""

"""11. Railway Ticket Fare System

A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600"""

"""dist=int(input("Enter distance="))
cls=input("Enter class=").lower()
if dist <= 100 :
	if cls == "sleeper" :
		print("Total Fare= ₹100")
	else :
		print("Total Fare= ₹200")
elif dist <= 500 :
	if cls == "sleeper" :
		print("Total Fare= ₹300")
	else :
		print("Total Fare= ₹600")
else : 
	if cls == "sleeper" :
		print("Total Fare= ₹500")
	else :
		print("Total Fare= ₹1000")"""

"""12. Restaurant Bill with GST System
A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680"""

'''amount=int(input("Enter bill amount="))
if amount <= 1000 :
	gst=amount*0.05
	amount+=gst
	print("Final Bill Amount=",amount)
elif amount <= 5000 :
	if amount > 3000 :
		gst=amount*0.12
		amount+=gst
		sc=200
		print("Final Bill Amount=",(amount+sc))
	else :
		gst=amount*0.12
		amount+=gst
		print("Final Bill Amount=",amount)
else : 
	gst=amount*0.12
	amount=amount+gst
	print("Final Bill Amount=",amount)'''
	
'''13. Employee Performance Appraisal System
A company evaluates employees based on performance rating (1 to 5):

* 5 25% salary hike
* 4  20% salary hike
* 3  10% salary hike
* 2  5% salary hike
* 1  No hike
  If salary is below 20000 and rating is 4 or above, an additional 2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: 23600'''

'''salary=int(input("Enter salary:="))
rating=int(input("Enter rating:="))
if salary < 20000 :
	if rating >= 4 :
		hike=salary*0.25
		salary+=hike+2000
		print("Revised Salary=",salary)
	else :
		if rating == 3 :
			hike=salary*0.10
			salary+=hike
			print("Revised Salary=",salary)
		elif rating == 2:
			hike=salary*0.05
			salary+=hike
			print("Revised Salary=",salary)
		else :
			print("Revised Salary=",salary)
else :
		if rating == 5 :
			hike=salary*0.25
			salary+=hike
			print("Revised Salary=",salary)
		elif rating == 4 :
			hike=salary*0.20
			salary+=hike
			print("Revised Salary=",salary)
		elif rating == 3 :
			hike=salary*0.10
			salary+=hike
			print("Revised Salary=",salary)
		elif rating == 2:
			hike=salary*0.05
			salary+=hike
			print("Revised Salary=",salary)
		else :
			print("Revised Salary=",salary)'''

'''14. Online Course Fee System
An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000

  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Studentmi

Output:
Final Course Fee: ₹4000'''
'''course=input("Enter course category=").lower()
profession=input("Enter user type=").lower()
if course == "programming" :
	if profession == "student" :
		dc=5000*0.20
		fees=5000-dc
		print("Final Course Fee=",fees)
	elif profession == "working" :
		dc=5000*0.10
		fees=5000-dc
		print("Final Course Fee=",fees)
	else :
		print("Final Course Fee=5000")
elif course == "design" :
	if profession == "student" :
		dc=4000*0.20
		fees=4000-dc
		print("Final Course Fee=",fees)
	elif profession == "working" :
		dc=4000*0.10
		fees=4000-dc
		print("Final Course Fee=",fees)
	else :
		print("Final Course Fee=4000")
else :
	if profession == "student" :
		dc=3000*0.20
		fees=4000-dc
		print("Final Course Fee=",fees)
	elif profession == "working" :
		dc=3000*0.10
		fees=4000-dc
		print("Final Course Fee=",fees)
	else :
		print("Final Course Fee=3000")'''

'''15. Smart Parking System
A smart parking system charges based on vehicle type and parking duration:
* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.
Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''

	
	
	




		