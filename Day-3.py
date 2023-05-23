#Just a fun little calculator that takes your name and determines some compatbility 
print("Welcome to the Love Calculator!")
#Asks the user names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#Combines the user names and converts to lower
combined_name = name1.lower() + name2.lower()
#Finding out both the times TRUE and LOVE occurs.
true_count = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
love_count = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')
#Translates both numbers into a string, then converts to an integer.
love_score = int(str(true_count) + str(love_count))

#Determins your compatibility (if any)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
