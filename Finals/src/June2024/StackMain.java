package June2024;

import java.util.Scanner;

public class StackMain {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter a string: ");
		String input = sc.next();
		
		StackX stack = new StackX(input.length());
		
		if (stack.isBalanced(input)) {
            System.out.println("Parentheses are balanced");
        } else {
            System.out.println("Parentheses are imbalanced");
        }

	}

}


