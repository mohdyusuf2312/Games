# It is a remaing part of day_12

import random

number = random.randint(1,100)

logo = '''
                                                                                                                        
    //   ) )                                          // | |       /|    / /                                              
   //                  ___      ___      ___         //__| |      //|   / /           _   __     / __      ___      __    
  //  ____  //   / / //___) ) ((   ) ) ((   ) )     / ___  |     // |  / / //   / / // ) )  ) ) //   ) ) //___) ) //  ) ) 
 //    / / //   / / //         \ \      \ \        //    | |    //  | / / //   / / // / /  / / //   / / //       //       
((____/ / ((___( ( ((____   //   ) ) //   ) )     //     | |   //   |/ / ((___( ( // / /  / / ((___/ / ((____   //        
'''
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")

def start():
    level = input("Choose a dificulty. Type 'easy' or 'hard' : ").lower()

    if level == "easy":
        easy()
    elif level == "hard":
        hard()
    else:
        print("Invalid Input!")
        start()

# easy = 10
def easy():
    remian = 10
    # global easy
    for i in range(10):
        print(f"You have {int(remian)} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            break
        elif guess < number:
            print("Too low! guess again.")
            remian -= 1
            continue
        elif guess > number:
            print("Too high! guess again.")
            remian -= 1
            continue

# hard = 5
def hard():
    remian = 5
    for i in range(5):
        print(f"You have {remian} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            break
        elif guess < number:
            print("Too low! guess again.")
            remian -= 1
            continue
        elif guess > number:
            print("Too high! guess again.")
            remian -= 1
            continue

start()