class LinkedListNode():
    """Node for the LinkedList class."""

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    """A standard linked list."""

    def __init__(self, headData):
        self.head = LinkedListNode(headData)

    def append(self, data):
        """append given node to the end of the Linked List.

        Parameters:
            data (varies): The node to append to the Linked List.

        Returns:
            None
        """

        current = self.head

        #go to the last node
        while current.next != None:
            current = current.next

        #make last link node point to given node
        current.next = LinkedListNode(data)

    def get(self, index):
        """Gets the node stored in the linked list at index

        Parameters:
            index (int): The index of the linked list element.

        Returns:
            (varies) : the node stored at that particular node.
        """
        current = self.head
        for i in range(index):
            current = current.next

        return current.data


