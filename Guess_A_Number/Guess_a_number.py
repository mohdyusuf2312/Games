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
    remain = 10
    # global easy
    while remain != 0:
        print(f"You have {int(remain)} attempts remaining to guess the number.")
        guess = input("Make a guess : ")
        if guess.isdigit() == False:
            print("Input should be an integer")
        else:
            if int(guess) == number:
                print(f"You got it! The answer was {number}")
                break
            elif int(guess) < number:
                print("Too low! guess again.")
                remain -= 1
                continue
            elif int(guess) > number:
                print("Too high! guess again.")
                remain -= 1
                continue
    if remain == 0:
        print(f"The number was {number}")

# hard = 5
def hard():
    remain = 5
    while remain != 0:
        print(f"You have {remain} attempts remaining to guess the number.")
        guess = input("Make a guess : ")
        if guess.isdigit() == False:
            print("Input should be an integer")
        else:
            if int(guess) == number:
                print(f"You got it! The answer was {number}")
                break
            elif int(guess) < number:
                print("Too low! guess again.")
                remain -= 1
                continue
            elif int(guess) > number:
                print("Too high! guess again.")
                remain -= 1
                continue
    if remain == 0:
        print(f"The number was {number}")

start()