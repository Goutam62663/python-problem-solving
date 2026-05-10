'''1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. 
This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.
input: n = 10
Output: Total Points = 55'''

'''num=int(input("Enter a Number="))
sum=0
for i in range(1,num+1) :
	sum=sum+i
print("Total Points/Sum of n natural numbers=",sum)'''

'''2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. 
Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120'''

'''n=int(input("Enter a number="))
fact=1
for i in range(1,n+1) :
	fact=fact*i
print("Factorial of", n," is ",fact)'''

'''3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60'''

'''n=int(input("Enter a number="))
for i in range(1,11) :
	print(n*i)'''

'''4. Reverse a Number
A security system stores OTP codes in reverse format for encryption to increase data safety. 
Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321'''

'''n=int(input("Enter Numer="))
reverse=0
while n > 0 :
	rem=n%10
	reverse=reverse*10+rem
	n=n//10
print(reverse)'''

'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. 
Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome'''

'''n=int(input("Enter Numer="))
original=n
reverse=0
while n > 0 :
	rem=n%10
	reverse=reverse*10+rem
	n=n//10
if original == reverse :
	print("Palindrome")
else :
	print("Not")'''

'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. 
A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''
#NOTE:- An Armstrong number (or narcissistic number) is a number that equals the sum of its own digits, each raised to the power of the total number of digits.
'''num=int(input("Enter a number="))
pow=len(str(num))
original=num
sum=0
while num > 0 :
	rem=num%10
	sum=sum+rem**pow
	num=num//10
print("The sum of the cubes of its digits = ",sum)
if original == sum :
	print(original,"is an Armstrong number")
else : 
	print("Not an Armstrong number.")'''


'''7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3'''

'''n=int(input("Enter a number="))
count=0
while n > 0 :
	rem=n%10
	if rem%2 == 0 :
		count=count+1
	n=n//10
print("Even digits count = ",count)'''
	

'''8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3'''

'''n=int(input("Enter NUmber="))
count=0
while n > 0 :
	rem=n%10
	if rem%2 != 0 :
		count=count+1
	n=n//10
print("Odd digits count = ",count)'''


'''9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even'''

'''n=int(input("Enter Number="))
all_even=True

while n > 0 :
	rem=n%10
	if rem % 2 != 0 :
		all_even=False
		break
	n=n//10
	
if all_even :
	print("All Even")
else : 
	print("Not all even")'''
		
		
'''10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20'''

'''n1=int(input("Enter Num1="))
n2=int(input("Enter Num2="))
for i in range(n1,n2+1,2) :
	print(i,end=" ")'''

'''11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3'''


'''12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, 
the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even'''
'''n=int(input("Enter The Number="))
pro=1
while n > 0 :
	rem=n%10
	pro=pro*rem
	n=n//10
print("Product=",pro)
if pro % 2 == 0 :
	print("Even")
else :
	print("Odd")'''



'''13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same'''

'''n1=int(input("Enter Num1 = "))
n2=int(input("Enter Num2 = "))
if n1 > n2 :
	for i in range(n1,n2-1,-1) :
		print(i)
elif n1 < n2 :
	for i in range(n1, n2+1-1) :
		print(i)
else :
	print("Both numbers are same")'''



'''14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor'''

curr=int(input("Enter Current Floor="))
des=int(input("Enter Destination Floor="))
if curr < des :
	for i in range(curr,des+1) :
		print(i,end=" → ")
elif curr > des :
	for i in range(curr,des-1,-1) :
		print(i,end=" → ")
else :
	print("Already on the same floor")

