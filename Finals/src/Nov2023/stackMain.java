package Nov2023;

public class stackMain {

	public static void main(String[] args) {
		StackX myStack = new StackX(4);
		myStack.push(56);
		myStack.push(8);
		myStack.push(45);
		myStack.push(11);
		
		StackX sortedStack = new StackX(4);
		
		while (!myStack.isEmpty()) {
		    double temp = myStack.pop();

		    while (!sortedStack.isEmpty() && sortedStack.peek() > temp) {
		        myStack.push(sortedStack.pop());
		    }

		    sortedStack.push(temp);
		}

		// Print sorted stack (optional)
		while (!sortedStack.isEmpty()) {
		    System.out.println(sortedStack.pop());
		}

		
		
	}

}
