import random

max_num = input('Please enter a number: ')
max_num = int(max_num)
min_num = 0
num_list = []

for num in range(max_num + 1):
	num_list.append(num)
print(f'\n{num_list}')

rand_num = random.choice(num_list)

game = True
while game == True:
	user_choice = input("\nPlease choose a number from the above list to see if you can find our number: ")
	user_choice = int(user_choice)

	if rand_num == user_choice:
		print('Well done! You guessed correctly!!!')
		game = False

	elif rand_num > user_choice:
		print('\nYour number was too low. Please guess again.')
		num_list = [e for e in num_list if e > user_choice]
		print(f'\n{num_list}')

	elif rand_num < user_choice:
		print('\nYour number was too high. Please guess again.')
		num_list = [e for e in num_list if e < user_choice]
		print(f'\n{num_list}')

		#item_list = [e for e in item_list if e not in ('item', 5)]
