# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: linked_stack
# Author: xiaxu
# DATA: 2022/12/22
# Description:栈的链式存储的实现
# ---------------------------------------------------
from __future__ import annotations

from typing import Generic, TypeVar, Iterator

#声明接收的类型为任意类型
T = TypeVar('T')


class Node(Generic[T]):
    """链栈的结点，实际同单链表相似"""
    def __init__(self,data:T):
        self.data = data
        self.next:Node[T] |None  =None

    def __str__(self)->str:
        return f"{self.data}"


class LinkedStack(Generic[T]):
    """链栈的定义，将head指针作为栈顶top指针push表示入栈操作pop表示出栈操作"""
    def __init__(self):
        self.top:Node[T] |None = None

    def __iter__(self)->Iterator[T]:
        """
        迭代器，遍 历单链表的数据
        """
        node = self.top  #起始位置
        while node:
            yield node.data
            node = node.next

    def __len__(self)->int:
        """此魔法方法实现了求单链表的长度，len()方法自动调用"""
        return len(tuple(iter(self)))

    def __repr__(self):
        """链表字符串可视化，类似于1->3->6,当str()方法自动调用"""
        return "->".join([str(item) for item in self])

    def __getitem__(self, index:int)->Iterator[T]:
        """对于索引的支持，用来获取指定位置的一个结点"""
        if not 0<=index<=len(self):
            raise IndexError("index out of range!")
        for i,node in enumerate(self):
            if i == index:
                return node

    def push(self,data:T)->None:
        new_node = Node(data)
        if not self.is_empty(): #栈为空时还没有top指针
            new_node.next=self.top  #新结点指向栈顶
        self.top = new_node #top指针指向新结点

    def pop(self)->T:
        if len(self) == 0:
            raise IndexError("pop stack_implyment data is none")
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

    def is_empty(self):
        return self.top is None

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return IndexError("peek from empty stack_implyment!")
        assert self.top is not None
        return self.top.data

    def clear(self)->None:
        self.top = None


#以下为测试
def test_01():
    linked_stack = LinkedStack()
    #测试判断空栈功能
    assert linked_stack.is_empty() is True
    #测试入栈操作
    print("空栈",str(linked_stack))
    for i in range(11):
        linked_stack.push(i+1)
    print("入栈",str(linked_stack))
    #测试出栈操作
    linked_stack.pop()
    print("出栈",str(linked_stack))
    #测试栈顶方法
    print('栈顶',linked_stack.peek())

if __name__ == '__main__':
    test_01()
