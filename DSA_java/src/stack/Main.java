package stack;

import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Stack<String> stack1 = new Stack<String>();
		
		System.out.println("Is stack1 empty? "+stack1.empty());
		
		
		stack1.push("DSA");
		stack1.push("PSA");
		stack1.push("ITP");
		stack1.push("MAD");
		stack1.push("PS");
		stack1.push("ESD");
		
		System.out.println("Is stack1 still empty? "+stack1.empty()+"\n");
		
		System.out.println("Stack: "+stack1+"\n");
		
		stack1.pop();
		System.out.println("Stack after popping: "+stack1);
		
		System.out.println("Top object: "+stack1.peek()+"\n");
		
		System.out.println("Index of 'MAD': "+stack1.search("MAD"));
		
		System.out.println("Index of 'DMS': "+stack1.search("DMS"));
		
	}

}
