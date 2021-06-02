class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def search(self, value):
        # head = self.head
        # if head.value == value:
        #     return head
        if self.head is None:
            return None
        head = self.head
        while head:
            if head.value == value:
                return head
            head = head.next
        return None

    def remove(self, value):
        if self.head is None:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        raise ValueError("Value not found in the list.")

    def to_list(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list


def union(llist_1, llist_2):
    # linked_list_to_check = LinkedList()
    # head = llist_1.head
    # while head.next:
    #     head = head.next
    #     linked_list_to_check.append(head.value)

    head = llist_2.head
    while head.next:
        head = head.next
        if  not llist_1.search(head.value):
            llist_1.append(head.value)

    return llist_1


def intersection(llist_1, llist_2):
    temp_list = LinkedList()
    head = llist_1.head

    while head.next:
        if llist_2.search(head.value):
            temp_list.append(head.value)
        head = head.next

    return temp_list


def test_union_function(test_case):
    link1 = test_case[0]
    link2 = test_case[1]
    link1_list = link1.to_list()
    link2_list = link2.to_list()
    result = union(link1, link2)

    test_result = list(set(link1_list) | set(link2_list))
    if test_result.sort() == result.to_list().sort():
        print("PASS")

    else:
        print("FAIL")


def test_intersection_function(test_case):
    link1 = test_case[0]
    link2 = test_case[1]
    link1_list = link1.to_list()
    link2_list = link2.to_list()
    result = intersection(link1, link2)

    test_result = list(set(link1_list) & set(link2_list))
    if test_result.sort() == result.to_list().sort():
        print("PASS")

    else:
        print("FAIL")


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# (union(linked_list_1, linked_list_2))
(test_intersection_function([linked_list_1, linked_list_2]))
test_union_function([linked_list_1, linked_list_2])

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

(test_union_function([linked_list_3, linked_list_4]))
(test_intersection_function([linked_list_3, linked_list_4]))
