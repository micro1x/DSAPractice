class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.top is None:
            return -1
        temp = self.top
        self.top = self.top.next
        val = temp.data
        del temp
        return val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        
        return self.top.data

    def isEmpty(self):
        return self.top is None

    


class LinkedList:
    def __init__(self):
        self.head = None

    def appendAtPos(self, pos, value):
        if pos < 1:
            return self.head
        if pos == 1:
            newNode = Node(value)
            newNode.next = self.head
            return newNode
        cur = self.head
        for _ in range(1,pos-1):
            if cur.next is None:
                break
            cur = cur.next
        newNode = Node(value)
        newNode.next = cur.next
        cur.next = newNode
        return self.head

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count