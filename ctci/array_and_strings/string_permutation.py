# Given two strings, write a method that decides if one is a permutation
# of the other.

def check_perm(input_string1, input_string2):
	print "Checking '{0}' against '{1}'".format(input_string1,input_string2)

	if len(input_string1) != len(input_string2):
		return False

	


def main():
	input_string1 = "hello"
	input_string2 = "bye"
	input_string3 = "eyb"

	print check_perm(input_string1,input_string2)
	print check_perm(input_string2,input_string3)


if __name__ == '__main__':
	main()