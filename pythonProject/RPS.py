import random
print('You will play rock paper scissors with computer. If you chose the same object as computer no one gets a point.'
	  'If you win you get a point otherwise computer gets a point. Winner is the one who first gets 3 points.')
list_of_choices = ['Rock', 'Paper', 'Scissors']

user_points = 0
computer_points = 0
while user_points < 3 and computer_points < 3:
	print(f'computer points:{computer_points}, user points:{user_points}')
	user_input = input('What is your choice? ').capitalize().strip()

	if user_input not in list_of_choices:
		print('Invalid input, please choose Rock, Paper, or Scissors.')
		continue

	computer_choice = random.choice(list_of_choices)

	if computer_choice == user_input:
		print(f'computer chose is : {computer_choice}')
		print('no one gets a point!')
	elif user_input == 'Rock':
		print(computer_choice)
		if computer_choice == 'Paper':
			print('Computer gets a point!')
			computer_points += 1
		elif computer_choice == 'Scissors':
			print('You got a point!')
			user_points += 1
	elif user_input == 'Scissors':
		print(computer_choice)
		if computer_choice == 'Rock':
			print('Computer gets a point!')
			computer_points += 1
		elif computer_choice == 'Paper':
			print('You got a point!')
			user_points += 1
if user_points == 3:
	print('Good job. You won!')
elif computer_points == 3:
	print('To bad, computer won. Better luck next time!')










