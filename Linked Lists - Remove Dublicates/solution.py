"""Exercise 8"""

class Node(object):
    """
    A class representing a node in a singly linked list.

    Attributes:
    data: The value stored in the node.
    next: A pointer to the next node in the list.
    """
    def __init__(self, data):
        """
        Initializes a new node with the given data.

        Args:
        data (int or any): The value to store in the node.
        """
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Removes duplicate values from a sorted singly linked list.

    This function assumes that the linked list is sorted in increasing order.
    It iterates through the list and removes any duplicate nodes.

    Args:
    head (Node or None): The head node of the singly linked list. If the list is empty (None),
                          the function returns None.

    Returns:
    Node: The head node of the modified linked list with duplicates removed.

    Example:
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node3 = Node(3)
    >>> node4 = Node(3)
    >>> node5 = Node(4)
    >>> node6 = Node(4)
    >>> node7 = Node(5)
    >>> node1.next = node2
    >>> node2.next = node3
    >>> node3.next = node4
    >>> node4.next = node5
    >>> node5.next = node6
    >>> node6.next = node7
    >>> new_head = remove_duplicates(node1)
    >>> remove_duplicates(None)
    >>> None
    """
    if head is None:
        return None

    current = head

    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
