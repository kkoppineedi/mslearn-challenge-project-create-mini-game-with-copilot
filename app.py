import random

# write 'hello world' to the console
print('Welcome to Rock, Paper, Scissors!')

# 3 simple rules - rock beats scissors, scissors beats paper, paper beats rock

# prompt the user to select between rock, paper, or scissors
# convert the user's input to lowercase
# store the user's input in a variable
user_choice = input('Please choose rock, paper, or scissors: ').lower()

# validate if value of user_choice is 'rock', 'paper', or 'scissors'
# if the value is not valid, print an error message to the console
# and exit the program
if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
    print('Invalid choice. Please try again.')
    exit()

# randomly select between rock, paper, or scissors and store in a variable
# print the computer's choice to the console
# compare the user's choice to the computer's choice
# print the results to the console
# if the user wins, print 'You win!'
# if the computer wins, print 'You lose!'
# if it's a tie, print 'It's a tie!'
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print('Your choice: ' + user_choice, 'Computer: ' + computer_choice)

if user_choice == computer_choice:
    print('It\'s a tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('You lose!')

