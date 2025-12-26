from random import randint
from art import logo

easy_level = 10
hard_level = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level
    elif level == "hard":
        return hard_level
    else:
        print("You typed something wrong. Try again.")
        return difficulty()

def game():
    
    print(logo)

    answer = randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = difficulty()

    guess = None
    while guess != answer and turns > 0:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose!")
            print(f"The correct answer was {answer}.")

game()
