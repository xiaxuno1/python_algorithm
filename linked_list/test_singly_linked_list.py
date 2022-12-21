# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: python_algorithm
# FN: test
# Author: xiaxu
# DATA: 2022/12/19
# Description:测试
# ---------------------------------------------------
from linked_list import single_linked_list
import unittest


#以下为测试程序
def test_singly_linked_list() -> None:
    """
    测试
    """
    linked_list = single_linked_list.SingleLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""
    try:
        linked_list.delete_head()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        raise AssertionError()  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_node(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_node(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))

    assert all(linked_list[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        linked_list[i] = -i  #由魔方函数_setitem_实现
    assert all(linked_list[i] == -i for i in range(0, 9)) is True

    linked_list.reverse()
    assert str(linked_list) == "->".join(str(i) for i in range(-8, 1))

def test_singly_linked_list_2() -> None:
    """
    测试单链表中数据输入类型
    """
    test_input = [
        -9,
        100,
        single_linked_list.Node(77345112),
        "dlrow olleH",
        7,
        5555,
        0,
        -192.55555,
        "Hello, world!",
        77.9,
        single_linked_list.Node(10),
        None,
        None,
        12.20,
    ]
    linked_list = single_linked_list.SingleLinkedList()

    for i in test_input:
        linked_list.insert_tail(i)

    # Check if it's empty or not
    assert linked_list.is_empty() is False
    assert (
        str(linked_list) == "-9->100->Node(77345112)->dlrow olleH->7->5555->0->"
        "-192.55555->Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the head
    result = linked_list.delete_head()
    assert result == -9
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the tail
    result = linked_list.delete_tail()
    assert result == 12.2
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None->None"
    )

    # Delete a node in specific location in linked list
    result = linked_list.delete_node(10)
    assert result is None
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None"
    )

    # Add a Node instance to its head
    linked_list.insert_head(single_linked_list.Node("Hello again, world!"))
    assert (
        str(linked_list)
        == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
        "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None"
    )

    # Add None to its tail
    linked_list.insert_tail(None)
    assert (
        str(linked_list)
        == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
        "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None->None"
    )

    # Reverse the linked list
    linked_list.reverse()
    assert (
        str(linked_list)
        == "None->None->Node(10)->77.9->Hello, world!->-192.55555->0->5555->"
        "7->dlrow olleH->Node(77345112)->100->Node(Hello again, world!)"
    )


def main():
    test_singly_linked_list()
    test_singly_linked_list_2()
    linked_list = single_linked_list.SingleLinkedList()
    linked_list.insert_head(input("Inserting 1st at head ").strip())
    linked_list.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting 1st at tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")


if __name__ == "__main__":
    main()