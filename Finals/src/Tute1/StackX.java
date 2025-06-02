package Tute1;

public class StackX {
	private int maxSize;
	private int top;
	private int stackArr[];
	
	public StackX(int size) {
		maxSize = size;
		stackArr = new int[maxSize];
		top = -1;
	}
	
	public void push(int no) {
		if(isFull()) {
			System.out.println("The stack is full");
		}
		else {
			stackArr[++top] = no;
		}
	}
	
	public int pop(){
		if(!isEmpty()) {
			System.out.println("The stack is empty");
			return -1;
		}
		return stackArr[top--];
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
