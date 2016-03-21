/**
* http://courses.csail.mit.edu/iap/interview/Hacking_a_Google_Interview_Handout_2.pdf
*
* Write  a  function  to  reverse  the  order  of  words  in  a  string  in  place.
*
**/

public class reverse_string {
	static String reverseString(String input) {
		if (input.length() == 1) {
			return input;
		}
		String reverse="";
		for(int i=input.length()-1; i>=0; i--) {
			reverse = reverse + input.charAt(i);
		}
		return reverse;
	}

	public static void main (String[] args) {
		String st1 = "Andrew";
		String st2 = "Andre";
		System.out.println(reverseString(st1));
		System.out.println(reverseString(st2));
	}
}