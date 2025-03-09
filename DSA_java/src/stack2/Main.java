package stack2;

import java.util.Stack;

public class Main{
	public static void main(String[] args) {
		
		Stack<String> bookStack = new Stack<String>();
		
		System.out.println(bookStack.empty());
		
		bookStack.push("Sherlock Holmes");
		bookStack.push("Malory Towers");
		bookStack.push("St.Clairs");
		bookStack.push("Percy Jackson");
		
		System.out.println(bookStack);
		
		String v1 = bookStack.pop();
		String v2 =bookStack.pop();
		
		System.out.println(bookStack);
		//System.out.println(v2);
		
		System.out.println(bookStack.peek());

	}

}
