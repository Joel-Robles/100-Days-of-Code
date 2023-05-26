#A fun little rock/scissors/paper program. 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  print(game_images[0])
elif choice == 1:
  print(game_images[1])
elif choice == 2:
  print(game_images[2])
else:
  print("Wrong! Wrong! Under section 37B of the contract signed by you, it states quite clearly that all offers shall become null and void if - and you can read it for yourself in this photostatic copy - 'I, the undersigned, shall forfeit all rights, privileges, and licenses herein and herein contained,' et cetera, et cetera...'Fax mentis incendium gloria cultum,' et cetera, et cetera...'Memo bis punitor delicatum!' It's all there, black and white, clear as crystal! You didn't chose a number between 0 and 2. You bumped into the ceiling of this program which now has to be washed and sterilized, so you get nothing! You lose! Good day!")
  quit()

computer_choice = random.randint(0,2)
print(f"Computer chose :{computer_choice}")

if computer_choice == 0:
  print(game_images[0])
elif computer_choice == 1:
  print(game_images[1])
else:
  print(game_images[2])

if choice == 0 and computer_choice == 0:
  print("Draw")
elif choice == 0 and computer_choice == 1:
  print("You lose")
elif choice == 0 and computer_choice == 2:
  print("You win")
elif choice == 1 and computer_choice == 0:
  print("You win")
elif choice == 1 and computer_choice == 1:
  print("Draw")
elif choice == 1 and computer_choice == 2:
  print("You lose")
elif choice == 2 and computer_choice == 0:
  print("You lose")
elif choice == 2 and computer_choice == 1:
  print("You win")
else:
  print("Draw")
