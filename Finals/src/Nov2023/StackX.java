package Nov2023;

public class StackX {
	private int maxSize;
	private int top;
	private double stackArr[];
	
	public StackX(int size) {
		maxSize = size;
		stackArr = new double[maxSize];
		top = -1;
	}
	
	public void push(double no) {
		if(isFull()) {
			System.out.println("The stack is full");
		}
		else {
			stackArr[++top] = no;
		}
	}
	
	public double pop(){
		if(isEmpty()) {
			System.out.println("The stack is empty");
			return -1;
		}
		return stackArr[top--];
	}
	
	public double peek() {
        return stackArr[top];
    }
	
	
	public boolean isEmpty() {
		return (top==-1);
	}
	
	public boolean isFull() {
		return top==maxSize-1;
	}
	
	public int getCount() {
		return top+1;
	}
}
