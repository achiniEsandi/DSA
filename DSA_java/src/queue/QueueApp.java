package queue;

public class QueueApp {

	public QueueApp() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		QueueX q1 = new QueueX(10); 
		
		q1.insert(10);
		q1.insert(25);
		q1.insert(55);
		q1.insert(65);
		q1.insert(85);
		
		System.out.println("inserted");
		
		while(!q1.isEmpty()) {
			int val = q1.remove();
			System.out.println(val);
		}
		
	}

}
