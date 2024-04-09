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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissor]
Computer_choice = random.randint(0,2)
User_choice = int(input("What do you want to choose? Enter 0 for 'Rock', 1 for 'Paper', 2 for 'Scissor' : "))

# print("Result : ")

if User_choice < 0 or User_choice > 2:
    print("Invalid Input")
else:
    if Computer_choice == User_choice : 
        print("It's a draw!")
    elif Computer_choice == 0 and User_choice == 1:
        print("You lose")
    elif Computer_choice == 0 and User_choice == 2:
        print("You lose")
    elif Computer_choice == 1 and User_choice == 0:
        print("You Win")
    elif Computer_choice == 1 and User_choice == 2:
        print("You Win")
    elif Computer_choice == 2 and User_choice == 0:
        print("You Win")
    elif Computer_choice == 2 and User_choice == 1:
        print("You lose")
    print(f"You : {list[User_choice]}\nComputer : {list[Computer_choice]}")
# print("\n")
