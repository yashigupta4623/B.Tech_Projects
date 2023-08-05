import random 

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X','Y','Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PassWord Generator!")

no_letter = int(input("How many Letters would you like in your Password?\n"))
no_symbols = int(input("How many Symbols would you like in your Password?\n"))
no_numbers = int(input("How many Numbers would you like in your Password?\n"))

#Easy
password = "" 

for char in range(1,no_letter+1):
    random_letter = random.choice(letters)
    password += random_letter

for sym in range(1,no_symbols+1):
    random_symbols = random.choice(symbols)
    password += random_symbols

for char in range(1,no_numbers+1):
    random_numbers = random.choice(numbers)
    password += random_numbers

print(password, end = "")

#HARD

password_list = []

for char in range(1,no_letter+1):
    random_letter = random.choice(letters)
    password_list += random_letter

for sym in range(1,no_symbols+1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

for char in range(1,no_numbers+1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

random.shuffle(password_list)
result = ""
for i in password_list:
    result+=i 

print(f"Your Password is : {result}")
