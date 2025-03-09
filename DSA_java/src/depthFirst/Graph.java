package depthFirst;

import java.util.*;

public class Graph {
	ArrayList<Node> nodes;
	int[][] matrix;
	
	Graph(int size){}
		public void addNode(Node node) {}
		public void addEdge(int src, int dst) {}
		public boolean checkEdge(int src,int dst) {
					return false;}
		public void print() {}
		
		public void breadthFirstSearch(int src) {
			
			Queue<Integer> queue  = new LinkedList<>();
			boolean[] visited = new boolean[matrix.length];
			
			queue.offer(src);
			visited[src] = true;
			
			while(queue.size() != 0) {
				src = queue.poll();
				
				System.out.println(nodes.get(src).data + " = visisted");
				
				for(int i=0; i<matrix[src].length; i++) {
					if(matrix[src][i] == 1 && !visited[i]) {
						queue.offer(i);
						visited[i] = true;
					}
				}
				
				
				
			}
			
		}
				
}
