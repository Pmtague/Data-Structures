import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, size, value, prev = None, next = None):
		# Declare class properties
        self.size = 0
        self.value = value
		self.prev = prev
		self.next = next


    def enqueue(self, value):
        

    def dequeue(self):
        pass

    def len(self):
        pass
