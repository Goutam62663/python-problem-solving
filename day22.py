'''1)WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''
'''x=int(input("Enter starting number="))
y=int(input("Enter ending number="))
sum=0
for i in range(x,y+1) :
	if i%9==0 :
		sum=sum+i
print("Sum=",sum)'''

'''2) WAP to print Square, Cube and Square Root of all numbers from 1 to N'''

'''import math
x=int(input("Enter the number="))
for i in range(1,x+1) :
	print("Number=",i)
	print("Square=",i**2)
	print("Cube=",i**3)
	print("Square Root=",math.sqrt(i))'''

'''3) WAP to find out all the leap years between two entered years'''

'''x=int(input("Enter starting year="))
y=int(input("Enter ending year="))
for i in range(x,y+1) :
	if i%4== 0 and i%400==0 and i%100==0:
		print(i)
	elif i%4==0 :
		print(i)'''
	

'''4)
1
00
111
0000
11111'''

'''num=int(input("Enter total number of lines="))
i=1
for i in range(i,num+1) :
	j=1
	for j in range(1,i+1) :
		if i%2==0 :
			print("0",end=" ")
		else :
			print("1",end=" ")
	print()'''

'''5)
A
AB
ABC
ABCD
ABCDE'''

'''x=int(input("Enter total number of lines="))
for i in range(1,x+1) :
	ch=65
	for j in range(1,i+1) :
		print(chr(ch),end=" ")
		ch=ch+1
	print()'''

'''6)
a
ab
abc
abcd
abcde'''
'''x=int(input("Enter total number of lines="))
for i in range(1,x+1) :
	ch=97
	for j in range(1,i+1) :
		print(chr(ch),end=" ")
		ch+=1
	print()'''

'''7. enter n6
     *
    **
   ***
  ****
 *****
******'''
'''x=int(input("Enter total number of lines="))
num=x
for i in range(1,x+1) :
	for j in range(1,(num-i)+1) :
		print(" ",end=" ")
	for k in range(1,i+1) :
		print("*",end=" ")
	print()'''

'''8. enter n6
 654321
  65432
   6543
    654
     65'''
'''x=int(input("Enter the number of lines="))
for i in range(1,x+1) :
	for k in range(1,i+1) :
		print(" ",end=" ")
	for j in range(6,i-1,-1) :
		print(j,end=" ")
	print()'''
	

'''9.
    1
   10
  101
 1010
10101'''
'''x=int(input("Enter total number of lines="))
for i in range(1,x+1) :
	for j in range(1,x-i+1) :
		print(" ",end=" ")
	digit=1
	for k in range(1,i+1) :
		print(digit,end=" ")
		digit=1-digit
	print()'''

'''10.enter number6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4'''

'''x=int(input("Enter total number of lines="))
for i in range(1,x+1) :
	for j in range(0,i) :
		print(j,end=" ")
	print()'''