"""Exercise 5"""

class Node(object):
    """
    Represents a single node in a singly linked list.

    Attributes:
        data (any): The value stored in the node.
        next (Node or None): The reference to the next node in the list.

    Example:
        >>> node = Node(5)
        >>> node.data
        5
        >>> node.next is None
        True
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    """
    A helper class that holds the state of two linked lists: source and destination.

    Attributes:
        source (Node or None): Head of the source linked list.
        dest (Node or None): Head of the destination linked list.

    Example:
        >>> a = Node(1)
        >>> b = Node(2)
        >>> ctx = Context(a, b)
        >>> ctx.source.data
        1
        >>> ctx.dest.data
        2
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    """
    Moves the first node from the front of the source list to the front of the destination list.

    Args:
        source (Node): The head of the source linked list (must not be None).
        dest (Node): The head of the destination linked list.

    Returns:
        Context: A Context object containing the updated source and dest lists.

    Raises:
        ValueError: If the source list is empty (i.e., source is None).

    Example:
        >>> src = Node(1)
        >>> src.next = Node(2)
        >>> dst = Node(4)
        >>> dst.next = Node(5)
        >>> result = move_node(src, dst)
        >>> result.source.data
        2
        >>> result.dest.data
        1
        >>> result.dest.next.data
        4
    """
    if source is None:
        raise ValueError("The list is empty")
    new_source = source.next
    source.next = dest
    new_dest = source
    return Context(new_source, new_dest)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
