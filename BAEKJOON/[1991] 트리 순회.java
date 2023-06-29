import java.io.*;
import java.util.*;
public class Main {
    static class Node{
        char value;
        Node left;
        Node right;

        Node(char value, Node left, Node right){
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }

    static Node root = new Node('A', null, null);
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st[];
        int n = Integer.parseInt(br.readLine());
        char parent, left, right;
        for(int i = 0; i < n; i++){
            st = br.readLine().split(" ");
            parent = st[0].charAt(0);
            left = st[1].charAt(0);
            right = st[2].charAt(0);
            makeTree(root, parent, left, right);
        }

        preOrder(root);
        System.out.println();
        inOrder(root);
        System.out.println();
        postOrder(root);
    }

    public static void makeTree(Node top, char parent, char left, char right){
        if(parent == top.value){
            top.left = (left == '.' ? null : new Node(left, null, null));
            top.right = (right == '.' ? null : new Node(right, null, null));
        }
        else{
            if(top.left != null){
                makeTree(top.left, parent, left, right);
            }
            if(top.right != null){
                makeTree(top.right, parent, left, right);
            }
        }
    }

    public static void preOrder(Node n){
        if(n == null){
            return;
        }
        System.out.print(n.value);
        preOrder(n.left);
        preOrder(n.right);
    }

    public static void inOrder(Node n){
        if(n == null){
            return;
        }
        inOrder(n.left);
        System.out.print(n.value);
        inOrder(n.right);
    }

    public static void postOrder(Node n){
        if(n == null){
            return;
        }
        postOrder(n.left);
        postOrder(n.right);
        System.out.print(n.value);
    }
}
