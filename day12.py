'''1. Product of Odd Numbers up to N
A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''
'''num=int(input("Enter the number="))
pro=1
for i in range(1,num+1) :
	if i % 2 != 0 :
		pro=pro*i
print("Product of odd numbers=",pro)'''


'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''
'''num1=int(input("Enter first number="))
num2=int(input("Enter second number="))
count=0
for i in range(num1,num2+1) :
	if i % 7 == 0 :
		count+=1
print("Count=",count)'''


'''3. Display Numbers Ending with 5
A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35'''
'''num1=int(input("Enter first number="))
num2=int(input("Enter second number="))
for i in range(num1,num2+1) :
	if i % 5 == 0  and i % 10 != 0:
		print(i,end=" ")'''

	


'''4. Strong Number Checker

A digital lock opens only for strong numbers.
A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number'''
'''num = int(input("Enter a number: "))

temp = num
sum_fact = 0

# Loop through each digit
while temp > 0:
    digit = temp % 10

    # Calculate factorial using loop
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum_fact = sum_fact + fact
    temp = temp // 10

# Check Strong Number
if sum_fact == num:
    print("Strong Number")
else:
    print("Not a Strong Number")'''

'''5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. 
To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. 
Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number'''
'''num=int(input("Enter number="))
temp=num
sum=0
while num > 0 :
	rem=num%10
	sum=sum+rem
	num=num//10
print("Sum=",sum)
if  temp % sum == 0 :
	print(temp,"is a Harshad Number.")
else :
	print("Not")'''


'''6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. 
When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. 
If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number'''


'''num = int(input("Enter a number: "))

square = num * num
temp_num = num
temp_square = square

is_automorphic = True

# Compare digits from last using loop
while temp_num > 0:
    if temp_num % 10 != temp_square % 10:
        is_automorphic = False
        break

    temp_num = temp_num // 10
    temp_square = temp_square // 10

# Output result
if is_automorphic:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")'''
'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. 
Coupon numbers containing at least one zero in between digits are considered special duck numbers. 
However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''

'''# Input from user (as string to check leading zero)
num = input("Enter a number: ")

# Check if number starts with 0
if num[0] == '0':
    print("Not a Duck Number")
else:
    has_zero = False

    # Loop through digits
    for digit in num:
        if digit == '0':
            has_zero = True
            break

    # Final check
    if has_zero:
        print("Duck Number")
    else:
        print("Not a Duck Number")'''


'''8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified'''

'''# Input from user
num = int(input("Enter Transaction ID: "))

# Step 1: Reverse the number using loop
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

# Step 2: Find absolute difference
difference = abs(num - reverse)

# Step 3: Count digits in difference using loop
count = 0
temp_diff = difference

# Special case when difference = 0
if temp_diff == 0:
    count = 1
else:
    while temp_diff > 0:
        count += 1
        temp_diff = temp_diff // 10

# Step 4: Print results
print("Reverse =", reverse)
print("Difference =", difference)
print("Digits =", count)

# Step 5: Conditions
if difference == 0:
    print("Perfect Match")
elif difference % 9 == 0:
    print("Verified")
else:
    print("Rejected")'''

'''9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''
# Input from user
num = int(input("Enter a number: "))

# Count digits
temp = num
digit_count = 0
while temp > 0:
    digit_count += 1
    temp = temp // 10

# Process step differences
temp = num
prev_digit = temp % 10
temp = temp // 10

sum_diff = 0
largest = 0

print("Step Differences:", end=" ")

while temp > 0:
    current_digit = temp % 10
    
    diff = abs(current_digit - prev_digit)
    
    print(diff, end=" ")
    
    sum_diff += diff
    
    if diff > largest:
        largest = diff
    
    prev_digit = current_digit
    temp = temp // 10

print()  # for new line

# Print results
print("Sum =", sum_diff)
print("Largest =", largest)

# Check Balanced or Unbalanced
if sum_diff % digit_count == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")