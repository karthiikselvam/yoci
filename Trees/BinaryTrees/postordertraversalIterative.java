import java.util.*;
class Node{
	
	int val ;
	Node left;
	Node right ;

	public Node(int val){
		this.val = val;
		this.left = null;
		this.right = null;
	}
}


class postordertraversalIterative{

	public static Stack<Integer> traversal(Node root){
		Stack<Integer> result = new Stack<>();
			
		Stack<Node> stack  = new Stack<>();
		stack.push(root);
		
		while( !stack.empty()){
			Node node = stack.pop();
			result.add(node.val);

			if (node.left != null){
				stack.add(node.left);
			}
			if (node.right != null){
				stack.add(node.right);
			}
		}
		return result;
	}

	public static void main(String args []){
		Node node1 = new Node(1);
		Node node2 = new Node(2);
		Node node3 = new Node(3);
		Node node4 = new Node(4);
		Node node5 = new Node(5);
		
		node1.left = node2;
		node1.right= node3;
		node2.left = node4;
		node2.right= node5;
	
		Stack<Integer> result = traversal(node1);
		while(!result.empty()){
			int val = result.pop();
			System.out.print(val);
		}
			
	}	
	}
