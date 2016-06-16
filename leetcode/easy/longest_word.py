'''
Using the Python language, have the function LongestWord(sen) 
take the sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, 
return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. 
'''
import re
def longest_word(input_str):
    word_list = input_str.split(" ")
    longest_word = ""

    for word in word_list:
        scrubbed_word = re.sub(r'\W+','',word)
        if len(scrubbed_word) > len(longest_word):
            longest_word = scrubbed_word

    return longest_word

def main():
    input_str = "longe$%^st word in this sentence"
    print longest_word(input_str)

if __name__ == "__main__": main()