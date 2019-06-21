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
            if current != None:
                current = current.next
            else:
                raise IndexError

        return current.data

    def __len__(self):
        """Get number of elements in linked list.
        Parameters:
            None.

        Returns:
            (int) : number of elements in linked list.
        """
        count = 1
        current = self.head
        while current.next != None:
            count += 1
            current = current.next

        return count

    def insert(self, index, data):
        """inserts the given data into the linked list at the given index.

        Parameters:
            index (int) : location to insert the data at.
            data (ind) : the data to be inserted.
        """
        newElement = LinkedListNode(data)

        #if inserting element at head of list
        if index == 0:
            newElement.next = self.head
            self.head = newElement
            return

        #otherwise traverse list to desired node
        previous = None
        current = self.head
        for i in range(index):
            if current != None:
                previous = current
                current = current.next
            else:
                raise IndexError

        #insert new element into list
        newElement.next = current
        previous.next = newElement



    def delete(self, index):
        """removes the data at the given index from the linked list.

        Parameters:
            index (int) : location of the data that will be deleted.
        """
        pass