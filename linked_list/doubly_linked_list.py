# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: doubly_linked_list
# Author: xiaxu
# DATA: 2022/12/20
# Description:双链表
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
        self.prior = None #前置指针

    def __repr__(self) ->str:
        """
        获取字符串表示，可以在命令行执行的表示
        :return:
        """
        return f"Node({self.data})"


class DoublyLinkedList:
    """
    双向链表对象
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
            new_node.prior=new_node.next = new_node #第一个结点前驱和后继都指向自己
            self.tail=self.head = new_node #头结点和尾结点都在第一个结点
        elif index == 0:
            #在头插入
            self.head.prior = new_node #1 head的前驱指向新结点
            new_node.next = self.head #2 将新结点的next指向头结点
            new_node.prior = self.tail # 3 新的头结点的前驱指向尾结点
            self.head = new_node #4 head的位置移动到新结点
            self.tail.next = self.head #5 将tail的next指向新头结点
        elif index == len(self):
            #在尾结点插入
            self.tail.next = new_node  # 插入位置上个结点next指向新结点
            #新结点前驱结点指向上个结点
            new_node.prior = self.tail
            #新结点next指向头结点
            new_node.next = self.head
            #尾指针位置移动
            self.tail = new_node
            #头结点的前驱指向尾结点
            self.head.prior = self.tail
        else:
            temp = self.head #从头开始
            for _ in range(index):#一个一个查询链表的next知道index位置
                temp = temp.next
            temp.prior.next = new_node  #1 前结点指向新结点
            new_node.next=temp  # 2.新结点next指向插入位置的下个结点
            # 4.新结点的前驱指针指向插入位置的上个结点
            new_node.prior = temp.prior
            # 3.插入位置下个结点的前驱指针指向新结点
            temp.prior = new_node

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
            #将新头结点的前驱指向尾结点
            self.head.next.prior = self.tail
            #将尾结点的next指针指向新的头结点
            self.tail.next = self.head.next
            self.head=self.head.next  #1 将头结点后移
        elif index ==len(self)-1:
            #删除尾结点
            delete_node = self.tail
            #尾结点指针上移
            self.tail = self.tail.prior
            self.tail.next = self.head  #新的尾结点的next指向头结点
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next #不断往下
            delete_node = temp.next #删除的结点
            #删除位置的下个结点的prior指向上上个结点
            temp.next.prior = temp.prior
            #删除位置上个结点的next指向下下个结点
            temp.prior.next = temp.next
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
    doubly_list = DoublyLinkedList()
    #测试is_empty功能
    assert doubly_list.is_empty() is True
    print("空链表",str(doubly_list))
    #测试插入数据
    for i in range(10):
        doubly_list.insert_node(i,i+1)
    #断言插入的数据的字符表达正确
    print("插入数据",str(doubly_list))
    assert str(doubly_list) == "->".join(str(i)  for i in range(1,11))
    #测试魔法方法__iter__
    assert len(doubly_list) == 10
    #测试插入头结点
    doubly_list.insert_head(66)
    print("插入头结点",str(doubly_list))
    assert doubly_list[0] == 66
    #测试插入尾结点
    doubly_list.insert_tail(77)
    print("插入尾结点",str(doubly_list))
    assert doubly_list[len(doubly_list)-1] == 77
    #测试删除头结点
    doubly_list.delete_head()
    print("删除头结点",str(doubly_list))
    assert doubly_list[0] == 1
    doubly_list.delete_tail()
    print("删除尾结点",str(doubly_list))
    assert doubly_list[len(doubly_list)-1] == 10
    doubly_list.delete_node(4)
    print("删除结点",str(doubly_list))
    assert doubly_list[4] == 6
    #测试中间插入数据
    doubly_list.insert_node(5,33.33)
    print("中间插入结点",str(doubly_list))
    assert doubly_list[5] == 33.33

if __name__ == '__main__':
    test_01()

