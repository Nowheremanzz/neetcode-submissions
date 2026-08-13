class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.n = 0
        self.head = None
        self.last_node = None
        self.capacity = capacity
    
    def update_node(self, node: Node) -> None:
        curr = node
        temp, pre = curr.next, curr.prev
        if self.head == curr:
            self.head = curr.next
            curr.next.prev = None
            curr.next = None
            curr.prev = self.last_node
            self.last_node.next = curr
            self.last_node = curr
        else:
            pre.next = temp
            temp.prev = pre
            self.last_node.next = curr
            curr.prev = self.last_node
            curr.next = None
            self.last_node = curr

    def get(self, key: int) -> int:
        if key in self.map:
            curr = self.map[key]
            if self.last_node != curr:
                self.update_node(curr)
            return self.map[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if not self.head:
            curr = Node(key, value)
            self.head = curr
            self.last_node = curr
            self.map[key] = curr
            self.n += 1
        elif key in self.map:
            curr = self.map[key]
            curr.val = value
            if self.last_node != curr:
                self.update_node(curr)
        else:
            curr = Node(key, value, self.last_node or None)
            self.last_node.next = curr
            self.last_node = curr
            self.map[key] = curr
            self.n += 1
        if self.n > self.capacity:
            temp = self.head
            self.head = temp.next
            if temp.next:
                temp.next.prev = None
            temp.next = None
            del self.map[temp.key]
            self.n -= 1
            


        
