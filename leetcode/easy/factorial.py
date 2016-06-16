'''Using the Python language, have the function FirstFactorial(num) 
take the num parameter being passed and return the factorial of it 
(ie. if num = 4, return (4 * 3 * 2 * 1)). 
For the test cases, the range will be between 1 and 18.'''

def factorial(input_num):
    output_num = 1
    for i in range(1,input_num+1):
        print i
        output_num = output_num*i
    return output_num

def main():
    input_num = 4
    print factorial(input_num)

if __name__ == "__main__": main()