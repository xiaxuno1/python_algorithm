# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: line_stackt
# Author: xiaxu
# DATA: 2022/12/22
# Description:线性表的栈
# ---------------------------------------------------
from __future__ import annotations

from typing import Generic, TypeVar


#声明接收的类型为任意类型
T = TypeVar('T')


class LineStack(Generic[T]):
    """线性表生成的栈，push表示入栈操作pop表示出栈操作"""
    def __init__(self,limit:int=20):
        self.stack:list[T] =[]
        self.limit = limit

    def __str__(self):
        return str(self.stack)

    def __bool__(self):
        return bool(self.stack)

    def push(self,data:T)->None:
        if len(self.stack)>self.limit:
            raise IndexError("push data out of limit!")
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("pop stack_implyment data is none")
        return self.stack.pop()

    def is_empty(self):
        return not bool(self.stack)

    def if_full(self):
        return len(self.stack) == self.limit

    def peek(self):
        """返回栈顶元素"""
        return self.stack[-1]


#以下为测试
def test_01():
    line_stack = LineStack()
    #测试判断空栈功能
    assert line_stack.is_empty() is True
    #测试入栈操作
    print("空栈",str(line_stack))
    for i in range(11):
        line_stack.push(i+1)
    print("入栈",str(line_stack))
    #测试出栈操作
    line_stack.pop()
    print("出栈",str(line_stack))
    #测试栈顶方法
    print('栈顶',line_stack.peek())

if __name__ == '__main__':
    test_01()


