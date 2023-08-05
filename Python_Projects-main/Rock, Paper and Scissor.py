
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

#input from user 
user_input = input("Type either 'rock', 'paper' or scissors :\n").lower()

print("User Choose:")
print(user_input)
#putting it in a list for the computer 
result = [rock,paper, scissors]

#Generate random result for the Computer
import random 
computer = result[random.randint(1,3)-1] 
print(computer) 

#Who WON, Who Lose?
if user_input == "rock":
    if computer == rock:
        print("It's a draw. Nobody Wins, repeat!")
    elif computer == paper:
        print("Paper cover up the whole rock and therefore is greater.\n You Lose")
    elif computer == scissors:
         print("One hit with the rock, destroys the scissors.\nYou win!")
elif user_input == "paper":
  if computer == rock:
    print("Paper is greater than the rock and eats the rock. You win!")
  elif computer == paper:
    print("It's a draw! Try again!")
  elif computer == scissors:
    print("Ohnoo, scissors cut the paper. You lose!")

elif user_input == "scissors":
  if computer == rock:
    print("Ohnoo! One hit by the rock breaks the scissors in two pieces. You lose!")
  elif computer == paper:
    print("Scissors cut the paper. You win!")
  elif computer == scissors: 
    print("It's a draw. Try again!")
    
else:
  print("I don't understand your input...\nDo you chose either rock, paper or scissors?\n")