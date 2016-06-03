'''
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
nums should be [1, 3, 12, 0, 0].'''

def move_zeros(input_array):
	for num in input_array:
		if num == 0:
			input_array.remove(0)
			input_array.append(0)

	return input_array

def main():
    input_array = [0, 1, 0, 3, 12]
    print move_zeros(input_array)

if __name__ == "__main__": main()