'''1.Multiplication Table Generator
Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9'''
'''num=int(input("Enter the number="))
for i in range(1,num+1) :
	print("Table of:",i)
	for j in range(1,11) :
		print(i*j,end=" ")
	print()'''


'''2.Perfect Number Analyzer
A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''

'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))

for i in range(x,y+1) :
	sum=0
	for j in range(1,i//2+1) :
		if i%j==0:
			sum=sum+j
	if sum==i :
		print(i)'''

'''3.Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47'''

'''x=int(input("Enter starting number="))		
y=int(input("Enter ending number="))
for i in range(x,y+1) :
	flag=1
	if i > 1 :
		for j in range(2,i//2+1) :
			if i % j == 0 :
				flag=0
				break
		else :
			flag=1
		if flag == 1:
			print(i,end="  ")'''
		
'''4.Armstrong Number Finder
A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''
'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))
for i in range(x,y+1) :
	total=0
	temp=i
	power=len(str(i))
	while temp > 0 :
		digit=temp%10
		total=total+digit**power
		temp=temp//10
	if total == i :
		print(i)'''
	

'''5.Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145'''
'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))
for i in range(x,y+1) :
	temp=i
	total=0
	while temp > 0 :
		digit=temp%10
		fact=1
		for j in range(digit,0,-1) :
			fact=fact*j
		total=total+fact
		temp=temp//10
	if total == i :
		print(i)'''
'''6.Palindrome Number Range Checker
A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''

'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))
for i in range(x,y+1) :
	temp=i
	rev=0
	while temp > 0:
		rem=temp%10
		rev=rev*10+rem
		temp=temp//10
	if i == rev :
		print(i,end=" ")'''

'''7.Neon Number Detector
Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9'''

'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))
for i in range(x,y+1) :
	sqr=i**2
	sum=0
	while sqr > 0 :
		rem=sqr%10
		sum=sum+rem
		sqr=sqr//10
	if i == sum :
		print(i)'''

'''8.Online Exam Result Processing System
An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277'''


'''cls=int(input("Enter number of classes:"))
std=int(input("Enter students per class="))
sub=int(input("Enter subjects per student="))
for i in range(1,cls+1) :
	print("Class",i,end="\n")
	for j in range(1,std+1) :
		print("Student",j,end="\n")
		sum=0
		for k in range(1,sub+1) :
			s=int(input("Enter Marks="))
			sum=sum+s
		print("Total=",sum)
	print()'''
			
