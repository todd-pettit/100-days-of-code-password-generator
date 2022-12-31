#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#I'll skip easy level

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ''
selected_characters = []


for n in range(1, (nr_letters + 1)):
    selected_characters.append(letters[random.randint(0, len(letters) - 1)])

for n in range(1, (nr_symbols + 1)):
    selected_characters.append(letters[random.randint(0, len(symbols) - 1)])

for n in range(1, (nr_numbers + 1)):
    selected_characters.append(numbers[random.randint(0,len(numbers) - 1)])

random.shuffle(selected_characters)

for char in selected_characters:
    password += char

print(f"Your password is: {password}")
