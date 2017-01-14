# Implement an algorithm to determine if a string has all unique
# characters. What if you cannot use additional data structures?

def check_unique(input_str):
	print "Checking string: {0}".format(input_str)

	char_set = set()

	for char in input_str:
		if char in char_set:
			return False
		else:
			char_set.add(char)

	return True

def check_unique_without_ds(input_str):
	print "Checking string without ds: {0}".format(input_str)
	if not input_str or len(input_str) < 1:
		print "Invalid String"
		return False

	index = 0
	for outer_letter in input_str:
		index =+ index + 1
		print "outer letter: {0}".format(outer_letter)
		for inner_letter in input_str[index:]:
			print "inner letter:{0}".format(inner_letter)
			if outer_letter == inner_letter:
				return False


	return True


def main():
	hello = "hello"
	andrew = "andrew"

	print check_unique(hello)
	print check_unique(andrew)

	print check_unique_without_ds(hello)

if __name__ == '__main__':
	main()