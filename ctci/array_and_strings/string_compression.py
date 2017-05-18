def string_compress(input_string):
	if len(input_string) < 3:
		return input_string

	processed_string = ""

	absolute_counter = 0
	counter = 0
	char_of_interest = input_string[0]

	for char in input_string:
		absolute_counter += 1
		if char ==char_of_interest:
			counter += 1
		else:
			processed_string += '{}{}'.format(char_of_interest, counter)
			char_of_interest = char
			counter = 1
			#run on last character 
			if absolute_counter == len(input_string):
				processed_string += '{}{}'.format(char_of_interest, counter)


	return processed_string

def main():
	ellen_name = "ellen"
	ellen_compress = "e1l2e1n1"
	for char in ellen_name:
		print char

	raw_string = 'ellen'
	compress_string = 'e1l2e1n1'

	processed_string = string_compress(raw_string)
	print processed_string
	if processed_string == compress_string:
		print "you did it!"
	else:
		print "try again."

if __name__ == '__main__':
	main()