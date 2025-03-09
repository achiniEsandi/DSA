package stack;

public class stackApp {

	public static void main(String[] args) {
		stackX stack1 = new stackX(3);
		
		stack1.push(30);
		stack1.push(80);
		stack1.push(100);
		stack1.push(25);
		
		
		while(!stack1.isEmpty()) {
			double v1 = stack1.pop();
			System.out.println(v1);
		}
		
		
	}

}
