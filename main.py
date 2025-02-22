from random import *

#creating variables with characters
digits = "1234567890"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "$%&*+-=?@^_.!#"

chars = []

#generation requirements
amount_of_passwords = int(input("Number of passwords to generate:"))
length = int(input("Password length:"))
if amount_of_passwords <= 0 or length <= 0:
    print("Error. Enter positive number")

#password requirements
allow_digits = input("Include digits? Yes/No ").lower()
allow_lowercase = input("Include lowercase letters? Yes/No ").lower()
allow_uppercase = input("Include uppercase letters? Yes/No ").lower()
allow_symbols = input("Include special symbols $%&*+-=?@^_.!#? Yes/No ").lower()
exclude = input("Exclude ambiguous characters il1Lo0O? Yes/No ").lower()

#removing ambiguous characters function
def exclude_true():
    lowercase_remove = "ilo"
    for _ in lowercase_letters:
        lowercase_letters = lowercase_letters.replace(lowercase_remove, "")
    uppercase_remove = "LO"
    for _ in uppercase_letters:
        uppercase_letters = uppercase_letters.replace(uppercase_remove, "")
    digits_remove = "01"
    for _ in digits:
        digits = digits.replace(1, 0, "")

if exclude == "yes":
    exclude_true()

#adding characters to the list
if allow_digits == "yes":
    chars.extend(digits)
if allow_lowercase == "yes":
    chars.extend(lowercase_letters)
if allow_uppercase == "yes":
    chars.extend(uppercase_letters)
if allow_symbols == "yes":
    chars.extend(punctuation)

#password generation function
def generate_password(length, chars):
    if amount_of_passwords >= 2: #for several passwords
        password_list = []
        for _ in range(amount_of_passwords):
            password_list.append("".join(sample(chars, length)))
    elif amount_of_passwords == 1: #for a single password
        password = "".join(sample(chars, length))

    return password_list if amount_of_passwords >= 2 else password

print(*generate_password(length, chars), sep="\n")
