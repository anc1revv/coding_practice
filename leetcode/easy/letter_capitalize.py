'''
Using the Python language, have the function LetterCapitalize(str) take the str 
parameter being passed and capitalize the first letter of each word. 
Words will be separated by only one space. 

'''
def letter_capitalize(input_str):
	list_words = input_str.split(" ")

	
	for word in list_words:
		for i in range(len(word)):
			if i == 0:



	return ' '.join(list_words)

def main():
    input_str = "hello bye"
    print letter_capitalize(input_str)

if __name__ == "__main__": main()