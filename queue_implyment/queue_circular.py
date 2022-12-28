# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: queue_circular
# Author: xiaxu
# DATA: 2022/12/26
# Description:循环队列的线性表实现
# ---------------------------------------------------
from typing import Any


class CirculreQueue:
    """循环线性队列"""
    def __init__(self,size:int = 10)->None:
        self.front = 0  #指向对首元素
        self.rear = 0  #指向对尾元素的下一个
        self.size = size #线性表的长度
        self.data = [None]*self.size #线性表的定义,先赋值为None，否则入队时无法赋值

    def __len__(self):
        return (self.rear-self.front+self.size)%self.size #长度的计算公式

    def __repr__(self):
        return "->".join([str(i) for i in self.data])

    def enqueue(self,data:Any)->None:
        if (self.rear+1)%self.size == self.front: #判断是否满了,rear和front之间留一个
            raise Exception('The Queue is full')
        self.data[self.rear] = data  #因为会回到头，所以使用赋值
        self.rear = (self.rear+1)%self.size #rear指针指向后一位置，如果到线性表的尾部，则从头开始

    def dequeue(self)->Any:
        """定义出队列"""
        if self.front == self.rear: #队列为空
            return "The Queue is enpty"
        dequeue_data = self.data[self.front]
        self.data[self.front] = None #删除的位置数据为空
        self.front = (self.front+1)%self.size  #front的位置循环移动到下一个位置
        return dequeue_data


if __name__ == '__main__':
    circular_queue = CirculreQueue()
    #数据入队,满队
    for i in range(9):
        circular_queue.enqueue(i)
    print(circular_queue)
    #出队
    circular_queue.dequeue()
    print(circular_queue)
    #循环插入
    circular_queue.enqueue(99)
    print(circular_queue)
    circular_queue.dequeue()
    print(circular_queue)
    #从对首插入
    circular_queue.enqueue(66)
    print(circular_queue)
