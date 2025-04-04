"""Exercise 9"""

class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
    data: The value stored in the node (default is None).
    next: A pointer to the next node in the list (default is None).
    """
    def __init__(self, data=None, next=None):
        """
        Initializes a new node with the given data and next pointer.

        Args:
        data (int or any): The value to store in the node (default is None).
        next (Node or None): The next node in the list (default is None).
        """
        self.data = data
        self.next = next


def swap_pairs(head):
    """
    Swaps every two adjacent nodes in a singly linked list.

    This function takes the head of a sorted singly linked list and swaps
    adjacent pairs of nodes. If the list has an odd length, the last node
    remains in place.

    Args:
    head (Node or None): The head node of the singly linked list. If the list
                          is empty (None), the function returns None.

    Returns:
    Node: The head node of the modified linked list with pairs of nodes swapped.

    Example:
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node3 = Node(3)
    >>> node4 = Node(4)
    >>> node1.next = node2
    >>> node2.next = node3
    >>> node3.next = node4
    >>> new_head = swap_pairs(node1)
    >>> swap_pairs(None)
    >>> None
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node1.next = node2
    >>> new_head = swap_pairs(node1)
    """
    if not head or not head.next:
        return head

    temp = Node()
    temp.next = head
    prev = temp

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return temp.next

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
