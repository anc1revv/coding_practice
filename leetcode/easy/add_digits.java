/**
* https://leetcode.com/problems/add-digits/
*
* Given a non-negative integer num, repeatedly add all its digits
* until the result has only one digit.
*
* For example:
* Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
* Since 2 has only one digit, return it.
* 
* Follow up:
* Could you do it without any loop/recursion in O(1) runtime?
**/
public class add_digits {
	static int getSingleDigit (int num){
		int sum=0;
		while(num>9){
			sum = sum + num%10;
			num = num/10;
		}
		sum = sum+num%10;
		return sum;
	}

	public static void main(String[] args){
		int num = 382;
		int sum_num = getSingleDigit(num);
		while (sum_num>9){
			sum_num = getSingleDigit(sum_num);
		}
		System.out.println(sum_num);
	}
}

