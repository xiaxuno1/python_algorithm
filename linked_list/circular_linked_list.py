# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: circular_linked_list
# Author: xiaxu
# DATA: 2022/12/20
# Description:循环单列表
# ---------------------------------------------------
from typing import Any
from collections.abc import Iterator


class Node:
    """
    结点的定义
    """
    def __init__(self,data: Any): #Any 包容所有的类型
        self.data = data
        self.next = None

    def __repr__(self) ->str:
        """
        获取字符串表示，可以在命令行执行的表示
        :return:
        """
        return f"Node({self.data})"


class CircularSingleLinkedList:
    """
    单链表对象
    """
    def __init__(self):
        """
        初始化结点对象
        """
        self.head = None
        self.tail = None #尾指针

    def __iter__(self)->Iterator[Any]:
        """
        迭代器，遍 历单链表的数据
        """
        node = self.head  #起始位置
        while self.head:
            yield node.data
            node = node.next
            #终端结点指向头结点
            if node == self.head:
                break

    def __len__(self)->int:
        """此魔法方法实现了求单链表的长度，len()方法自动调用"""
        return len(tuple(iter(self)))

    def __repr__(self):
        """链表字符串可视化，类似于1->3->6,当str()方法自动调用"""
        return "->".join([str(item) for item in self])

    def __getitem__(self, index:int)->Any:
        """对于索引的支持，用来获取指定位置的一个结点"""
        if index <0 or index>len(self):
            raise IndexError("index out of range!")
        for i,node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index:int, data:Any)->None:
        """改变指定位置结点的值"""
        if index <0 or index>len(self):
            raise IndexError("index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_node(self,index:int,data:Any):
        """根据索引插入结点"""
        #判断索引是否超出范围,超出范围报错
        if index <0 or index>len(self):
            raise IndexError("index out of range!")
        #如果为插入的链表为空，直接插入不改变
        new_node = Node(data) #创建一个新的结点
        if self.head ==None:  #相当于初始化
            new_node.next = new_node #第一个结点指向自己
            self.tail=self.head = new_node #头结点和尾结点都在第一个结点
        elif index == 0:
            #在头插入
            new_node.next = self.head #1 新结点的指针指向头结点
            self.tail.next = new_node #2 将尾结点指向新结点
            self.head = new_node #3 head的位置移动到新结点
        else:
            temp = self.head #从头开始
            for _ in range(index-1):#一个一个查询链表的next知道index位置
                temp = temp.next
            new_node.next = temp.next  #新结点指向插入位置下一结点
            temp.next = new_node  #上结点指向新结点
            #如果index为tail，应该将tail位置更新
            if index == len(self)-1:
                self.tail = temp.next

    def insert_head(self,data:Any)->None:
        """从头插入"""
        self.insert_node(0,data)

    def insert_tail(self,data:Any)->None:
        """插入尾部"""
        self.insert_node(len(self),data)

    def delete_node(self,index:int=0)->Any:
        """删除指定索引位置的结点"""
        #检查index是否超限
        if  0>index or index>len(self)-1:
            raise IndexError('index out of range!')
        #删除头时head也要移动
        delete_node = self.head  #要删除结点
        if self.head == self.tail:  #仅一个结点
            self.tail = self.head = None
        elif index == 0:
            self.tail.next = self.head.next  #1 将尾结点的指针指向头结点后面的结点
            self.head = self.head.next  #2.将head位置下移，不用删除结点python有回收机制

        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next #不断往下
            delete_node = temp.next #删除的结点
            temp.next = temp.next.next  #指向下下个
            #如果删除的是尾结点，将指针移动
            if index == len(self)-1:
                self.tail = temp  #尾指针移动到上个结点
        return delete_node.data

    def delete_head(self):
        """删除头"""
        return self.delete_node(0)

    def delete_tail(self):
        """删除尾"""
        return self.delete_node(len(self)-1)  #索引从0开始

    def print_list(self)->None:
        print(self)

    def is_empty(self)->bool:
        return len(self) == 0

#以下为测试程序
def test_01():
    """"""
    c_list = CircularSingleLinkedList()
    #测试is_empty功能
    assert c_list.is_empty() is True
    print("空链表",str(c_list))
    #测试插入数据
    for i in range(10):
        c_list.insert_node(i,i+1)
    #断言插入的数据的字符表达正确
    print("插入数据",str(c_list))
    assert str(c_list) == "->".join(str(i)  for i in range(1,11))
    #测试魔法方法__iter__
    assert len(c_list) == 10
    #测试插入头结点
    c_list.insert_head(66)
    print("插入头结点",str(c_list))
    assert c_list[0] == 66
    #测试插入尾结点
    c_list.insert_tail(77)
    print("插入尾结点",str(c_list))
    assert c_list[len(c_list)-1] == 77
    #测试删除头结点
    c_list.delete_head()
    print("删除头结点",str(c_list))
    assert c_list[0] == 1
    c_list.delete_tail()
    print("删除尾结点",str(c_list))
    assert c_list[len(c_list)-1] == 10
    c_list.delete_node(4)
    print("删除结点",str(c_list))
    assert c_list[4] == 6

if __name__ == '__main__':
    test_01()
