class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next

        print("None")

    


    """insert after:
needs head, target, and value to insert
traverse list until we find target
make value a node
make value point to target.next (value.next = target.next)
make target point next to value (target.next = value)
    """
    def insertAfter(self, target, value):
        
        cur = self.head
        while cur is not None:
            if cur.data == target:
                break
            cur = cur.next
        if cur is None:
            print("target not found")
            return "target not found"
        newNode = Node(value)
        newNode.next = cur.next
        cur.next = newNode
        return self.head
    
    def insertAtFront(self,value):
        newNode = Node(value)
        newNode.next = self.head
        return newNode

    """insertNode(self, pos, value)
    traverse list until at position
    if position is 1: insertAtFront(make new node, make newNode.next = head, return newNode)
    if current pos is pointing to None: target not found 
    make new node with value
    new node points to currents pointer
    current position points to new node
    return head

    """
    def insertNode(self,pos,value):
        cur = self.head
        if pos < 1:
            return self.head
        if pos == 1:
            newNode = Node(value)
            newNode.next = self.head
            return newNode
        for _ in range(1, pos-1):
            if cur is None:
                break
            cur = cur.next
        newNode = Node(value)
        newNode.next = cur.next
        cur.next = newNode
        return self.head

    def insertAtEnd(self, value):
        cur = self.head
        newNode = Node(value)
        if self.head is None:
            return newNode
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        return self.head

    def deleteHead(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp = None
        return self.head
    
    def deleteAtPos(self,pos):
        if pos < 1:
            return self.head
        if pos == 1:
            return LinkedList.deleteHead(self)
        cur = self.head
        for _ in range(1,pos-1):
            cur = cur.next
        
        if cur is None or cur.next is None:
            return self.head
        temp = cur.next
        cur.next = temp.next
        temp = None
        return self.head



SingleLst = LinkedList()
SingleLst.head = Node(1)
SingleLst.head.next = Node(2)
SingleLst.head.next.next = Node(3)
SingleLst.head.next.next.next = Node(4)
SingleLst.head.next.next.next.next = Node(5)

SingleLst.print()
SingleLst.insertAfter(2,2.5)
SingleLst.print()
SingleLst.head = SingleLst.insertAtFront(0)
SingleLst.print()
SingleLst.insertNode(6,3.5)
SingleLst.print()

SingleLst.insertAtEnd(6)
SingleLst.print()
SingleLst.head = SingleLst.deleteHead()
SingleLst.print()
SingleLst.head = SingleLst.deleteAtPos(1)
SingleLst.print()
