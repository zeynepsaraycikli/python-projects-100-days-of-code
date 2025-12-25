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
my_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)

computers_choice = random.randint(0,2)
print(f"Computer choice {computers_choice}")
if computers_choice == 0:
    print(rock)
elif computers_choice == 1:
    print(paper)
elif computers_choice == 2:
    print(scissors)
if my_choice == 0 and computers_choice == 2:
    print("You win!!")
elif computers_choice < my_choice :
    print("You win!!")
elif computers_choice == my_choice:
    print("Draw!!!")
else:
    print("You lose..")
