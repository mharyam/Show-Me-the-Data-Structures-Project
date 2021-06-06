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


class BlockChain:
    def __init__(self):
        self.head = None
        self.num_of_element = 0

    def append(self,  timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, previous_hash=self.previous_hash())
            self.num_of_element += 1
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Block(timestamp, data, previous_hash=self.previous_hash())
        self.num_of_element += 1
        return

    def previous_hash(self):
        node = self.head
        if node is None:
            return 0
        while node.next:
            node = node.next
        return node.hash

    def remove_block(self, value):
        if self.head is None:
            return None

        if self.head.data == value:
            self.head = self.head.next
            self.num_of_element -= 1
            return

        node = self.head
        while node.next:
            if node.next.data == value:
                node.next = node.next.next
                self.num_of_element -= 1
                return
            node = node.next
        raise ValueError("Value not found in the list.")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"DATA:{node.data}, Prev:{node.previous_hash}, HASH:{node.hash}, NEXT:{node.next}")
            node = node.next
        return "\n".join(nodes)


llist = BlockChain()
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


(test_function1())
print(test_function2())


# second edge test case
b1 = BlockChain()
b1.append(datetime.now(), "First")
b1.append(datetime.now(), "Second")
b1.append(datetime.now(), "Third")


def test_block_chain(block_chain):
    if block_chain.num_of_element == 3:
        print("PASS")
    else:
        print("FAIL")


test_block_chain(b1)

# print(b1)  # should print three block data


b1.remove_block("Second")
b1.append(datetime.now(), "Fourth")
# should print three block data after removing second and adding fourthhree block data after removing second and adding fourth


def test_block_chain2(block_chain):
    if block_chain.num_of_element == 3:
        print("PASS")
    else:
        print("FAIL")


test_block_chain(b1)


b2 = BlockChain()

# should print empty because there is no block in b2 chain
def test_block_chain3(block_chain):
    if block_chain.num_of_element == 0:
        print("PASS")
    else:
        print("FAIL")


test_block_chain3(b2)

