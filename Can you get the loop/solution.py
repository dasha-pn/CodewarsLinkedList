"""Exercise 11"""

class Node:
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

def loop_size(head):
    """
    Detects the size of the loop in a linked list.

    This function uses Floyd’s Tortoise and Hare algorithm to detect a loop and calculate its size.

    Args:
    head (Node or None): The head of the input linked list.

    Returns:
    int: The size of the loop, or 0 if there is no loop.

    Raises:
    ValueError: If the list has no loop and is not cyclic.

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
    >>> node5.next = node2
    >>> loop_size(node1)
    4

    >>> node1 = Node(1)
    >>> node2 = Node(2)
    >>> node1.next = node2
    >>> loop_size(node1)
    0
    """
    if not head or not head.next:
        return 0

    tortoise = head
    hare = head
    
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        
        if tortoise == hare:
            loop_size = 1
            loop_node = tortoise.next
            while loop_node != tortoise:
                loop_size += 1
                loop_node = loop_node.next
            return loop_size

    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
