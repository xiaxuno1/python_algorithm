# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: single_linked_list
# Author: xiaxu
# DATA: 2022/12/14
# Description:单链表的实现
# ---------------------------------------------------
"""
ADT 单链表list
Data
	data
	next
Opration
	ListInsert(*L,i,e):在L的第i个元素位置插入e
	ListDelete(*L,i,*e):在L的第i个元素位置删除，并用e返回
	ListLength(L)   :返回线性表L的元素个数
	print_list(): 打印功能
	is_empty: 判断是否为空，返回bool
endADT
"""
from typing import Any
import unittest


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


class SingleLinkedList:
    """
    单链表对象
    """
    def __init__(self):
        """
        初始化结点对象
        """
        self.head = None

    def __iter__(self)->Any:
        """
        迭代器，遍 历单链表的数据
        """
        node = self.head  #起始位置
        while node:
            yield node.data
            node = node.next

    def __len__(self)->int:
        """此魔法方法实现了求单链表的长度，len()方法自动调用"""
        return len(tuple(iter(self)))

    def __repr__(self):
        """链表字符串可视化，类似于1->3->6,当str()方法自动调用"""
        return "->".join([str(item) for item in self])

    def __getitem__(self, index:int)->Any:
        """对于索引的支持，用来获取指定位置的一个结点"""
        if not 0<=index<=len(self):
            raise IndexError("index out of range!")
        for i,node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index:int, data:Any)->None:
        """改变指定位置结点的值"""
        if not 0<=index<=len(self):
            raise IndexError("index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_node(self,index:int,data:Any):
        """根据索引插入结点"""
        #判断索引是否超出范围,超出范围报错
        if not 0<=index<=len(self):
            raise IndexError("index out of range!")
        #如果为插入的链表为空，直接插入不改变
        new_node = Node(data) #创建一个新的结点
        if self.head ==None:  #相当于初始化
            self.head = new_node
        elif index == 0:
            #在头插入
            new_node.next = self.head
            self.head = new_node #head的位置移动到新结点
        else:
            temp = self.head #从头开始
            for _ in range(index-1):#一个一个查询链表的next知道index位置
                temp = temp.next
            new_node.next = temp.next  #新结点指向插入位置下一结点
            temp.next = new_node  #上结点指向新结点

    def insert_head(self,data:Any)->None:
        """从头插入"""
        self.insert_node(0,data)

    def insert_tail(self,data:Any)->None:
        """插入尾部"""
        self.insert_node(len(self),data)

    def delete_node(self,index:int=0)->Any:
        """删除指定索引位置的结点"""
        #检查index是否超限
        if not 0<=index<=len(self)-1:
            raise IndexError('index out of range!')
        #删除头时head也要移动
        delete_node = self.head  #要删除结点
        if index == 0:
            self.head = self.head.next  #将head位置下移，不用删除结点python有回收机制
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next #不断往下
            delete_node = temp.next #删除的结点
            temp.next = temp.next.next  #指向下下个
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
        return self.head is None

    def reverse(self)->None:
        """翻转链表"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev  #将head的位置移动到尾







    




