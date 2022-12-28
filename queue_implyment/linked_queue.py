# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: linked_queue
# Author: xiaxu
# DATA: 2022/12/28
# Description:链队列的实现
# ---------------------------------------------------
from typing import Any, Iterator


class Node:
    """结点的实现"""
    def __init__(self,data:Any):
        """结点的元素和指针"""
        self.data:Any = data
        self.next:Node|None = None

    def __str__(self):
        """字符串表达形式"""
        return f"Node({self.data})"

class LinkedQueue:
    """链队列的实现"""
    def __init__(self):
        self.front:Node|None = None #对首指针
        self.rear:Node|None = None #队尾指针

    def __iter__(self)->Iterator[Any]:
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self)->int:
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def is_empty(self)->bool:
        return len(self) == 0

    def enqueue(self,data:Any)->None:
        """入队列的方法"""
        new_node = Node(data)
        if self.is_empty(): #当链队列为空时，front和rear都指向新结点
            self.rear = self.front = new_node
        else:
            #队尾指向新结点
            self.rear.next = new_node
            #rear指向新结点
            self.rear = new_node

    def dequeue(self):
        """出队列"""
        if self.is_empty():
            return "The Queue is empty"
        delete_node = self.front
        #将front指向下一个结点
        self.front = self.front.next
        #只有一个结点，删除后指向空
        if self.front is None:
            self.rear = None
        return delete_node.data

    def clear(self):
        self.rear = self.front = None

if __name__ == '__main__':
    linked_queue = LinkedQueue()
    print(linked_queue.is_empty())
    #入队列
    for i in range(10):
        linked_queue.enqueue(i)
    print(linked_queue)
    #出队列
    linked_queue.dequeue()
    print(linked_queue)
    print(linked_queue.is_empty())
    print(len(linked_queue))
