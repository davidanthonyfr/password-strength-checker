# Password Strength Checker

# Step 1: Ask user for a password
password = input("Enter your password: ")

# Step 2: Start a score at 0
score = 0

# Step 3: Check for lowercase letters
for char in password:
    if char.islower():
        score = score + 1
        break   # stop checking once we find one

# Step 4: Check for uppercase letters
for char in password:
    if char.isupper():
        score = score + 1
        break

# Step 5: Check for digits
for char in password:
    if char.isdigit():
        score = score + 1
        break

# Step 6: Check for symbols
symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
for char in password:
    if char in symbols:
        score = score + 1
        break

# Step 7: Check password length
length = len(password)

# Step 8: Print the results
print("\nPassword length:", length)
print("Variety score:", score, "out of 4")

if length < 8:
    print("Overall: WEAK (too short!)")
elif length >= 8 and length <= 12:
    if score >= 3:
        print("Overall: MEDIUM")
    else:
        print("Overall: WEAK")
else:  # length >= 13
    if score == 4:
        print("Overall: STRONG")
    else:
        print("Overall: MEDIUM")
