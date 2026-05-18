'''1.Vowel Counter in Customer Feedback
 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.
Input: Enter feedback message: Hello Customer Service
Output: Total vowels: 8'''

'''feedback=input("Enter feedback message:").lower()
i=0
count=0
while i < len(feedback) :
	if feedback[i]=='a' or feedback[i]=='e' or feedback[i]=='i' or feedback[i]=='o' or feedback[i]=='u' :
		count+=1
	i+=1
print("Total vowels:", count)'''
	
'''2.
Space Counter in Chat Messages
A chat application wants to calculate how many spaces are used in a message.
Input: Enter chat message: Good morning everyone how are you
Output: Total spaces: 5'''

'''msg=input("Enter chat message:")
i=0
count=0
while i < len(msg) :
	if msg[i].isspace() == True :
		count+=1
	i+=1
print("Total spaces:",count)'''



'''3.
Character Occurrence Checker in Product Review
An e-commerce website wants to know how many times a particular character appears in a product review.
Input: Enter product review: this product is really good Enter character to check: o
Output: Character 'o' occurs: 3 times'''

'''msg=input("Enter product review:")
char=input("Enter character to check:")
print(msg.count(char))'''
	

'''4.
Consonant Counter in Student Name Record
A school management system wants to count how many consonants are present in student names.
Input: Enter student name: Ajay Singh Thakur
Output: Total consonants: 10

NOTE:
Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U'''

'''name=input("Enter student name:").lower()
count=0
for ch in name :
	if ch.isalpha() and ch not in "aeiou" :
		count+=1
print("Total consonants:",count)'''

'''5.
Advanced Password Security Checker
A cyber security company wants to verify whether employee passwords are highly secure before giving system access.
Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45
Output: Secure Password'''

'''passw = input("Enter password: ")

digit = 0
space = 0
special = 0
i = 0

while i < len(passw):

    ch = passw[i]

    if ch.isdigit():
        digit += 1

    elif ch.isspace():
        space += 1

    elif ch in "@#$%&*":
        special += 1

    i += 1

if 8 <= len(passw) <= 15 and passw[-1].isdigit() and digit >= 2 and space == 0 and special >= 1 and passw[0].isupper():

    print("Secure Password")

else:

    print("In-Secure Password")'''


'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''

'''pnr = input("Enter PNR: ")

if pnr.startswith("PNR") and len(pnr) == 12 and pnr[3:].isdigit():

    print("Valid PNR Number")

else:

    print("Invalid PNR Number")'''


'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''
vehicle = input("Enter vehicle number: ")

if vehicle[0:2].isalpha() and vehicle[2:4].isdigit() and len(vehicle) == 10:

    print("Valid Vehicle Number")

else:

    print("Invalid Vehicle Number")