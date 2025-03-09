package stackX;

public class stack {
		private char[] stackArray;
		private int top;
		private int maxSize;
		
		//Constructor
		public stack(int size) {
			this.maxSize = size;
			this.stackArray = new char[maxSize];
			this.top = -1;
			
			
			
		}
}
