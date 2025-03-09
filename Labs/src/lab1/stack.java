package lab1;

public class stack {
	private int maxSize; //size of the stack array
	private char []stackArray;
	private int top;
	
	public stack(int s) {
		this.maxSize = s;
		this.stackArray = new char[maxSize];
		this.top = -1;
	}
	
	public void push(char j) {
		//check whether the stack is full
		//increment top
		//insert item
		if(top == maxSize - 1) {
			System.out.println("The stack is full");
		}
		
		else {
			stackArray[++top] = j;
		}
	}

	public char pop() {
		//check whether the stack is empty
		//if not, access item and decrement the top
		if(top == -1) {
			System.out.println("The stack is empty");
		}
		
		else {
			char temp = stackArray[top--];
			return temp;
		}
		return 0;
	}
	
	
	public char peek() {
		//check whether the stack is empty
		//if not, access item 
		if(top== -1) {
			System.out.println("The stack is empty");
		}
		
		else {
			char temp = stackArray[top];
			return temp;
		}
		return 0;
	}
	
	
	public int getCount() {
		return top+1;
	}
	
	
	
}
