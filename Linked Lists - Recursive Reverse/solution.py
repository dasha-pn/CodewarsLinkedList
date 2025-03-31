"""Exercise 7"""

class Node(object):
    """Represents a Node"""

    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    """
    Recursively reverses a singly linked list.

    :param head: Head of the linked list to reverse.
    :return: New head of the reversed linked list.

    >>> a = Node(2)
    >>> b = Node(1)
    >>> c = Node(3)
    >>> d = Node(6)
    >>> e = Node(5)
    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e
    >>> new_head = reverse(a)
    >>> print(new_head)
    5 -> 6 -> 3 -> 1 -> 2 -> None

    >>> print(reverse(None))
    None
    """

    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
