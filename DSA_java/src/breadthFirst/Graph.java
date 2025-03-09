package breadthFirst;

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
		
		public void depthFirstSearch(int src) {
			boolean[] visited = new boolean[matrix.length];
			dFSHelper(src,visited);
			
		}
		
		private void dFSHelper(int src, boolean[] visited) {
			if(visited[src]) {
				return;
			}
			
			else {
				visited[src] = true;
				System.out.println(nodes.get(src).data + " = visited");
			}
			
			
			for(int i=0; i < matrix[src].length; i++) {
				if(matrix[src][i] == 1) {
					dFSHelper(i, visited);
					
				}
			}
			
			return;
			
			
			
		}
				
}
