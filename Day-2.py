#Tip Calculator based on fixed input.
#Printing welcome to user.
print("Welcome to the tip calculator.")
#Asking the user for the total bill and converting to float. 
total_bill = float(input("What was the total bill? $"))
#Asking the user for their percent tip as whole number, converting to a float and then a percentage.
percent_tip = (float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100) +1
#Asking the user for how many people the bill needs to split by each person
person_split = int(input("How many people to split the bill? "))
#Calculating the split per person based on the user input and rounding to two digits. 
print("Each person should pay: $" + f"{((total_bill/person_split)*percent_tip):.2f}")
