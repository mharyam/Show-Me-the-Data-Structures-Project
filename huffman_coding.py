# A Huffman Tree Node
import sys


class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (charecter)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''


def print_nodes(node, val=''):
    # huffman code for current node
    new_val = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)

    if node.right:
        print_nodes(node.right, new_val)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


def huffman_encoding(data):
    data_dict = dict()

    for _ in data:
        if _ != ' ':
            data_dict[_] = data_dict.get(_, 0) + 1

    chars = [char for char in data_dict.keys()]

    # frequency of characters
    freq = [freq for freq in data_dict.values()]

    # list containing unused nodes
    nodes = []

    for x in range(len(chars)):
        nodes.append(Node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        # remove the 2 nodes and add their
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    print_nodes(nodes[0])


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))