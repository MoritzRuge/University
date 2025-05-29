import java.util.Random;
import java.util.NoSuchElementException;

public class SkipList {
    private Node head;
    private int maxLevel;
    private int level;
    private Random random;

    public SkipList() {
        maxLevel = 6; // maximum number of levels
        // working with low upper-bounds and therefore also with smaller skriplists for readability and debugging.
        level = 0; // current level of SkipList
        head = new Node(Integer.MIN_VALUE, maxLevel);
        random = new Random(); // for randomness of coinflips
    }
    public int getLevel(){
        return this.level;
    }
    public Node getHead(){
        return this.head;
    }
    private int randomLevel() { // determine how often a new inserted node will be promoted to a higher level.
        int lvl = 0;
        // Keep flipping coins as long as we get heads (probability < 0.5)
        // and we haven't reached maxLevel
        while (random.nextDouble() < 0.5 && lvl < this.maxLevel) {
            lvl++;
        }
        return lvl;
    }
    // Returns an array of predecessors where predecessors[i] is the last node
    // at level i whose value is less than the search value.
    private Node[] findPredecessors(int searchValue) {
        Node[] predecessors = new Node[maxLevel + 1];
        Node curr = head;
        // begin search at highest populated level. continue until node is found on the lowest level if present. 
        for (int i = this.level; i >= 0; i--) {
            // move right as long as there are values on the same level, that a smaller than the searchValue. else move down 1 level
            while (curr.forward[i] != null && curr.forward[i].value < searchValue) {
                curr = curr.forward[i];
            }
            predecessors[i] = curr;
        }
        
        return predecessors;
    }
    // lookup -> check if a given node is part of the Skiplist
    public Node search(int searchValue){ 
        Node[] preds = this.findPredecessors(searchValue);
         // At level 0 preds[0] is the greatest node thats still smaller, than the searchValue node.value < searchValue
        Node curr = preds[0].forward[0]; // expected found position

        if(curr.value == searchValue && curr != null){
            return curr; // if the current node is the wanted node than return that node
        }
        else{
            throw new NoSuchElementException();
            //return null; // else return null -> the wanted node is not part of the SkipList.
        }
    }
    public void insert(int value){ // insertion -> insert a node with a given value into the SkipList.
        Node[] preds = this.findPredecessors(value); // get all predecessors of the node that have smaller values than value. This variable 
        Node curr = preds[0]; // get the greatest node in the SkipList that whos value is still smaller than value.
        Node successor = curr.forward[0]; // Node to check if a node with the given value already exists seperatly.

        if(successor != null && successor.value == value){ // node with value exists no insertion return.
            return;
        }
        // the given value is not part of the SkipList.
        int newNodeLvL = randomLevel(); // flip coins to determine the levels where the newNode should be on.
        if(newNodeLvL > this.level){ // if the rolled highest level of the newNode is higher, than the highest currently populated level. add empty levels ontop
            for(int i = this.level+1; i <= newNodeLvL; i++){
                preds[i] = this.head;
            }
            this.level = newNodeLvL;
        }
        Node newNode = new Node(value, newNodeLvL); // declare and initialize the new node with the given value and new nodes maxlevel.
        for(int i = 0; i <= newNodeLvL;i++){ // from the base-level too the highest populated level
            // one each level newNode.successor becomes the successor of the current predecessor, which is greater than newNode. 
            // This includes the case where insertion adds a node at the end of the skiplist. in theory that is tail.value = +infinity and in implementation practice its just null.
            newNode.forward[i] = preds[i].forward[i]; 
            preds[i].forward[i] = newNode; // after the copy process the successor of pred[i] becomes the newNode.
        }
    }
    public void delete(int value){ // deletion -> delete a existing node with given Value from all SkipList levels.
        Node[] preds = this.findPredecessors(value); // get all predecessors of the node that have smaller values than value. This variable 
        Node curr = preds[0].forward[0]; // curr is now the Node to be deleted.

        if(curr != null && curr.value == value){ // if curr is indeed the node to be deleted begin deletion process. else do nothing and exit the function.
            for(int i = 0; i <= this.level;i++){ // from the base-levek to the highest populated level delete curr by:
                if(preds[i].forward[i] != curr){ // if on any level the current node to be deleted isn't there anymore -> stop as curr has been deleted.
                    return;
                }
                preds[i].forward[i] = curr.forward[i]; // delete curr by skipping over it and "cutting" connection with its predeseccor and successor -> cleaned up by garbage collector.
            }
            // after deleting curr check for empty levels from top to bottom and remove them by decrementing the level attribute. 
            while(level > 0 && this.head.forward[level] == null){
                level--;
            }
        }
    }
}   