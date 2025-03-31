"""Exercise 1"""

class Node():
    """Represents a node"""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def parse(string: str):
    """
    Parse a string representation of a singly linked list into an actual linked list.

    The input string has the format: "value1 -> value2 -> ... -> null",
    where each value is a non-negative integer and "null" marks the end of the list.

    Parameters:
        string (str): A string representing a singly linked list.

    Returns:
        Node | None: The head of the linked list corresponding to the input string.
                     Returns None if the string is just "null".

    Examples:
        >>> def print_linked_list(node):
        ...     result = []
        ...     while node:
        ...         result.append(str(node.data))
        ...         node = node.next
        ...     result.append("null")
        ...     return " -> ".join(result)

        >>> print_linked_list(parse("1 -> 2 -> 3 -> null"))
        '1 -> 2 -> 3 -> null'

        >>> print_linked_list(parse("7 -> null"))
        '7 -> null'

        >>> print_linked_list(parse("null"))
        'null'
    """

    if string.strip() is None:
        return None

    parts = string.split(" -> ")
    parts = parts[:-1]

    head = None
    for value in reversed(parts):
        head = Node(int(value), head)

    return head

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
