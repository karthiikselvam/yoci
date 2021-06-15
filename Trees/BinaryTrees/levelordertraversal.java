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


class levelordertraversal{

	public static ArrayList<Integer> traversal(Node root){
		Queue<Node> queue = new LinkedList<Node>();
		ArrayList<Integer> result = new ArrayList<>();	
		queue.add(root);	
		while(queue.size()!=0){
			Node node = queue.poll();

			result.add(node.val);
				
			if(node.left != null){
				queue.add(node.left);
			}
			if(node.right != null){
				queue.add(node.right);
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
		ArrayList<Integer> result = traversal(node1);
		System.out.println(result);
	}
}
