package stack;

public class stackX {

	private int maxSize;  //size of stack array
	private double[] stackArray;
	private int top; //top of the stack
	
	public stackX(int s) {   //constructor
		
		maxSize = s;   //set array size
		stackArray = new double[maxSize]; 
		top = -1;  //means that the stack is empty	
	}

	public void push(double j) {
		//increment top and then insert item
		
		//check whether the stack is full
		if(top == maxSize-1) {
			System.out.println("Stack is full");
		}
		
		else {
			stackArray[++top] = j;
		}
		
	}
	
	public double pop() {
		if (top == -1)
		      return -99;
		else
		      return stackArray[top--];
	 }

	
	
	
	public double peek() {
		if (top == -1)
		      return -99;
	              	else
		      return stackArray[top];
	}

	public boolean isEmpty() {
	    return (top == -1); // Return true if `top` is -1 (stack is empty)
	}

	public boolean isFull() {
	    return (top == maxSize - 1); // Return true if `top` has reached the last index
	}
	
	
	public int getCount() {
		return top+1;
	}
	
	
	
	
	
	
	


}
