public class Node {
    int value;
    Node[] forward; // The forward array stores references to the next nodes at each level. forward[0] is the base-level. when having a base-list of (1,2,3,4) and starting at head.forward[0] = 2, head.forward[0].forward[0] = 3 etc.

    public Node(int value, int level) {
        this.value = value;
        this.forward = new Node[level + 1]; //  declare an array of size level+1 to be able to hold level elements.
    }
    public int getValue(){
        if(this != null){
            return this.value;
        }
        else{
            return -1;
        }
    }
}