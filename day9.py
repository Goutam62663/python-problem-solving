'''1. Smart Credit Card Approval System
A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. 
If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. 
If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.
If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card'''

'''inc=int(input("Income = "))
cs=int(input("Credit Score = "))
et=input("Employment(private/government) = ").lower()
debt=int(input("Debt = "))
if inc >= 50000 :
	if cs >= 750 :
		if debt < 20000 :
			print("Premium Card")
		else :
			print("Gold Card")
	else :
		if et == "government" :
			if cs >= 650 :
				print("Gold Card")
			else :
				print("Rejected")
		else :
			print("Rejected")
else :
	if inc >= 30000 :
		if cs >= 700 :
			print("Silver Card")
		else :
			print("Rejected")
	else :
		print("Rejected")'''

'''2. Hospital Emergency Priority System
A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.
If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.
If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes
Output:
Treatment = Immediate ICU'''

'''age=int(input("Age="))
severity=input("Severity=").lower()
ins=input("Insurance(y/n)=").lower()
if severity == "critical" :
	if age >= 60 :
		print("Immediate ICU")
	else :
		print("Emergency Ward")
elif severity == "moderate" :
	if ins == 'y' :
		print("Priority Treatment")
	else :
		print("General Queue")
else :
	if age < 10 :
		print("Pediatric Priority")
	else :
		print("Wait")'''

'''3. Smart Scholarship Allocation System
A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. 
If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.
If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.
If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship'''

'''marks=int(input("Marks = "))
inc=int(input("Income = "))
cat=input("Category = ").lower()
if marks >= 85 :
	if inc <= 300000 :
		if cat != "general" :
			print("Full Scholarship")
		else :
			print("75% Scholarship")
	else :
		print("50% Scholarship")
elif marks >= 70 :
	if inc <= 200000 :
		print("50% Scholarship")
	else :
		print("25% Scholarship")
else :
	print("No scholarship is given")'''

'''4. Airline Ticket Pricing Engine
An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.
If class is economy, then check distance. If distance is greater than 1000, then check booking time. 
If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000'''

'''cls=input("Class=").lower()
dis=int(input("Distance="))
book=input("Booking=")

if cls == "business" :
	if dis > 1000 :
		print("Ticket price is 8000")
	else :
		print("Ticket price is 5000")
else :
	if dis > 1000 :
		if book == "early" :
			print("Ticket price is 4000")
		else :
			print("Ticket price is 5000")
	else :
		print("Ticket price is 2500")'''

'''5. Smart Exam Evaluation System
A student’s result depends on marks, attendance, and internal score.

If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. 
If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.
If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

Input:
Marks = 38
Attendance = 80
Internal = 26

Output:
Result = Reappear'''

'''marks=int(input("Marks="))
atd=int(input("Attendance="))
inter=int(input("Internal="))
if marks >= 40 :
	if atd >= 75 :
		if inter >= 20 :
			print("Result = Pass")
		else :
			print("Result = Grace Pass")
	else :
		print("Result = Detained")
else :
	if marks >= 35 :
		if inter >= 25 :
			print("Result = Reappear")
		else :
			print("Fail")
	else :
			print("Fail")'''

'''6. Banking Fraud Detection System
A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. 
If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.
If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.
If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)'''

'''amt=int(input("Transaction Amount = "))
loc=input("Location(Domestic/International) = ").lower()
dvc=input("Device(New/Old) = ").lower()
tc=int(input("Transaction Count = "))
act=input("Any Unusual  Activity(y/n)=").lower()

if amt >= 50000 :
	if loc == "international" :
		if dvc == "new" :
			if tc > 3 :
				print("Risk Level = High Risk (Blocked)")
			else :
				print("Risk Level = Medium Risk")
		else :
			print("Risk Level = Medium Risk")
	else :
		if loc == "domestic" :
			if tc > 5 :
				print("Risk Level = Medium Risk")
			else :
				print("Risk Level = Low Risk")
		else :
			print("Enter Currect Location")
else :
	if act == 'y' :
		if dvc == new :
			print("Risk Level = Medium Risk")
		else :
			print("Risk Level = Low Risk")
	else :
		print("Risk Level = Safe")'''

'''7. University Result Classification System
A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. 
If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.
If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.
If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction'''

'''marks=int(input("Marks="))
back=int(input("Backlogs="))
ps=int(input("Project Score="))

if marks >= 75 :
	if back == 0 :
		if ps >= 80 :
			print("Result = First Class with Distinction")
		else :
			print("Result = First Class")
	else :
		print("Result = First Class")
else :
	if marks >= 60 :
		if back <= 2 :
			print("Result = Second Class")
		else :
			print("Result = Pass")
	elif (marks >= 50 and marks <= 59) :
		print("Result = Pass")
	else :
		print("Result = Fail")'''

'''8. E-Commerce Dynamic Pricing System
An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. 
If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.
If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.
If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%'''

'''dmd=int(input("Demand="))
stk=int(input("Stock="))
ut=input("User Type(premium/not)=").lower()
fest=input("Festival(y/n)=").lower()

if dmd >= 80 :
	if stk < 50 :
		if ut == "premium" :
			if fest == 'y' :
				print("Discount = 20%")
			else :
				print("Discount = 10%")
		else :
			print("Discount = No")
	else :
		print("Discount = 5%")
elif (dmd >= 40 and dmd < 80) :
	if fest == 'y' :
		print("Discount = 10%")
	else :
		print("Discount = No")
else :
	if stk > 200 :
		print("Discount = 15%")
	else :
		print("Discount = No")'''

'''9. Smart Loan Eligibility System
A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. 
If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.
If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%'''

'''salary=int(input("Salary = "))
age=int(input("Age = "))
cs=int(input("Credit Score = "))
emi=int(input("EMI = "))
if salary >= 40000 :
	if (age >20 and age < 60) :
		if cs >= 750 :
			if emi <= (salary*0.40) :
				print("Loan Status = Approved at 8%")
			else :
				print("Loan Status = Approved at 10%")
		else :
			if cs >= 650 :
				print("Loan Status = Approved at 12%")
			else :
				print("Loan Status = Rejected")
	else :
		print("Loan Status = Rejected")
else :
	if salary >= 25000 :
		if cs >= 700 :
			print("Loan Status = Approved at 13%")
		else :
			print("Loan Status = Rejected")
	else :
		print("Loan Status = Rejected")'''
		

'''10. Military Recruitment Fitness System
Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. 
If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.
If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.
If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected'''

'''age=int(input("Age="))
bmi=int(input("BMI="))
rt=int(input("Running Time="))
mc=input("Medical Condition=").lower()

if (age >= 18 and age  <= 25) :
	if (bmi >= 18 and bmi <= 25) :
		if rt <=15 :
			if mc == "fit" :
				print("Selection Status = Selected")
			else :
				print("Selection Status = Medical Rejected")
		else :
			print("Selection Status = Physical Fail")
	else :
		print("Selection Status = BMI Fail")
else :
	if (age >= 26 and age <= 30) : 
		if rt <= 14 :
			if mc == "fit" :
				print("Selection Status = Conditionaly Selected")
			else :
				print("Selection Status = Rejected")
		else :
			print("Selection Status = Rejected")
	else :
		print("Not Eligible")'''



		
	

