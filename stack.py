# -*- coding: utf-8 -*-




"""Класс реализующий тип данных Стек."""
class Stack(object):
    def __init__(self):
        self.stack = []


    """Добавление элемента в конец стека."""
    def push(self, item):
        self.stack.append(item)


    """
    Удаление элемента с конца. Возвращает значение
    удаляемого элемента или None, если стек пуст.
    """
    def pop(self):
        return self.stack.pop() if self.stack else None


    """
    Значение последнего элемента с конца.
    Возвращает значение или None, если стек пуст.
    """
    def peek(self):
        return self.stack[-1] if self.stack else None


    """Возвращает True, если стек не пуст, иначе False."""
    def isEmpty(self):
        return (self.stack == [])




"""Класс реализующий тип данных Очередь."""
class MyQueue(object):
    def __init__(self):
        self.stack = Stack()


    """Добавляет значение в очередь"""
    def enqueue(self, item):
        self.stack.push(item)


    """
    Возвращает первое значение из очереди удаляя его.
    Или None, если очередь пуста.
    """
    def dequeue(self):
        temp_stack = Stack()

        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())

        item = temp_stack.pop()

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

        return item


    """
    Возвращает первый элемент очереди не удаляя его.
    Или None, если очередь пуста.
    """
    def peek(self):
        temp_stack = Stack()

        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())

        item = temp_stack.peek()

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

        return item


    """True, если очередь не пуста, иначе False."""
    def isEmpty(self):
        return self.stack.isEmpty()




if __name__ == '__main__':
    queue = MyQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    while not queue.isEmpty():
        print (queue.peek())
        queue.dequeue()