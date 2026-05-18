 #1
'''num=int(input("Enter Number="))
for i in range(1,num+1) :
	print("*",end=" ")'''

#2
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	print("*",end="\n")'''

#3
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for s in range(1,i) :
		print(" ",end=" ")
	for j in range(i,i+1) :
		print("*")
	print()'''

#4
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for s in range(1,row+1) :
		print("*",end=" ")
	print()'''

#5
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for n in range(1,row+1) :
		print(n,end="")
	print()'''

#6
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for n in range(1,row+1) :
		print(i,end="")
	print()'''

#7
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for n in range(1,i+1):
		if i%2==0 :
			print("0",end="")
		else :
			print("1",end="")
	print()'''

#8
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print("*",end="")
	print()'''

#9
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(j,end="")
	print()'''

#10
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(i,end="")
	print()'''

#11
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	ch=65 # "A"
	for j in range(1,i+1) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#12
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	ch=97 # 'a'
	for j in range(1,i+1) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#13
'''row=int(input("Enter total number of rows="))
digit=1
for i in range(1,row+1) :
	for j in range(1,i+1) :
			print(digit,end=" ")
			digit=1-digit
	print()'''

#14
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(num,end=" ")
		num+=1
	print()'''

#15
'''row=int(input("Enter total number of rows="))
ch=65
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(chr(ch),end="")
	ch+=1
	print()'''

#16
'''row=int(input("Enter total number of rows="))
ch=97
for i in range(1,row+1) :
	for j in range(1,i+1) : 
		print(chr(ch),end="")
		ch+=1
	print()'''

#17
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,i+1) :
		if i%2==0 :
			print("#",end="")
		else :
			print("*",end="")
	print()'''

#18
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	digit=1
	for j in range(1,i+1) :
		print(digit,end="")
		digit=1-digit
	print()'''

#19
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	for j in range(1,i+1):
		if j==i or j==1 or i==row :
			print("*",end="")
		else :
			print(" ",end="")
	print()'''
	
#20
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	num=1
	for j in range(num,i+1) :
		print(j,end="")
	print()'''

#21
'''row=int(input("Enter total number of rows="))
digit=1
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(digit,end="")
	digit+=1
	print()'''

#22
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	ch=65
	for j in range(1,i+1) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#23
'''row=int(input("Enter total number of rows="))
ch=97
for i in range(1,row+1) :
	for j in range(1,i+1) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#24
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	for j in range(1,i+1):
		if j==1 or i==row or j==i :
			print("*",end="")
		else :
			print("@",end="")
	print()'''

#25
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	num=row
	for j in range(1,i+1) :
		print(num,end="")
		num-=1
	print()'''

#26
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,i+1) :
		if j==2 or j==4 :
			print("#",end="") 
		else :
			print("*",end="")
	print()'''


#27
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	digit=1
	for j in range(1,i+1) :
		print(digit,end="")
		digit=1-digit
	print()'''

#28
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1) :
	for j in range(1,num+1) :
		print(j,end="")
	num=num+2
	print()'''

#29
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1) :
	for j in range(1,num+1) :
		print(i,end="")
	num=num+2
	print()'''

#30
'''row=int(input("Enter total number of rows="))
for i in range(0,row) :
	for j in range(0,row-i):
		print("*",end="")
	print()'''

#31
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	num=1
	for j in range(0,row-i):
		print(num,end="")
		num=num+1
	print()'''

#32
'''row=int(input("Enter total number of rows="))
num=row
for i in range(0,row+1) :
	for j in range(0,row-i):
		print(num,end="")
	num=num-1
	print()'''

#33
'''row=int(input("Enter total number of rows="))
for i in range(0,row+1) :
	ch=65
	for j in range(0,row-i):
		print(chr(ch),end="")
		ch+=1
	print()'''

#34
'''row=int(input("Enter total number of rows="))
ch=64+row
for i in range(0,row+1) :
	for j in range(0,row-i) :
		print(chr(ch),end="")
	ch=ch-1
	print()'''

#35
'''row=int(input("Enter total number of rows="))
for i in range(0,row+1):
	for j in range(1,row-i+1):
		if  j==1 or j==row-i or i==0 :
			print("*",end="")
		else :
			print(" ",end="")
	print()'''


#36
'''row=int(input("Enter total number of rows="))
for i in range(0,row+1):
	ch=65
	for j in range(0,row-i) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#37
'''row=int(input("Enter total number of rows="))
for i in range(0,row) :
	for j in range(0,row-i) :
		if i%2==0:
			print("#",end="")
		else :
			print("*",end="")
	print()'''

#38
'''row=int(input("Enter total number of rows="))
num=row
for i in range(0,row+1):
	for j in range(0,row-i):
		print(num,end="")
	num-=1
	print()'''

#39
'''row=int(input("Enter total number of rows="))
for i in range(0,row) :
	num=1
	for j in range(0,row-i) :
		print(num,end="")
		num+=1
	print()'''
#40
'''row=int(input("Enter total number of rows="))
count=0
for i in range(0,row+1) :
	for j in range(0,count+1) :
		print("*",end="")
		count+=1
	print()'''

#41
'''row=int(input("Enter total number of rows="))
ch=65
for i in range(0,row+1):
	if i==0:
		for j in range(0,i+1):
			print(chr(ch),end="")
			ch+=1
	else :
		for k in range(1,i*2+1+1):
			print(chr(ch),end="")
			ch+=1
	print()'''
	

#42
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(row,i-1,-1):
		print(j,end="")
	print()'''

