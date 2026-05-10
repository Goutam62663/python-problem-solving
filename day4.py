'''Note:
* Do NOT use if-else
* All percentages are given as whole numbers (like 5, 10). Convert using (value ÷ 100)
* Follow correct operator precedence and associativity
* Use ** for power (exponent), not ^

Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

nput:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''

'''TA=int(input("Total Amount="))
GST=int(input("Enter GST="))
SC=int(input("Enter Service Charge="))
FRD=int(input("Enter Total Friends="))
GST=TA*(GST/100)
SC=TA*(SC/100)
FB=TA+GST+SC
print(f"Final Bill={FB}")
print(f"Each Person Pays={FB/FRD}")'''

'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''

'''MP=int(input("Enter Mobile Price="))
DP=int(input("Enter Down Payment="))
IR=int(input("Enter Interest Rate="))
MTH=int(input("Enter Months="))
RA=MP-DP
Intrs=RA*(IR/100)
TWI=RA+Intrs
print(f"Remaining Amount={RA}")
print(f"Total With Interest={TWI}")
print(f"Monthly EMI={TWI/MTH}")'''

'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2'''

'''TS=int(input("Enter number of subject="))
M,S,P,C,E=map(int,input("Enter all subject marks=").split(","))
TM=M+S+P+C+E
AVG=TM/TS
PRC=(TM/500)*100
print(f"Total Marks={TM}")
print(f"Average={AVG}")
print(f"Percentage={PRC}")'''

'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''

'''SD=int(input("Enter Speed="))
H,M=map(int,input("Enter Time(Hours,Minutes)=").split(","))
M=M/60
TT=H+M
DT=SD*TT
print(f"Total Time={TT} hours")
print(f"Distance={DT} Km")'''

'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''

'''MS=int(input("Enter Monthly Salary="))
WD=int(input("Enter Working Days="))
WH=int(input("Enter Working hours per day="))
SPD=(MS / WD)
SPH=(SPD / WH)
print(f"Salary per day={SPD}")
print(f"Salary per hour={SPH}")'''

#6 Data Storage Conversion
'''GB=int(input("Enter Data in GB="))
MB=GB*1024
KB=MB*1024
print("MB=",MB)
print("KB=",KB)'''

'''Assignment 7: Cricket Run Rate
In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

'''# Input
runs = 275
overs = 48.3

# Convert overs into balls
full_overs = int(overs)          # 48
balls = int((overs - full_overs) * 10)   # 3

total_balls = full_overs * 6 + balls

# Convert overs to proper decimal
actual_overs = full_overs + balls / 6

# Calculate run rate
run_rate = runs / actual_overs

# Output
print("Total Balls =", total_balls)
print("Run Rate =",run_rate)'''

'''Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0'''

Principal=int(input("Enter Principal="))
Rate=int(input("Enter Rate="))
Time=int(input("Enter Time="))
Amount=Principal*(1+Rate/100)**Time
print("Amount after interest=",Amount)





