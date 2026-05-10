'''1. Triple Operation Prime Verification System
A cybersecurity company generates a security score from entered access code.
Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''
'''n=int(input("Enter the Number="))
num=n
sum=0
rev=0
while n > 0 :
    rem=n%10
    sum=sum+rem
    rev=rev*10+rem
    n=n//10
print("Sum=",sum)
print("Reverse=",rev)
if rev > num :
    diff=rev-num
else :
    diff=num-rev
print("Difference=",diff)
final_sum=sum+diff
print("Final Result=",final_sum)
if final_sum <= 1 :
    print("Not prime number")
else :
    for i in range(2,final_sum) :
        if final_sum % i == 0 :
            print("Not Prime Number")
            break
    else :
        print("Prime Number")'''



'''2. Multi Stage Prime Lock System
A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime'''
n=int(input("Enter the number="))
sum=0
pro=1
while n > 0 :
     rem=n%10
     sum=sum+rem
     pro=pro*rem
     n=n//10
print("Sum=",sum)
print("Product=",pro)
diff=pro-sum
temp_diff=diff
print("Difference=",diff)
count=0
while diff > 0 :
    rem=diff%10
    count+=1
    diff=diff//10
print("Digits=",count)
final_result=count+temp_diff
print("Final Result=",final_result)
if final_result <= 1 :
    print("Not Prime")
else :
    for i in range(2,final_result) :
        if final_result % i == 0 :
            print("Prime Number")
            break
    else :
        print("Prime")


'''3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked'''

'''n=int(input("Enter th number="))
temp=n
sum=0
for i in range(1,n//2+1) :
    if n%i==0 :
        sum=sum+i
else :
    if sum == temp :
        print("Reward Unlocked")
    else :
        print("Try Agian")'''

'''4.Unique Digit Security Scanner
A smart locker accepts only numbers whose all digits are unique.
Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code'''


'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number

6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29

7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime

8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7

9.
 Bike Service Kilometer Checker

A bike needs service every 3000 km.

Write a program to:

- Read travelled kilometers
- Print every service checkpoint till entered km

Input:
10000

Output:
3000 6000 9000


10.
Lift Mode Operation – Advanced Smart Elevator System

A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
The system must automatically execute floor movement instructions using loops.

Write a program:

- If mode = 1  
  Normal Up Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in ascending order.

- Else if mode = 2  
  Down Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in descending order.

- Else if mode = 3  
  Energy Saving Mode activated.  
  Read destination floor.  
  Lift starts from ground floor (0) and stops only on alternate floors till destination.

- Else  
  Emergency Mode activated.  
  Print "Emergency Alarm" 4 times using loop.

Input:
3
6

Output:
0 2 4 6


Input:
1
2
7

Output:
2 3 4 5 6 7


Input:
2
8
3

Output:
8 7 6 5 4 3


Input:
5

Output:
Emergency Alarm
Emergency Alarm
Emergency Alarm
Emergency Alarm'''