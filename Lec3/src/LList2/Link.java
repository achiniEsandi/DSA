package LList2;

public class Link {
	public int iData;
	public Link next;
	
	public Link(int data) {
		iData = data;
		next = null; //as there is only one link
	}
	
	public void displayLink() {
		System.out.println(iData);
	}
}
