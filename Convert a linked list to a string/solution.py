"""Exercise 1"""

class Node():
    """
    Represents a node in a singly linked list.

    Attributes:
        data: The value stored in the node.
        next: A reference to the next node in the list (or None if it's the last node).
    """

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node'):
    """

    Convert a linked list starting at 'node' into a string representation.

    The format is: "data1 -> data2 -> ... -> None"

    Args:
        node (Node): The starting node of the linked list.

    Returns:
        str: The string representation of the list.

    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    '0 -> 1 -> 4 -> 9 -> 16 -> None'
    """

    res = ""

    if not isinstance(node, Node):
        return 'None'

    while node.next:
        res += str(node.data) + ' -> '
        node = node.next

    res += str(node.data) + ' -> '

    return res + 'None'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
