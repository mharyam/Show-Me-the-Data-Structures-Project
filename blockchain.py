import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.next = None
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha_signature = hashlib.sha256(data.encode()).hexdigest()
        return sha_signature


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,  timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, previous_hash=self.previous_hash())
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Block(timestamp, data, previous_hash=self.previous_hash())
        return

    def previous_hash(self):
        node = self.head
        if node is None:
            return 0
        while node.next:
            node = node.next
        return node.hash

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"DATA:{node.data}, Prev:{node.previous_hash}, HASH:{node.hash}, NEXT:{node.next}")
            node = node.next
        return "\n".join(nodes)


llist = LinkedList()
llist.append(datetime.now(), "MARYAM YSUUF")
llist.append(datetime.now(), "Rufai YSUUF")


def test_function1():
    node = llist.head
    if node.previous_hash == 0:
        print("PASS")
    else:
        print("FAIL")


def test_function2():
    node = llist.head
    while node is not None and node.next:
        if not node.next.previous_hash == node.hash:
            return "FAIL"
        node = node.next

    return "PASS"


test_function1()
print(test_function2())
