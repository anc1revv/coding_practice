'''Write a function that takes a string as input and returns the string reversed.'''

def reverse_string(input_str):
	rev_string = ''
	for char in input_str:
		rev_string = char + rev_string

	return rev_string

def main():
    input_str = "hello"
    print reverse_string(input_str)

if __name__ == "__main__": main()