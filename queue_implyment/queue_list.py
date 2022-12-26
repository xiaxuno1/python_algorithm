# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: queue_list
# Author: xiaxu
# DATA: 2022/12/26
# Description:使用py的list实现queue结构
# ---------------------------------------------------
"""
普通的队列结构每次移动出去一个，所有成员的位置都会变化
"""
from typing import Any


class ListQueue:
    """队列的线性表表示"""
    def __init__(self,length:int=10)->None:
        self.length = length  #定义列表的长度
        self.front = 0  #对首位置
        self.data = []

    def __str__(self):
        return "<"+str(self.data)+">"

    def put(self,data:Any):
        """定义入队"""
        if len(self.data)<self.length:
            self.data.append(data)
            self.length = self.length+1
        else:
            raise IndexError("out of length")

    def get(self):
        """出队的操作；出队后所有位置都会移动"""
        if self.length == 0:
            raise IndexError("the queue_implyment is enpty")
        dequeue = self.data[self.front] #存储出队元素，后面赋值后对列会改变
        self.length = self.length-1
        self.front = self.front-1
        self.data = self.data[1:]
        return dequeue


#以下为测试文本
if __name__ == '__main__':
    list_queue = ListQueue()
    print(str(list_queue))
    #数据入队
    for i in range(10):
        list_queue.put(i+1)
    print(str(list_queue))
    list_queue.get()
    print(str(list_queue))