class HashTable(size : Int, compressionFunktion: Int => Int):
    // public changable Attribute to alter, hold and display the (Key,Values) pairs.
    // Using Array two a fixed size for the Hashtable and dynamic List Chains.
    private var Table = Array.fill[List[(Int,Int)]](size)(Nil)
    private var numEntries = 0 // counter pairs in Table
    private var loadFactorCheck = 20 // indicator when the Table needs to be resized

    private def resize(newSize : Int) : Unit =
        val oldTable = this.Table
        this.size = newSize
        this.Table = Array.fill[List[(Int,Int)]](this.size)(Nil)
        this.numEntries = 0
        this.loadFactorCheck = loadFactorCheck * 2
        // copy all old pairs into the resized Table.
        for chain <- oldTable do
            for (k,v) <- chain do 
                put(k,v)

    // Two-Part hash-function 1. builtin hashCode and 2. class instances given compression function to create a index for the Table
    def hash(key : Int) : Int = 
        val hashedPosition = key.hashCode()
        val index = compression_division(hashedPosition,size)

    // main 3 Operations
    // get(k,v)
    def get(key : Int) : Int =
        val index : Int = hash(key) // 1. get the starting index
        //2.Search the linked list at T[i] for an entry with key k
        //3.If found, return the associated value
        //4.If not found, throw NoSuchElementException in this case std error value 
        var chain : List[(Int,Int)] = this.Table(index)
        var res : Int = -1 // std return value -> handling in main
        for (k,v) <- chain do
            if k == key then 
                res = v
        res
    
    //remove(k)
    //1.Calculate index i = h(k)
    //2.Search the linked list at T[i] for an entry with key k
    //3.If found, remove that node from the linked list
    //4.If not found -> nothing happens in this implementation
    def remove(key : Int) : Unit =
        val index : Int = hash(key)
        val initalLength : Int = this.Table(index).length
        Table(index) = Table(index).filter(_._1 != key)
        if Table(index).length != initalLength then
            this.numEntries -= 1 // keeping track of the number of entries

    // put(k,v)
    //  1.Calculate index i = h(k)
    //  2.Search the linked list at T[i] for an entry with key k
    //  3.If found, update its value to v
    //  4.If not found, append a new node with (k,v) to the list at T[i]
    def put(key : Int, value : Int): Unit =
        val index : Int = hash(key)
        var chain : List[(Int,Int)] = this.Table(index)
        chain = chain.map(x = > if(x._1 == key) then (key,value) else x)    // map over chain if entry.key == wanted key -> update value
        if chain.filter(_._1 == key).length == 0 then                       // After maping no entry with key present -> append
            chain = chain ::: List((key, value))
            this.numEntries += 1                                            // keeping track of the number of entries
        this.Table(index) = chain                                           // update the chain in Table with the new altered Chain
        if numEntries >= loadFactorCheck then   // if more Entires than the current loadFactorCheck allows are in the Table -> resize accordingly
            val loadFactor = this.numEntries.toDouble / this.size
            if loadFactor < 1 then      // loadFactor too small
                resize(this.size/2)
            if loadFactor > 3 then      // loadFactor too high
                resize(this.size*2)

//compression functions modeled after the script
def compression_division(hash : Int, size : Int): Int =
    hash % size
def compression_multiplication(hash : Int, size : Int): Int = 
    val A : Float = 0.6180339887 // 0.6180339887 is the standard value from the script.
    val product = hash * A 
    val fraction = product - Math.floor(product)
    (size * fraction).toInt

// main-function for debugging and testing
@main def main(): Unit = 
    var HT : HashTable = HashTable(10,compression_division)