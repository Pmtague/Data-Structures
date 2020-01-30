"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    # Defines the properties of objects of the ListNode class
    # Self is akin to this in JS
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        # Store next pointer of node we are inserting after in a variable
        current_next = self.next
        # Set next equal to a list node obj, passing in the new value and attaching the old self.next to it
        self.next = ListNode(value, self, current_next)
        # TODO Not sure I understand how this part is working, but I think it is supposed to create a previous pointer for the new node 
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    # Define properties of list and their default values
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    # Giving others easy access to the length property
    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # Create a new node
        new_node = ListNode(value, None, None)
        # Increment the length of the list to account for the new node
        self.length += 1
        # If the list is empty, the new node is both the head and the tail in DLL
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Otherwise, assign the new node's next pointer to the old head, change the old head's prev pointer from null to the new node, and assign the head as to the new node
        else:
			# Assign new node's next pointer to the current head
            new_node.next = self.head
			# Assign the current head's previous pointer to the new node
            self.head.prev = new_node
			# Declare the new node as the head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # Store the value before removing the head
        value = self.head.value
        # Delete the current head
        self.delete(self.head)
        # Return the value previously stored in the deleted head
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # Create a new node
        new_node = ListNode(value, None, None)
        # Add to the length of the list
        self.length += 1
        # If the list was empty, assign the head and the tail to the new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Otherwise, assign the new node's previous pointer to the old tail, point the old tail's next pointer to the new node, assign the tail label to the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Store the value of the tail in a variable
        value = self.tail.value
        # Delete the tail
        self.delete(self.tail)
        # Return the value that was stored in the deleted tail
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # Store the value of the node being moved
        value = node.value
        # Delete the node being moved
        self.delete(node)
        # Use the add to head method to add to create a new node and store the value of the deleted node
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Store the value of the node being moved
        value = node.value
        # Delete the node being moved
        self.delete(node)
        # Create a new node with the old value at the new location
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # If LL is empty
        if not self.head and not self.tail:
            print("The list is empty")
            return
        # Decrement the length of the list
        self.length -= 1
        # If the node is the head and tail, only one item in the list
        if self.head == self.tail:
            # Remove the pointers and get on with your life
            self.head = None
            self.tail = None
        # If the node is the head
        elif self.head is node:
            # Set the former next as the current head
            self.head = node.next
            # Delete the node
            node.delete()
        # If the node is the tail
        elif self.tail is node:
            # Set the former prev as the current tail
            self.tail = node.prev
            # Delete the node
            node.delete()
        # Otherwise
        else:
            node.delete()
    """Returns the highest value currently in the list"""
    def get_max(self):
        # If there is a head
        if self.head == None:
            return None
        # Set a variable for max value and set it equal to the value of the head
        max_value = self.head.value
        # Set a variable for the current node being evaluated and set it equal to the head to start there
        current = self.head
        # While current is a node
        while current:
            # If the value of current is greater than the currently stored max_value, replace the max value with the value of current
            if current.value > max_value:
                max_value = current.value
            # Set current to the next node for comparison
            current = current.next
        # Return the max value
        return max_value
