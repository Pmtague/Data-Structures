import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # Declare cache properties
    def __init__(self, limit=10):
        # Max number of nodes in cache
        self.limit = limit
        # Current amount of nodes in cache
        self.length = 0
        # Initialize empty cache
        self.cache = {}
        # Bring in functionality from DoublyLinkedList class
        self.storage = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Check if the requested key is already in the cache
        if key in self.cache:
            node = self.cache[key]
            # Move node with requested key to the beginning of the cache (most recently used)
            self.storage.move_to_front(node)
            # Return the requested value
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # node and self.order.tail are essentially the same, addresses to the same node
    def set(self, key, value):

        # If the key is already in the cache
        if key in self.cache:
            # Declare the node as cache[key]
            node = self.cache[key]
            # Destructure the node value
            node.value = (key, value)
            # Move the new node to the front (MRU)
            self.storage.move_to_front(node)
            return

        if self.length == self.limit:
            # Delete the LRU item from the dictionary
            del self.cache[self.storage.tail.value[0]]
			# Remove the tail node
            self.storage.remove_from_tail()
			# Decrease the length by 1
            self.length -= 1

        # Add the new value to the head
        self.storage.add_to_head((key, value))
		# Add the new key, value pair to the dictionary
        self.cache[key] = self.storage.head
		# Increase the length by 1
        self.length += 1