# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Getting the length of the list
names_length = len(names)
#Chosing a random person (not using choice)
test = random.randint(0,names_length-1)
#Printing out the "lucky" person
print(f"{names[test]} is going to buy the meal today!")