#43
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1) :
	for j in range(1,row-i+1) :
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end="")
	print()'''
#44
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1) :
	for j in range(1,row-i+1) :
		print(" ",end="")
	for k in range(1,i+1):
		print(num,end="")
	num+=1
	print()'''
#45
'''row=int(input("Enter total number of rows="))
num=row
for i in range(1,row+1) :
	for j in range(1,row-i+1) :
		print(" ",end="")
	for k in range(1,i+1):
		print(num,end="")
	num-=1
	print()'''

#46
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	ch=65
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1) :
		print(chr(ch),end="")
		ch+=1
	print()'''

#47
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		if k==1 or k==i or i==row :
			print("1",end="")
		else :
			print("*",end="")
	print() '''

#48
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	ch=65
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		if k==1 or k==i or i==row :
			print(chr(ch),end="")
			ch+=1
		else :
			print("_",end="")
			ch+=1
	print()'''

#49
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	digit=1
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		print(digit,end="")
		digit=1-digit
	print()'''

#50
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	num=1
	for j in range(0,i+1):
		print(" ",end="")
	for k in range(1,row-i+1):
		print(k,end="")
	print()'''

#51
'''row=int(input("Enter total number of rows="))
num=row
for i in range(0,row+1):
	for j in range(0,i+1):
		print(" ",end="")
	for k in range(1,row-i+1):
		print(num,end="")
	num-=1
	print()'''

#52
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	num=1
	for j in range(0,i):
		print(" ",end="")
	for k in range(num,row-i+1):
		if i==0 or k==1 or k==row-i :
			print(num,end="")
			num+=1
		else:
			print("_",end="")
			num+=1
	print()'''	

#53
'''row=int(input("Enter total number of rows="))
num=row
for i in range(0,row):
	for j in range(0,i):
		print(" ",end="")
	for k in range(0,row-i):
		if i==0 or i==row-1 or k==0 or k==row-i-1 :
			print(num,end="")
		else :
			print(" ",end="")
	num-=1
	print()'''

#54
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	ch=65
	for j in range(0,i):
		print(" ",end="")
	for k in range(0,row-i):
		if i==0 or i==row-1 or k==0 or k==row-i-1 :
			print(chr(ch),end="")
			ch+=1
		else:
			print("_",end="")
			ch+=1
	print()'''
#55
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	ch=65
	for j in range(0,i+1):
		print(" ",end="")
	for k in range(1,row-i+1):
		print(chr(ch),end="")
		ch+=1
	print()'''
	
#56
'''row=int(input("Enter total number of rows="))
num=1
for i in range(0,row):
	for j in range(0,i+1):
		print(" ",end="")
	for k in range(1,row-i+1):
		print(num,end="")
	num+=1
	print()'''

#57
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		print("*",end="")
	print()'''

#58
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end="")
	print()'''

#59
'''row=int(input("Enter total number of rows="))
for i in range(1,row+1):
	ch=65
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,i+1):
		print(chr(ch),end="")
		ch+=1
	print()'''

#60
'''row=int(input("Enter total number of rows="))
for i in range(0,row):
	for j in range(0,row-i):
		print(" ",end=" ")
	for k in range(0,i+1):
		if i==0 or i==row-1 or k==0 or k==i :
			print("X",end=" ")
		else :
			print(" ",end=" ")
	print()'''
	
#61
'''row=int(input("Enter total number of rows="))
star=1
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(0,star):
		print("*",end="")
	star+=2
	print()'''

#62
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,num+1):
		print(k,end="")
	num+=2
	print()'''

#63
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1):
	ch=65
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,num+1):
		print(chr(ch),end="")
		ch+=1
	num+=2
	print()'''

#64
'''row=int(input("Enter total number of rows="))
star=1
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,star+1):
		if k==1 or i==row or k==star :
			print("*",end="")
		else :
			print("_",end="")	
	star+=2
	print()'''

#65
n =int(input("Enter total number of rows="))

for i in range(1, n + 1):

    print(1, end=" ")

    for j in range(2, i):
        print(i - 1, end=" ")

    if i > 1:
        print(1, end=" ")

    print()
