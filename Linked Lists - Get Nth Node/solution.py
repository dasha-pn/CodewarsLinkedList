"""Exercise 4"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Returns the node at the given index in a singly linked list.

    Indexing starts from 0 (C-style). If the index is out of bounds or the list is empty,
    raises an IndexError.

    Args:
        node (Node): The head node of the linked list.
        index (int): The zero-based position of the node to retrieve.

    Returns:
        Node: The node at the specified index.

    Raises:
        IndexError: If the index is negative, the list is empty, or the index is out of bounds.

    Examples:
        >>> n = Node(1, Node(2, Node(3)))
        >>> get_nth(n, 0).data
        1
        >>> get_nth(n, 1).data
        2
        >>> get_nth(n, 2).data
        3
        >>> get_nth(n, 3)
        Traceback (most recent call last):
        ...
        IndexError: Index out of bounds
        >>> get_nth(None, 0)
        Traceback (most recent call last):
        ...
        IndexError: Index out of bounds
    """

    if node is None:
        raise IndexError("Index out of bounds")

    counter = 0

    while node:
        if counter == index:
            return node
        counter += 1
        node = node.next

    raise IndexError("Index out of bounds")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
