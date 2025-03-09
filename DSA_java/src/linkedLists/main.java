package linkedLists;

import java.util.*;

public class main {
	public static void main(String args[]) {
		
		LinkedList<String> linkedList = new LinkedList<String>();
		/*
		linkedList.push("A");
		linkedList.push("B");
		linkedList.push("C");
		linkedList.push("D");
		linkedList.push("E");
		linkedList.push("F");
		
		linkedList.pop();
		
		System.out.println(linkedList);
		
		*/
		
		linkedList.offer("A");
		linkedList.offer("B");
		linkedList.offer("C");
		linkedList.offer("D");
		linkedList.offer("F");
		
		//linkedList.poll();
		
		linkedList.add(4,"E");
		linkedList.remove("E");
		System.out.println("The index of F is "+linkedList.indexOf("F"));
		
		System.out.println(linkedList);
		
		System.out.println(linkedList.peekFirst());
		System.out.println(linkedList.peekLast());
		
		
		linkedList.addFirst("0");
		linkedList.addLast("G");
		
		String first = linkedList.removeFirst();
		String last = linkedList.removeLast();
		
		System.out.println(linkedList);
	}
}
