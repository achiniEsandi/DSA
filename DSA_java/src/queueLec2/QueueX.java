package queueLec2;

public class QueueX {
	private int maxSize;
	private int queArray[];
	private int front;
	private int rear;
	private int nItems;
	
	public QueueX(int s) {
		maxSize = s;
		queArray = new int [maxSize];
		front = 0;
		rear = -1;
		nItems = 0;
	}
	
}
