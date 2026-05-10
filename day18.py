'''1. Adjacent Digit Difference Analyzer
A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''
'''num=input("Enter the number=")
first_diff = abs(int(num[1]) - int(num[0]))
uniform=True

count=0
max_diff=0
print("Differences=",end=" ")
for i in range(len(num)-1) :
	diff=abs(int(num[i])-int(num[i+1]))
	if first_diff != diff :
		uniform=False
	if max_diff < diff :
		max_diff=diff
	print(diff,end=" ")
	
	if diff % 2 == 0:
		count+=1
	
print("\nEven Differences Count =",count)
print("Max Difference = ",max_diff)
if uniform:
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")'''

'''2. Digit Sum Mirror Checker
A validation system checks symmetry in digit sums.
Write a program to:
Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''

'''num = input("Enter number: ")

mid = len(num) // 2

first_half = num[:mid]
second_half = num[mid:]

sum1 = 0
sum2 = 0

for i in first_half:
    sum1 += int(i)

for i in second_half:
    sum2 += int(i)

print("First Half Sum =", sum1)
print("Second Half Sum =", sum2)

if sum1 == sum2:
    print("Balanced Number")
else:
    print("Unbalanced Number")'''

'''3.Digit Neighbor Sum Analyzer
A system analyzes the relationship between a digit and its immediate neighbors.
Write a program to:
Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121324

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found'''

'''num = input("Enter number: ")
count = 0
print("Matching Digits:", end=" ")
for i in range(1, len(num) - 1):
    left = int(num[i - 1])
    current = int(num[i])
    right = int(num[i + 1])

    if current == left + right:
        print(current, end=" ")
        count += 1

print()

print("Count =", count)

if count == 0:
    print("No Matching Digit")
else:
    print("Neighbor Sum Pattern Found")'''


'''4.Digit Gap Analyzer
A system analyzes the gap between consecutive digits.
Write a program to:
Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number'''

'''num = input("Enter number: ")
count = 0
max_diff = 0
print("Differences:", end=" ")
for i in range(len(num) - 1):
    diff = abs(int(num[i]) - int(num[i + 1]))
    print(diff, end=" ")

    if diff > 2:
        count += 1

    if diff > max_diff:
        max_diff = diff

print()

print("Count (>2) =", count)
print("Max Difference =", max_diff)

if max_diff <= 2:
    print("Smooth Number")
else:
    print("Irregular Pattern")'''

'''5.Tech Number Checker
A number is called a Tech Number if:
It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:
Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''

'''num = input("Enter number: ")
digits = len(num)
if digits % 2 == 0:
    mid = digits // 2

    first_half = int(num[:mid])
    second_half = int(num[mid:])

    total = first_half + second_half

    square = total * total

    print("First Half =", first_half)
    print("Second Half =", second_half)
    print("Sum =", total)
    print("Square =", square)

    if square == int(num):
        print("Tech Number")
    else:
        print("Not a Tech Number")

else:
    print("Number does not have even digits")''


n = int(input("Enter number: "))
s=str(n)
for i in range(0,len(s)):
     if i%2==0:
         sum = sum+int(s[i])
     else:
          sum=sum-int(s[i])
print("Result = ",sum)
if sum>0:
      print("Positive Number")
else:
     print("Negative Number")'