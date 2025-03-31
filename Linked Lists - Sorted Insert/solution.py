"""Exercise 6"""

class Node(object):
    def __init__(self, data):
        """
        Creates a new node for a singly linked list.

        :param data: The value to store in the node.
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Returns a string representation of the linked list starting from this node.

        >>> a = Node(1)
        >>> b = Node(3)
        >>> a.next = b
        >>> print(a)
        1 -> 3 -> None
        """
        nodes = []
        current = self
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"


def sorted_insert(head, data):
    """
    Inserts a new node with the given `data` into a sorted singly linked list (ascending order).

    :param head: The head node of the sorted linked list (or None if the list is empty).
    :param data: The value to insert into the list.
    :return: The head of the updated linked list with the new node inserted in the correct position.

    Doctests:
    >>> a = Node(1)
    >>> b = Node(2)
    >>> c = Node(4)
    >>> a.next = b
    >>> b.next = c
    >>> new_head = sorted_insert(a, 3)
    >>> print(new_head)
    1 -> 2 -> 3 -> 4 -> None

    >>> new_head = sorted_insert(new_head, 0)
    >>> print(new_head)
    0 -> 1 -> 2 -> 3 -> 4 -> None

    >>> new_head = sorted_insert(new_head, 5)
    >>> print(new_head)
    0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

    >>> empty_head = None
    >>> new_head = sorted_insert(empty_head, 10)
    >>> print(new_head)
    10 -> None
    """
    new_node = Node(data)

    if not head or data < head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
