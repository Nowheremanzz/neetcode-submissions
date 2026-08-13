class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node()
        self.last = Node()
        self.head.next = self.last
        self.last.prev = self.head
        self.capacity = capacity
    
    def update_node(self, node: Node) -> None:
        curr = node
        l = curr.prev
        r = curr.next
        l.next = r
        r.prev = l
        temp = self.last.prev
        temp.next = curr
        curr.prev = temp
        self.last.prev = curr
        curr.next = self.last

    def get(self, key: int) -> int:
        if key in self.map:
            curr = self.map[key]
            self.update_node(curr)
            return self.map[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            curr = self.map[key]
            curr.val = value
            self.update_node(curr)
        else:
            curr = Node(key, value)
            temp = self.last.prev
            temp.next = curr
            curr.prev = temp
            curr.next = self.last
            self.last.prev = curr
            self.map[key] = curr
        if len(self.map) > self.capacity:
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            temp.next = None
            temp.prev = None
            del self.map[temp.key]
            


        
