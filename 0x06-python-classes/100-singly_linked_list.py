#!/usr/bin/python3
class Node:
    """Defines a node of a singly linked list.
    Attributes:
        data (int): the data of node.
        next_node: the next node.
    """
    def __init__(self, data, next_node=None):
        """Initializes new node and data.
        Args:
            data (int): the data of new_node.
            next_node: the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the value of data
        Args:
            value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """Gets the next node of the node"""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a node object")
        self.__next_node = value
class SinglyLinkedList:
    """Represensts a singly linked list."""
    def __init__(self):
        """Initializes a linked list."""
        self.__head = None
    def sorted_insert(self, value):
        """Insert a new node to singly linked list.
        Args:
            value (Node): The new node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node
    def __str__(self):
        """Defines the printd rep of a single linked list."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
