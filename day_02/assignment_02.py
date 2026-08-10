# Arithmetic operators

a = 2
b = 5
print(a**b) # Exponentiation
print(a%b) # Modulus (remainder)
print(a/b) # Division
print(a//b) # Floor division (integer division)
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication

#strings
str1 = "Ryan Gosling"
str2 = " is literally me"
print(str1+str2) # String concatenation
print(str1 * 2) # String repetition
str2 = "literally literally me"
print(str2) # Print the updated string
print("The Odyssey has grossed over "+str(1.2)+"B dollars globally") # Convert number to string for concatenation


# Round function - rounds to the nearest integer
print(round(1.89)) # Example of round function
# Absolute value - returns the positive value of a number
print(abs(-10)) # Example of absolute value


# Relational operators - compare two values

num1 = 5
num2 = 2
print(num1 == num2) # Equal to operator
print(num1 != num2) # Not equal to operator
print(num1 > num2) # Greater than operator
print(num1 < num2) # Less than operator
print(num1 >= num2) # Greater than or equal to operator
print(num1 <= num2) # Less than or equal to operator
# Conditional statements using relational operators

num1 = int(input("Enter number 1: ")) # Get first integer input from user
num2 = int(input("Enter number 2: ")) # Get second integer input from user

if(num1 == num2):
    print(num1," is equal to number 2")
elif(num1 < num2):
    print("Number 1 is less than number 2")
elif(num1 != num2):
    print("Number 1 is not equal to number 2")
elif(num1 >= num2):
    print("Number 1 is greater than or equal to number 2")
elif(num1 <= num2):
    print("Number 1 is less than or equal to number 2")


# Logical operators

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     #Flip


# Python game with all the concepts learned so far 

print("You are locked inside a vault")
print("Your mission is to get enough power to escape this vault")

# Level 1: Energy Core - Addition operator
energy=10
print("LEVEL 1 — ENERGY CORE")
print(f"You start with {energy} energy.")

found = int(input("You found an energy crystal worth: "))

energy = energy + found # Add found energy to current energy

print("Energy collected!")
print(f"Your energy is now: {energy}")

# Level 2: Power Boost - Multiplication operator
print("LEVEL 2 — POWER BOOST")

boost = int(input("Choose your power multiplier (1–5): "))

powered_energy = energy * boost # Multiply energy by boost factor

print("POWER ACTIVATED!")
print(f"Your energy became: {powered_energy}")

# Level 3: Laser Wall - Subtraction operator
print("LEVEL 3 — LASER WALL")

laser_cost = int(input("How much energy does the laser wall cost? "))

remaining = powered_energy - laser_cost # Subtract laser cost from powered energy

print("Laser wall disabled!")
print(f"Energy remaining: {remaining}")

# Level 4: Team Up - Division operator
print("LEVEL 4 — TEAM UP")

team_size = int(input("How many hackers are in your team? "))

share = remaining / team_size # Divide remaining energy among team members

print(f"Each hacker gets {share:.2f} energy.")

# Level 5: Build the Squad - Floor division operator
print("LEVEL 5 — BUILD THE SQUAD")

energy_per_hacker = int(input("Energy required per hacker: "))

full_hackers = remaining // energy_per_hacker # Calculate how many hackers can be fully powered

print(f"You can fully power {full_hackers} hackers.")

# Level 6: Leftover Energy - Modulus operator
leftover = remaining % energy_per_hacker # Calculate remaining energy after powering hackers

print(f"Energy left unused: {leftover}")

# Level 7: The Final Vault - Exponentiation operator
print("LEVEL 7 — THE FINAL VAULT")

power_level = int(input("Enter your final power level: "))

final_power = power_level ** 2 # Calculate final power by squaring the input

print(f"Your final power is: {final_power}")

# Mission Escape
print("VAULT UNLOCKED!")

# Display mission complete summary
print(f"""
🏆 MISSION COMPLETE!

🔋 Final energy      : {remaining}
👥 Full hackers      : {full_hackers}
♻️ Leftover energy   : {leftover}
⚡ Final power       : {final_power}

You didn't just learn operators.
You used them to build something. 🐍

WELCOME TO PYTHON.
""")