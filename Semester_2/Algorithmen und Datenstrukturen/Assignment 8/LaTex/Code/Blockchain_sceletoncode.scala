import java.security.MessageDigest

class BlockNode(val data: String, val prevHash: String, val nonce: Int = 0):
  // Next node reference
  var next: BlockNode = null
  
  // Compute this node's hash including prevHash, data, and nonce
  val hash: String = computeHash(prevHash + data + nonce.toString)
  
  // Compute hash using SHA-256
  private def computeHash(input: String): String =
    val digest = MessageDigest.getInstance("SHA-256")
    val hashBytes = digest.digest(input.getBytes("UTF-8"))
    hashBytes.map("%02x".format(_)).mkString
  
  // For proof-of-work: find nonce that creates hash with specified number of zeros
  def mineBlock(difficulty: Int): BlockNode =
    val target = "0" * difficulty
    var currentNonce = 0
    var currentHash = computeHash(prevHash + data + currentNonce.toString)
    
    while !currentHash.startsWith(target) do
      currentNonce += 1
      currentHash = computeHash(prevHash + data + currentNonce.toString)
    
    new BlockNode(data, prevHash, currentNonce)

class HashLinkedList:
  private var head: BlockNode = null
  private val genesisHash = "0" * 64  // Initial hash for first block
  
  // Add a new node to the list
  def add(data: String, difficulty: Int = 0): Unit =
    val prevHash = if head == null then genesisHash else head.hash
    val newNode = new BlockNode(data, prevHash)
    
    // If proof-of-work is required, mine the block
    val minedNode = if difficulty > 0 then newNode.mineBlock(difficulty) else newNode
    
    // Add to front of list
    minedNode.next = head
    head = minedNode
  
  // Verify integrity of the chain
  def verifyChain(): Boolean =
    if head == null then return true
    
    var current = head
    while current.next != null do
      val computedHash = current.computeHash(current.next.prevHash + current.next.data + current.next.nonce.toString)
      if current.next.hash != computedHash || current.hash != current.next.prevHash then
        return false
      current = current.next
    
    true
  
  // Other methods like toString, get, etc.
  override def toString: String =
    var result = "HashLinkedList:\n"
    var current = head
    while current != null do
      result += s"Data: ${current.data}, Hash: ${current.hash.take(10)}..., PrevHash: ${current.prevHash.take(10)}..., Nonce: ${current.nonce}\n"
      current = current.next
    result