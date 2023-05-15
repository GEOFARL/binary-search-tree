class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def build_from_array(self, arr):
        sorted_arr = sorted(arr)
        for value in sorted_arr:
            if value != 0:
                self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def printTree(self):
        self._pretty_print(self.root, '', True)

    def _pretty_print(self, node, prefix, is_left):
        if node.right is not None:
            self._pretty_print(node.right, prefix +
                               ("|   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left is not None:
            self._pretty_print(node.left, prefix +
                               ("    " if is_left else "|   "), True)
