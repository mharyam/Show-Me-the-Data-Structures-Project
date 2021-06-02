class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.num_element = 0
        self.capacity = 5

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

    # def delete(self, key):
    #     self.arr.pop(key)
    #     self.num_element -= 1
    #
    # def get_arr_index(self, key):
    #     return self.get_hash_code(key)

    # def get_hash_code(self, key):
    #     #key = str(key)
    #     num_buckets = len(self.bucket_array)
    #
    #     # represents (self.p^0) which is 1
    #     current_coefficient = 1
    #     hash_code = 0
    #
    #     for character in key:
    #         hash_code += ord(character) * current_coefficient
    #         hash_code = hash_code % num_buckets  # compress hash_code (return hash_code % num_buckets   Mod operation)
    #         current_coefficient *= self.p
    #         current_coefficient = current_coefficient % num_buckets  # compress coefficient as well
    #
    #     return hash_code % num_buckets

    def __str__(self):
        return f"{self.cache}"


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

print(our_cache)