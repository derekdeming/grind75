
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(list(self.cache.keys())[0])
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
implements a Least Recently Used (LRU) cache. The LRU cache is a type of cache in which the least recently used entries are removed when the cache reaches its capacity


The get method retrieves the value of a key if the key exists in the cache. If the key is not in the cache, it returns -1. After accessing the key, it moves the key to the end of the cache to mark it as recently used.

The put method inserts or updates the value of a key. If the key is already in the cache, it updates the key's value and moves the key to the end of the cache. If the key is not in the cache, it inserts the key-value pair into the cache. If the cache is at capacity, it removes the least recently used item before inserting the new key-value pair.
'''


