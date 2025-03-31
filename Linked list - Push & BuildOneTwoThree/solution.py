"""Exercise 2"""

class Node1:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node in the list (or None if it's the last node).
    """
    def __init__(self, data):
        """
        Initialize a new node with the given data.

        Args:
            data: The value to store in the node.
        """
        self.data = data
        self.next = None


def push(head, data):
    """
    Insert a new node containing the given data at the beginning of the list.

    Args:
        head: The current head of the list (can be None).
        data: The value to insert into the new node.

    Returns:
        Node1: The new head of the list.
    """
    new_node = Node1(data)
    new_node.next = head
    return new_node


def build_one_two_three():
    """
    Build and return a linked list with the elements 1 -> 2 -> 3 -> None.

    Returns:
        Node1: The head of the newly created linked list.
    """
    head = None
    for value in [3, 2, 1]:
        head = push(head, value)
    return head
