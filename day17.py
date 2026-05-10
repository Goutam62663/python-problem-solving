'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number

2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number


3.
Zero Detection & Early Termination System

A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

Write a program to:

Traverse each digit of the number from right to left
Display each digit processed before encountering 0
Stop the loop immediately when 0 is found using break
Count how many digits were processed before termination
If no zero is found, print No Zero Found

Use loops and break wherever required.

Input:
572049

Output:
Digits Processed: 9 4
Count = 2
Zero Found - Process Stopped

Input:
56789

Output:
Digits Processed: 9 8 7 6 5
Count = 5
No Zero Found

4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected

5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern'''

'''rev=int(input('enter a number= '))

num=0
while rev>0:
    t=rev%10
    num=num*10+t
    rev=rev//10


first=num%10
num=num//10
product=1
count=1
sum=0
smallest=num


while num>0:
    t=num%10
    product=first*t
    print(product,end=" ")
    sum+=product
    if product<smallest:
        smallest=product
    count+=1
    first=t
    num=num//10

print("\nsum is ",sum)
print("smaalest =",smallest)
if sum%count==0:
    print("stable number ")
else:
    print("unstable number")'''

'''num=int(input("enter a number ="))
count=len(str(num))
num1=num%10
num=num//10
print("count = ",count)
while num>0:
    count-=1
    t=num%10
    if t>num1:
        print("breaking at ",count)
        break
    else:
        num=num//10
else:
    print('strictly increasing number ')'''


'''num=int(input("enter a number "))
count=0
rev=0

while num>0:
    t=num%10
    
    if count ==0:
        print("Digit Process: ",end=" ")
    
    
    if t==0:
       
        print("\ncount",count)
        print("zero found process stop")
        break
    else:
        print(t,end=" ")
        count+=1
        num=num//10
else:
    
    print("\ncount",count)
    print("no zero found")'''


'''num=int(input("enter a number "))
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10


n1=rev%10
rev=rev//10
n2=rev%10
rev=rev//10
sub=abs(n1-n2)

while rev>0:
    t=rev%10
    sub2=abs(n2-t)
    if sub2!=sub:
        print('intial gap is ',sub)
        print("pattern break detected")
        break
    else:
        n2=t
        rev=rev//10
else:
    print("intial Gap is ",sub)
    print("Consistent pattern")'''


'''num=int(input("enter number "))
rev=0
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10

count=1
r1=0
r2=0
while rev>0:
    t=rev%10
    if count%2!=0:
        r1=r1+t
    else:
        r2=r2-t
    rev=rev//10
    count+=1

result=r1+r2
print("Result: ",result)
if result<0:
    print('Negative pattern')
else:
    print("Positive pattern ")'''

a=-11
print(a<<2)