#66
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,num+1):
		if k==1 or k==num or i==row:
			print("1",end="")
		else :
			print("*",end="")
	num+=2
	print()'''

#67
'''row=int(input("Enter total number of rows="))
num=1
ch=65
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,num+1):
		if k==1 or i==row or k==num :
			print(chr(ch),end="")
		else :
			print(" ",end="")
	ch+=1
	num+=2	
	print()'''

#68
'''row=int(input("Enter total number of rows="))
num=1
for i in range(1,row+1):
	for j in range(1,row-i+1):
		print(" ",end="")
	for k in range(1,num+1):
		if k%i==0:
			print("#",end="")
		else:
			print("*",end="")
	num+=2
	print()'''

#69
'''row=int(input("Enter total number of rows="))
rn=1
for i in range(1,row+1):
	for j in range(0,i):
		print(" ",end="")
	for k in range(1,row*2-rn+1):
		print("X",end="")
	rn+=2
	print()'''

#70
'''row=int(input("Enter total number of rows="))
for i in range(row,0,-1):
	for j in range(0,row-i):
		print(" ",end="")
	for k in range(1,i+1):
		print("*",end="")
	print()'''

#71
'''row=int(input("Enter total number of rows="))
num=1
space=1
odd=1
for i in range(row,0,-1):
	for j in range(0,space):
		print(" ",end="")
	space+=1
	for k in range(1,row*2-odd+1):
		print(k,end="")
	odd+=2
	print()'''

#72
'''row=int(input("Enter total number of rows="))
char=row
for i in range(0,row):
	ch=65
	for i in range(0,i):
		print(" ",end="")
	for k in range(0,char):
		print(chr(ch),end=" ")
		ch+=1
	char-=1
	print()'''

#73
'''row=int(input("Enter total number of rows="))
num=row
for i in range(0,row):
	for j in range(0,i):
		print(" ",end="")
	for k in range(1,num+1):
		print(num,end=" ")
	num-=1
	print()'''

#74
'''row=int(input("Enter total number of rows="))
num=1
for i in range(0,row):
	for j in range(0,i):
		print(" ",end="")
	for k in range(1,row*2-num+1):
		if k==1 or i==0 or k==row*2-num :
			print(k,end="")
		else :
			print(" ",end="")
	num+=2
	print()'''

#75
'''row=int(input("Enter total number of rows="))
num=1
for i in range(0,row):
	for j in range(0,i):
		print(" ",end="")
	for k in range(1,row*2-num+1):
		if k==1 or i==0 or k==row*2-num :
			print(k,end="")
		else :
			print("+",end="")
	num+=2
	print()'''

#76
'''row=int(input("Enter total number of rows="))
for i in range(1,row):
	for j in range(1,i+1):
		print("X",end="")
	print()
for i in range(row-2,0,-1):
	for j in range(1,i+1):
		print("X",end="")
	print()'''
	

#77
'''row=int(input("Enter total number of rows="))
for i in range(1,row):
	for j in range(1,i+1):
		print(j,end="")
	print()
for i in range(row-2,0,-1):
	for j in range(1,i+1):
		print(j,end="")
	print()'''

#78
'''row=int(input("Enter total number of rows="))
space=1
for i in range(1,row):
	for j in range(1,row-i):
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end="")
	print()
for i in range(row-2,0,-1):
	for j in range(1,space+1):
		print(" ",end="")
	space+=1
	for k in range(1,i+1):
		print(k,end="")
	print()'''

#79
'''row=int(input("Enter total number of rows="))
for i in range(1,row):
	for j in range(1,i+1):
		if j==1 or j==i :
			print(j,end="")
		else:
			print(" ",end="")
	print()
for i in range(row-2,0,-1):
	for j in range(1,i+1):
		if j==1 or j==i :
			print(j,end="")
		else :
			print(" ",end="")
	print()'''

#80
'''row=int(input("Enter total number of rows="))
for i in range(1,row):
	for j in range(1,row-i):
		print(" ",end="")
	for k in range(1,i+1):
		print("*",end=" ")
	print()
space=1
for i in range(row-2,0,-1):
	for j in range(1,space+1):
		print(" ",end="")
	space+=1
	for k in range(i,0,-1):
		print("*",end=" ")
	print()'''

#81
'''n =int(input("Enter total number of rows="))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")
    print()'''

#82
'''n =int(input("Enter total number of rows="))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 1:
        for j in range(2 * i - 3):
            print("_", end=" ")

        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 1:
        for j in range(2 * i - 3):
            print("_", end=" ")

        print("*", end=" ")
    print()'''

#83
'''n =int(input("Enter total number of rows="))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

#84
'''n =int(input("Enter total number of rows="))

for i in range(1, n + 1):

    for j in range(i, 0, -1):
        print(j, end="")

    for j in range(2, i + 1):
        print(j, end="")

    print()'''

#85
'''n =int(input("Enter total number of rows="))

for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()'''

#86
'''n =int(input("Enter total number of rows="))

for i in range(n, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")'''

#87
'''n =int(input("Enter total number of rows="))

for i in range(n, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

for i in range(2, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(2 * (n - i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

    print()'''

#88
'''n =int(input("Enter total number of rows="))

for i in range(1, n + 1):
    print(i)

print("123454321")

for i in range(n, 0, -1):
    print(i)'''

#89
'''n =int(input("Enter total number of rows="))

for i in range(1, n + 1):

    for j in range(1, 2 * i):
        if j % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")

    print()'''

#90
'''n =int(input("Enter total number of rows="))

for i in range(n):

    for j in range(n):

        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()'''
		


	


		

	

	

