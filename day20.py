'''1. Utility Toolkit System
You are developing a Utility Toolkit Application for a small office. 
Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.
The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions'''
'''while True :
	print("1 → Check Prime Number")
	print("2 → Check Palindrome Number")
	print("3 → Reverse a Number")
	print("4 → Count Digits")
	print("5 → Exit")
	num=int(input("Enter the choise="))
	match num :
		case 1 :
			n=int(input("Enter the number="))
			for i in range(2,n//2) :
				if n%i == 0 :
					print("Not Prime  Number")
					break
			else :
				print("Prime Number")
		case 2 :
			n=int(input("Enter the number="))
			temp=n
			rev=0
			while n > 0 :
				rem=n%10
				rev=rev*10+rem
				n=n//10
			if temp == rev :
				print("Palindrome Number")
			else :
				print("Not Palindrome Number")
		case 3 :
			n=int(input("Enter the number="))
			rev=0
			while n > 0 :
				rem=n%10
				rev=rev*10+rem
				n=n//10
			print("Reverse Number=",rev)
		case 4 :
			n=int(input("Enter the number="))
			count=0
			while n > 0 :
				rem=n%10
				count+=1
				n=n//10
			print("Total Digits=",count)
		case 5 :
			print("Exiting program... Thank you!")
			break
		case _:
			print("Wrong Choise")'''
			
			
					

'''2.Employee Salary Processor

Scenario:
You are developing an Employee Salary Processing System for a company’s HR department. 
The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.
The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. 
Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit

---

Sample Run 1:
Input:
Enter your choice: 3

Output:
Please enter basic salary first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter Basic Salary: 40000

Output:
Basic Salary recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
HRA: 8000
DA: 4000

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Net Salary (before tax): 52000

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Tax Deduction: 5200

---

Sample Run 6:
Input:
Enter your choice: 5

Output:
----- Salary Slip -----
Basic Salary: 40000
HRA: 8000
DA: 4000
Net Salary: 52000
Tax: 5200
Final Salary: 46800

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 6

Output:
Exiting program... Thank you!'''

'''while True :
		print("1 → Enter Basic Salary")
		print("2 → Calculate HRA (20%) and DA (10%)")
		print("3 → Calculate Net Salary")
		print("4 → Tax Deduction")
		print("5 → Display Salary Slip")
		print("6 → Exit")
		salary=None
		hra=0
		da=0
		net_salary=0
		td=0
		fs=0
		choice=int(input("Enter your choise="))
		match choice :
				case 1 :
					salary = float(input("Enter Basic Salary: "))
					print("Basic Salary recorded successfully")
				case 2 :
					if salary is None :
						print("Please enter basic salary first")
					else :
						hra=salary * 0.20
						da=salary * 0.10
						print("HRA=",hra,"\nDA=",da)
				case 3 :
					if salary is None :
						print("Please enter basic salary first")
					else :
						net_salary=hra+da+salary
						print("Net Salary (before tax)=",net_salary)
				case 4 :
					if salary is None :
						print("Please enter basic salary first")
					else :
						if net_salary > 50000 :
							td=net_salary * 0.10
							print("Tax Deduction=",td)
						else :
							td=net_salary*0.05
							print("Tax Deduction=",td)
				case 5 :
					if salary is None :
						print("Please enter basic salary first")
					else :
						print("\n----- Salary Slip -----")
						print("Basic Salary=",salary)
						print("HRA=",hra)
						print("DA=",da)
						print("Net Salary=",net_salary)
						print("Tax=",td)
						fs=net_salary-td
						print("Final Salary=",fs)
				case 6 :
					print("Exiting program... Thank you!")
					break
				case _:
					print("Invalid choice. Please try again.")'''

''' 3.Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.
Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!'''

'''balance = None

while True:

    print("\n----- Smart Banking System -----")
    print("1 → Deposit Money")
    print("2 → Withdraw Money")
    print("3 → Check Balance")
    print("4 → Apply Interest")
    print("5 → Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            amount = float(input("Enter amount to deposit: "))
            balance = amount
            print("Amount deposited successfully")

        case 2:
            if balance is None:
                print("No balance available. Please deposit first")

            else:
                withdraw = float(input("Enter amount to withdraw: "))

                if withdraw > balance:
                    print("Insufficient balance")

                else:
                    balance = balance - withdraw
                    print("Withdrawal successful")

        case 3:
            if balance is None:
                print("No balance available. Please deposit first")

            else:
                print("Current Balance:", balance)

        case 4:
            if balance is None:
                print("No balance available. Please deposit first")

            else:
                if balance > 50000:
                    interest = balance * 0.05

                else:
                    interest = balance * 0.03

                balance = balance + interest

                print("Interest added:", interest)
                print("Updated Balance:", balance)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")'''

'''4. Electricity Bill Management System
You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.
Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!'''
units = None
bill = 0
surcharge = 0
total = 0

while True:

    print("\n----- Electricity Bill Management System -----")
    print("1 → Enter Units Consumed")
    print("2 → Calculate Bill Amount")
    print("3 → Apply Surcharge")
    print("4 → Display Final Bill")
    print("5 → Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            units = int(input("Enter units consumed: "))
            print("Units recorded successfully")

        case 2:
            if units is None:
                print("Please enter units consumed first")

            else:

                if units <= 100:
                    bill = units * 5

                elif units <= 200:
                    bill = (100 * 5) + ((units - 100) * 7)

                else:
                    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

                print("Bill Amount:", bill)

        case 3:
            if units is None:
                print("Please enter units consumed first")

            else:
                if bill > 2000:
                    surcharge = bill * 0.10

                else:
                    surcharge = bill * 0.05

                print("Surcharge:", surcharge)

        case 4:
            if units is None:
                print("Please enter units consumed first")

            else:
                total = bill + surcharge

                print("\n----- Final Bill -----")
                print("Units:", units)
                print("Bill Amount:", bill)
                print("Surcharge:", surcharge)
                print("Total Payable:", total)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")