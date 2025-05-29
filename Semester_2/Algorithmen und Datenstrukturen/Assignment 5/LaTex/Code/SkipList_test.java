/*scources: https://www.geeksforgeeks.org/java-util-random-nextint-java/
            ADS Skript
            https://github.com/LJWittenberg/Java-code-for-Refactoring (refactorcode unteranderen)
            https://www.tutorialspoint.com/java/util/random_nextdouble.htm
            https://stackoverflow.com/questions/2707322/what-is-null-in-java
            https://www.baeldung.com/java-skiplist#bd-5-delete-operation
            https://stackoverflow.com/questions/7630014/difficulty-throwing-nosuchelementexception-in-java
            https://rollbar.com/guides/java/how-to-throw-exceptions-in-java/

*/
import java.util.Random;
public class SkipList_test {
    // declare and initialize 3 test Skiplists.
    // 1. 1-20 inserted in assending order
    // 2. 20 random Int values between 1-50
    // 3. 1-20 inserted in reverse order
    public static void main(String[] args){
        SkipList sklst1 = new SkipList();
        SkipList sklst2 = new SkipList();
        SkipList sklst3 = new SkipList();
        SkipList sklst0 = new SkipList(); // empty List
        for(int i = 1; i <= 20; i++){
            sklst1.insert(i);
        }
        PrintSkipList(sklst1);
        Random randomgen = new Random();
        for(int i = 1; i <= 20; i++){
            sklst2.insert(randomgen.nextInt(1,50));
        }
        PrintSkipList(sklst2);
        for(int j = 20; j >= 1; j--){
            sklst3.insert(j);
        }
        PrintSkipList(sklst3);
        PrintSkipList(sklst0);
        // lookup test:
        Node searchResult = new Node(0,10);
        searchResult = searchHandler(sklst1,10); // look for value that exists. expected output: the wanted Node 
        if(searchResult.getValue() == 0){
            System.out.println("The wanted Node does not exit in the selected SkipList returning std.Failuire Value: 0");
        }
        else{
            System.out.println(searchResult.getValue());
        }
        searchResult = searchHandler(sklst1,30); // look for value that does not exist. expected output: the wanted Node
        if(searchResult.getValue() == 0){
            System.out.println("The wanted Node does not exit in the selected SkipList returning std.Failuire Value: 0");
        }
        else{
            System.out.println(searchResult.getValue());
        }
        // deletion test:
        sklst0.delete(1); // deleting from empty List.
        // deleting 3 nodes from the assending list 
        sklst1.delete(10);
        sklst1.delete(1);
        sklst1.delete(20);
        PrintSkipList(sklst1);
        // deleting an node that does not exists
        sklst3.delete(30);
        PrintSkipList(sklst3);
        // deleting a node in the highest populated level.
        int hgtLevel3 = sklst3.getLevel();
        Node hgtNode3 = sklst3.getHead().forward[hgtLevel3];
        int hgtNode3Val = hgtNode3.getValue();
        sklst3.delete(hgtNode3Val);
        PrintSkipList(sklst3);
        return;
    }
    // helperfunction to visualize the SkipList
    public static void PrintSkipList(SkipList sklst){
        int printLevels = sklst.getLevel();
        
        for(int i = printLevels; i >= 0; i--){
            Node curr = sklst.getHead();
            System.out.print("Level "+ i + ": HEAD ->");
            while(curr.forward[i] != null){
                curr = curr.forward[i];
                System.out.print(curr.getValue() + " -> ");
            }
            System.out.println("TAIL");
            
        }
        System.out.println();
        return;
    }
    // helperfunction to avoid manuell null-handling every time SkipList.search() is used.
    public static Node searchHandler(SkipList lst ,int value){
        Node result = new Node(0,lst.getLevel());
        try{
            result = lst.search(value);
        } catch (Exception e){
            e.printStackTrace();
        }
        return result;
        
    }
}