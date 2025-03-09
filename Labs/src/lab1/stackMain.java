package lab1;

public class stackMain {

	public static void main(String[] args) {
		stack stack1 = new stack(6);
		
		stack1.push('A');
		stack1.push('C');
		stack1.push('H');
		stack1.push('I');
		stack1.push('N');
		stack1.push('I');
		
		System.out.println(stack1.getCount());
		
		System.out.println("Peek: "+stack1.peek());
		
		System.out.println("Popped "+stack1.pop());
		
		//stack1.pop();
		
		
	}

}
