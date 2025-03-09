package queue;

import java.util.*;

public class Main {

	public Main() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		Queue<String> queue1 = new LinkedList<String>();
		
		//Adding elements to the queue
		queue1.add("Karen");   //will be the front
		queue1.add("Chad");
		queue1.add("Steve");
		queue1.add("Harold");  // will be the rear
		
		//Display queue 
		System.out.println(queue1);
		
		//PeekFront
		System.out.println("The front: "+queue1.peek());
		
		//Removing from the queue - The front will be removed first
		queue1.poll();
		
		//Display queue after polling
		System.out.println("Queue after removing: "+queue1);
		
		//To check if the queue is empty - returns boolean
		System.out.println(queue1.isEmpty());
		
		
		//To check the size of the queue
		System.out.println(queue1.size());
		
		//To check if the queue has a certain object - returns boolean
		System.out.println(queue1.contains("Harold"));
		
		
	}

}
