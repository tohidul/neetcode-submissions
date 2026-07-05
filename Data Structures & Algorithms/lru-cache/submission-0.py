class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        self.lru = {}
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        

    def get(self, key: int) -> int:
        if key in self.lru:
            self.remove(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(self.lru[key])
        self.lru[key] = Node(key, value)
        self.insert(self.lru[key])

        if len(self.lru) > self.cap:
            last = self.left.next
            self.remove(last)
            del self.lru[last.key]


                

        
