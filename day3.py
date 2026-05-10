#1Speed Calculator
'''distance=float(input("Enter Distance(in km) = "))
time=float(input("Enter time(in hours) = "))
print(f"Speed = {distance/time} km/h ", )'''

#2 Salary Calculator
'''daily_wage=int(input("Enter Daily Wage = "))
days=int(input("Enter total days= "))
print(f"Salary =  {daily_wage * days}")'''

#3 Electricity Bill Calculator
# 6 Rs. per unit
'''units=int(input("Enter total units = "))
print(f"Bill = {units*6}")'''

#4 Area of Rectangle
'''L,B=map(int,input("Enter length & Breadth of a Rectangle = ").split(","))
print(f"Area of Reactangle = {L*B}")'''

#5 Average Marks Calculator
'''maths,eng,hindi=map(int,input("Enter marks of 3 subject(Maths, Eng, Hindi) = ").split(","))
avg=(maths+eng+hindi)/3
print("Average Marks = ",avg)'''

#6 Discount Calculator
'''amount=int(input("Total Amount = "))
discount=amount*10/100
Final_Amount=amount-discount

print(f"Amount= {amount} \nDiscount={discount} \nFinal Amount={Final_Amount}")'''

#7 Area of circle
'''rad=int(input("Enter radius="))
area=3.14*rad*rad

print(f"Area Of Circle= {area}")'''

#8 Data Storage Converter
'''mb=int(input("MB="))
gb=mb/1024
print(f"GB={gb}")'''

#9 Fuel Cost Calculator
'''dis=int(input("Enter total distance="))
mileage,petrol_price=20,100
One_Km_cost=petrol_price/mileage
print(f"mile_Age={mileage} \npetrol_Price={petrol_price}")
print(f"Total Cost={One_Km_cost*petrol_price}")'''

#10 Percentage Calculator
'''tot,obt=map(int,input("Total Marks & Obtained Marks=").split(","))
print(f"Percentage={(obt/tot)*100}")'''

#11 Time Duration Adder
'''hr,mn,sec=map(int,input("Enter Hours,Minutes & Seconds=").split(","))
hr=hr*3600
mn=mn*60
print(f"Total Seconds={hr+mn+sec}")'''

#12 Change Return system
'''amount=int(input("Enter Amount="))
ths=amount//100
rem=amount%100
fif=rem//50
rem=rem%50
tn=rem//10
print(f"100 Rs={ths}\n50 Rs={fif}\n10 Rs={tn}")

#13 Compound Interest Calculator
p=int(input("Enter Principal="))
r=int(input("Enter Rate="))
t=int(input("Enter Time="))
amount=p*(1+r/100)**t
ci=amount-p
print("Amount=",amount)
print(f"CI= {ci}")



#14 Profit and loss
cp,sp=map(int,input("Enter cost price & selling price=").split(","))
profit = sp-cp
pp = (profit/cp)*100
print("Profit=",profit)
print("Profit Percentage=",pp)

#15 Average Speed for muliple trips
'd1,t1=map(int,input("Enter Distance1=\nTime1=\n").split(","))
d2,t2=map(int,input("Enter Distance2=\nTime2=\n").split(","))
sp1=d1/t1
sp2=d2/t1
avg=(sp1+sp2)/2
print(f"Average Speed = {avg} km/h")'''

n1 = int(input("Enter first number="))
n2 = int(input("Enter second number="))
sum = 0
for i in range(n1, n2 + 1):
    for j in range(1, i // 2):
        if i % j == 0:
            sum = sum + j

    if sum == i:
        print(i)

