# BrainMaven-Assessment
`Task`: Writing a code to implement a **"Least-Recently Used" (LRU) Cache**. 


`Problem definition`: A Least Recently Used (LRU) Cache organized items in *order of use*, allowing you to quickly identify which item hasn't been used for the longest amount of tiem. The LRU gets the least recent used item in **O(1)** and also access items in **O(1)**. It also takes up **O(n) space**.


`Implementation`: Using `OrderedDict()` from *collections* library in `Python 3.7`, to keep track of the head and tail of our items. Initiating the cache item by asking the capacity from user and setting it to our cache size. The class LRUCache will create an interface of the cache and the two functions `get()` and `set()` will each the item if it's already in the cache and also add new items if they are not in the cache as well as updating the cache when the maximum capacity has been reached.
