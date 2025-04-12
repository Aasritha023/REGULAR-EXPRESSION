import re

# Name
while True:
    pattern = re.compile(r'^[A-Za-z]+$')
    text = input("Enter your name: ")
    res = pattern.fullmatch(text)
    if res:
        name = res.group()
        break
    else:
        print("Enter name in correct format (letters only)!")

print("Name:", name)

# Date of Birth
while True:
    pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')  
    text = input("Enter date of birth (DD-MM-YYYY): ")
    res = pattern.fullmatch(text)
    if res:
        dob = res.group()
        break
    else:
        print("Enter DOB in correct format (DD-MM-YYYY)!")

print("Date of Birth:", dob)

# Email
while True:
    pattern = re.compile(r'^[a-z0-9]+@gmail\.com$')  
    text = input("Enter email ID: ")
    res = pattern.fullmatch(text)
    if res:
        mailid = res.group()
        break
    else:
        print("Enter email ID in correct format (e.g., username@gmail.com)!")

print("Email ID:", mailid)

# Mobile Number
while True:
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')  
    text = input("Enter mobile number (XXX-XXX-XXXX): ")
    res = pattern.fullmatch(text)
    if res:
        mobileno = text.replace("-", "") 
        break
    else:
        print("Enter mobile number in correct format (XXX-XXX-XXXX)!")

print("Mobile Number:", mobileno)
