package LList2;

public class LinkMain {

	public static void main(String[] args) {
		LinkList l1 = new LinkList();
		
		l1.insertFirst(10);
		l1.insertFirst(20);
		l1.insertFirst(30);
		l1.insertFirst(40);
		
		l1.displayList();
		
		while(!l1.isEmpty()) {
			Link temp = l1.deleteFirst();
			System.out.println("Deleting " + temp.iData); //As temp is a link object we cannot simply say temp
		}
	}

}
