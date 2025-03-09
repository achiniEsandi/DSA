package priorityQueue;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

public class main2 {

	public static void main(String[] args) {
		
		
		Queue<String> queue1 = new PriorityQueue<>();
		
		queue1.offer("B");
		queue1.offer("C");
		queue1.offer("A");
		queue1.offer("F");
		queue1.offer("D");
		
		while(!queue1.isEmpty()) {
			System.out.println(queue1.poll());
		}
		System.out.println();
		
		
		
		Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder());
		
		queue.offer("B");
		queue.offer("C");
		queue.offer("A");
		queue.offer("F");
		queue.offer("D");
		
		while(!queue.isEmpty()) {
			System.out.println(queue.poll());
		}
		
		
		
	}


}
