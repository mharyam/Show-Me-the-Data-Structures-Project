class LRU_Cache:

    def __init__(self, capacity):
        if capacity < 0:
            return None
        # Initialize class variables
        self.cache = {}
        self.num_element = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = self.cache.get(key)
        if value:
            return value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity > len(self.cache):
            self.cache[key] = value
        else:
            key_to_remove = list(self.cache.keys())[0]
            del(self.cache[key_to_remove])
            self.cache[key] = value

    def __str__(self):
        try:
            return f"{self.cache}"
        except:
            return ""


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

(our_cache.get(1))    # returns 1
(our_cache.get(2))      # returns 2
(our_cache.get(9))     # returns -1 because 9 is not present in the cache


our_cache.set(5, 5)
our_cache.set(6, 6)


def test_function1():
    if (our_cache.get(1)) == -1:
        print("PASS")
    else:
        print("FAIL")


def test_function2():
    if (our_cache.get(9)) == -1:
        print("PASS")
    else:
        print("FAIL")


test_function1()
test_function2()

# second edge cas


def test_function3():
    second_cache = LRU_Cache(-1)
    if second_cache == "":
        print("PASS")
    else:
        print("FAIL")


test_function3()