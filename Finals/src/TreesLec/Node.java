package TreesLec;

public class Node {
	public int iData; //it number
	public double dData; //gpa
	public Node leftChild;
	public Node rightChild;
	
	//constructor
	public Node(int id, double dd) {
		iData = id;
		dData = dd;
		leftChild = null;
		rightChild = null;
	}
	
	public void displayNode() {
		System.out.println(iData+","+dData);
		
	}

}
