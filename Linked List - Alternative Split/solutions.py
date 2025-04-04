"""Exercise 10"""

class Node(object):
    """
    A class representing a node in a singly linked list.

    Attributes:
    data: The value stored in the node (default is None).
    next: A pointer to the next node in the list (default is None).
    """
    def __init__(self, data=None):
        """
        Initializes a new node with the given data and next pointer.

        Args:
        data (int or any): The value to store in the node (default is None).
        next (Node or None): The next node in the list (default is None).
        """
        self.data = data
        self.next = None


class Context(object):
    """
    A class to store the two split linked lists.

    Attributes:
    first: The first linked list after the alternating split.
    second: The second linked list after the alternating split.
    """
    def __init__(self, first, second):
        """
        Initializes the context with the two linked lists.

        Args:
        first (Node): The first linked list.
        second (Node): The second linked list.
        """
        self.first = first
        self.second = second


def alternating_split(head):
    """
    Splits a linked list into two sublists based on alternating nodes.

    The first sublist contains nodes from the odd positions (1st, 3rd, 5th, etc.),
    and the second sublist contains nodes from the even positions (2nd, 4th, 6th, etc.).

    Args:
    head (Node or None): The head of the input linked list.

    Returns:
    Context: A context object containing the two split linked lists.

    Raises:
    ValueError: If the input list is empty or contains a single node.

    Example:
    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node3 = Node(3)
    >>> node4 = Node(4)
    >>> node5 = Node(5)
    >>> node1.next = node2
    >>> node2.next = node3
    >>> node3.next = node4
    >>> node4.next = node5
    >>> context = alternating_split(node1)
    >>> alternating_split(None)
    Traceback (most recent call last):
        ...
    ValueError
    >>> node1 = Node(1)
    >>> alternating_split(node1)
    Traceback (most recent call last):
        ...
    ValueError
    """

    if not head or not head.next:
        raise ValueError()

    first_head = Node()
    second_head = Node()

    first = first_head
    second = second_head

    current = head
    index = 1
    
    while current:
        if index % 2 != 0:
            first.next = current
            first = first.next
        else:
            second.next = current
            second = second.next
        
        current = current.next
        index += 1

    first.next = None
    second.next = None

    return Context(first_head.next, second_head.next)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
