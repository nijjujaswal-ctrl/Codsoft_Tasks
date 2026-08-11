import random
import string

# Ask the user for password length
length = int(input("Enter the desired password length: "))

# Ask for complexity
print("\nChoose password complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter your choice (1/2/3): ")

# Select characters based on choice
if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice!")
    exit()

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display password
print("\nGenerated Password:", password)
