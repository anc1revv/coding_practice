'''
Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num. 
For the test cases, the parameter num will be any number from 1 to 1000. 
'''
def simple_adding(num):
    total = 0
    for i in range(1,num+1):
        total = total + i
    return total

def main():
    num = 5
    print simple_adding(num)

if __name__ == "__main__": main()