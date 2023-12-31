#!/usr/bin/python3
"""A class node that defines a node of
singly linked list
"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """Initialize the list with given parameters"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method that inserts
        new node into the correct sorted position
        It takes a parameter `value`, which is the data for
        the new node

        It creates a new `Node` instance called `new_node`
        with the given value`.

        1. Insertion at the beginning:
        -   If the linked list is empty(`self.__head is None)
            or if the new node's value is less than the value
            of the current node, then the new node becomes the new head.

        -   The new_node.next_node is set to the current head,
            and `self.__head` is updated to `new_node`.

        2. Insertion in the Middle or at the End
        - If the new node's value is greater than or equal to the current
        head node's value, it iterates through the linked list to find
        the correct position.

        - The loop continues until it finds a node whose next node has a
        greater value or until it reaches the end of the list

        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout
        - one node number by line
        - It starts at the head of the linked list
            (current = self.__head)
            and iterates through each node, printing its data

        - The loop continues until it reaches the end of the
        list(when `current` becomes `None`)
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
