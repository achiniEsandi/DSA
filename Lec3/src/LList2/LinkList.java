package LList2;

public class LinkList {
	private Link first;
	
	public LinkList() {
		first = null;  //initially the connection is not created
	}
	
	public boolean isEmpty() {
		return(first == null);
	}
	
	//linked list cannot be full as there is no fixed size. No isFull()
	
	public void displayList() {
		Link current = first;
		
		while(current != null) {
			current.displayLink();
			current = current.next;
		}
	}
	
	public Link find(int key) {
		Link current = first;
		
		while(current != null) {
			if(current.iData == key) {
				return current;
			}
			
			else {
				current = current.next;
			}
		}
		return null;
		
		
	}
	
	
	public void insertFirst(int key) {
		Link nl = new Link(key);
		nl.next = first;
		first = nl;
		
	}
	
	
	/*public void deleteFirst() {
		first = first.next;
	}*/
	
	public Link deleteFirst() {
		Link temp = first;
		first = first.next;
		return temp;
		
	}
	
}
