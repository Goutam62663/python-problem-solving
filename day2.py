# Accept total duration in seconds
total_seconds = int(input("Enter total duration in seconds: "))

# Calculate hours, minutes, and seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Display the result
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

# Accept age in years
'''age = int(input("Enter your age in years: "))

# Calculate days, hours, and minutes
days = age * 365
hours = days * 24
minutes = hours * 60

# Display the result
print("You've lived approximately:")
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)

# Accept total bill amount
total_bill = float(input("Enter total bill amount: "))

# Accept number of friends
friends = int(input("Enter number of friends: "))

# Calculate amount per person
each_pay = total_bill / friends

# Display result
print("Each should pay =", each_pay)

# Rate per kilometer
rate = 15

# Accept distance traveled
distance = float(input("Enter distance in km: "))

# Calculate total fare
total_fare = distance * rate

# Display result
print("Total fare = ₹", total_fare)


# Accept cart total amount
cart_total = float(input("Enter cart total amount: ₹"))

# Calculate 12% GST
tax = cart_total * 0.12

# Calculate final total
final_total = cart_total + tax

# Display result
print("Tax = ₹", tax)
print("Total = ₹", final_total)


# Accept total amount
amount = int(input("Enter amount: ₹"))

# Calculate number of ₹10 coins
ten_coins = amount // 10

# Remaining amount after ₹10 coins
remaining = amount % 10

# Calculate number of ₹5 coins
five_coins = remaining // 5

# Display result
print("₹10 x", ten_coins, ", ₹5 x", five_coins)


# Accept temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result


# Accept inputs
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

# Calculate Simple Interest
si = (principal * rate * time) / 100

# Display result
print("Simple Interest =", si)

print("Fahrenheit =", fahrenheit)'''







