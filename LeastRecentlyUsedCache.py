import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        #Using OrderedDict to work as a Doubly LinkedList to track the head and tail
        self.cache = collections.OrderedDict()
    

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
    
    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        
        self.cache[key] = value



#Asking for user input for size of cache and number of items
size = int(input())
n = int(input())

cache1 = LRUCache(size)
for i in range(n):
    cache1.set(i,i)
    print(cache1.cache)
