class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;
    //to track the least and recent, dummy ends
    private Node least;
    private Node recent;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.least = new Node(0,0);
        this.recent = new Node(0,0);
        this.least.next = this.recent;
        this.recent.prev = this.least;
    }
    
    //helper - change in linked list
    public void remove(Node node){
        //remove the node by getting the prev and next and pointing to each other, skip node
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next;
        next.prev = prev;
    }

    //helper - change in linked list
    public void insert(Node new_recent){
        //get the right most value (previous to recent), and the recent node, insert inbetween
        Node curr_recent = this.recent.prev;
        curr_recent.next = new_recent;
        new_recent.prev = curr_recent;

        //change dummy end's previous to new recent
        new_recent.next = this.recent;
        this.recent.prev = new_recent;
    }

    public int get(int key) {
        if(cache.containsKey(key)){
            // update the nodes, 
            // get is moved to most recent in linkedlist, 
            // no change to hashmap bc val not changed
            Node node = cache.get(key);
            remove(node);
            insert(node);

            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        //if it contains already remove from linked list to add again later
        //change in hashmap bc new value/node there to be updated 
        if(cache.containsKey(key)) {
            Node node = cache.get(key);
            remove(node);
        } 
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);

        if(cache.size() > capacity){
            Node lru = this.least.next;
            cache.remove(lru.key);
            remove(lru);
        }
    }
}

/*
doubly linked list - track recents 
keep a dummy left and right so it have the ends 

cache as hashmap - key and then the node, find in 0(1)

*/
