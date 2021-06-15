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


class inordertraversal{

	public static void traversal(Node root,ArrayList result){
		
		if (root  ==  null){
			return; 
		}
		traversal(root.left,result);
		result.add(root.val);
		traversal(root.right,result);

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
	
		ArrayList<Integer> result = new ArrayList<>();
		preorderTraversal.traversal(node1,result);
		System.out.println(result)	;
	}
}
