'''
Using the Python language, have the function LetterChanges(str) take the str 
parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet 
(ie. c becomes d, z becomes a). 
Then capitalize every vowel in this new string (a, e, i, o, u) 
and finally return this modified string. 
'''
def letter_changes(input_str):
    output_str=""
    for char in input_str:
        if char.isalpha():
            ascii_code = ord(char)
            if char in ['z','d','h','n','t']:
                output_str = output_str + chr(ascii_code-31)
            else:
                output_str = output_str + chr(ascii_code+1)
        else:
            output_str = output_str + char

    return output_str


def main():
    input_str = "hello*3"
    print letter_changes(input_str)

if __name__ == "__main__": main()