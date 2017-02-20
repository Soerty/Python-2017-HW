#!/usr/bin/env python3
# -*- coding: utf-8 -*-




class Node:
    __slots__ = ['data', 'next']

    def __init__(self, data, next=None):
        self.data = data
        self.next = next




class LinkedList:
    def __init__(self, head=None):
        self.head = head


    def empty(self):
        if self.head:
            return False
        return True


    def printList(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print()


    def push(self, data):
        node = Node(data, next=self.head)
        self.head = node


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node


    def size(self):
        size = 1 if self.head.next else 0
        current = self.head

        while current.next is not None:
            current = current.next
            size += 1

        return size


    def delete(self, value):
        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                break
            current = current.next


    def insert(self, index, value):
        if index >= 0:
            current = self.head

            while index != 0 and current.next is not None:
                index -= 1
                current = current.next

            new_node = Node(value, current.next)
            current.next = new_node


    def reverseList(self):
        node = self.head
        tail = None

        while node:
            next = node.next
            node.next = tail
            tail = node
            node = next

        self.head = tail




if __name__ == '__main__':
    n3 = Node(3)
    n2 = Node(2, next=n3)
    n1 = Node(1, next=n2)


    l = LinkedList(head=n1)
    for i in [1,2,3,4,5,4,5,6,6,6,6,1,1,54,3]:
        l.append(i)
    l.printList()

    l.reverseList()

    print (l.size())
    l.insert(3, 100)
    l.delete(100)
    l.printList()
    print (l.size())