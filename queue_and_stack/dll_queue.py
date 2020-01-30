import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):

        # Declare class properties
        self.size = 0

        # Store the DoublyLinkedList class as a property
        self.storage = DoublyLinkedList()

    # Add a node to the back of the queue (the head)
    def enqueue(self, value):

        # Increment the size of the queue
        self.size += 1

        # Create a new node and add it to the head of the DLL (The end of the queue)
        self.storage.add_to_head(value)

    # Remove a node from the front of the queue(the tail)
    def dequeue(self):

        # If the queue is not empty, deincrement the size and remove the tail of the DLL (The beginning of the queue)
        if self.len() > 0:
            self.size -= 1
            value = self.storage.remove_from_tail()
            return value

        # If the queue is empty, return none
        else:
            return None
			
    # Return the size of the queue
    def len(self):
        return self.size
