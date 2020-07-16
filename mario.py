get_number = input('Let us make a pyramid. Please enter a number: ')
get_number = int(get_number)

white_space = get_number
new = 1
while new <= get_number:
	print(' ' * white_space + '#' * new + ' ' + '#' * new + ' ' * white_space)
	new += 1
	white_space -= 1


