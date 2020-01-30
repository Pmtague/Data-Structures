import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stacks are LIFO
class Stack:
    def __init__(self):

        # Declare stack props
        self.size = 0

        # Why is our DLL a good choice to store our elements? 
        self.storage = DoublyLinkedList()

    # Add a node to the top of the stack (the head)
    def push(self, value):

        # Increment stack size
        self.size += 1

        # Create the new node and add it to the top
        self.storage.add_to_head(value)

    # Remove a node from the top of the stack (the head)
    def pop(self):

        # If the stack is not empty, store the value from the current node, delete the node, and return the value
        if self.len() > 0:

            # Store the value of the node we want to delete and delete it
            value = self.storage.remove_from_head()

            # Decrement the stack size
            self.size -= 1

            # Return the deleted node's value
            return value
		
        # If stack is empty, return none
        else:
            return None
    
    # Return the size of the stack
    def len(self):
        return self.size
