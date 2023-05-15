class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def build_from_array(self, arr):
        sorted_arr = sorted([i for i in arr if i != 0], reverse=True)
        print(sorted_arr)
        self.root = self.reconstruct_tree(arr)
        self.inorder_traversal(self.root, sorted_arr)

    def reconstruct_tree(self, preorder):
        if not preorder:
            return None

        value = preorder.pop(0)
        if value == 0:
            return None

        node = Node(value)
        node.left = self.reconstruct_tree(preorder)
        node.right = self.reconstruct_tree(preorder)

        return node

    def inorder_traversal(self, node, sorted):
        if node:
            self.inorder_traversal(node.left, sorted)
            node.value = sorted.pop()
            self.inorder_traversal(node.right, sorted)

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

    def find_monotonic_paths(self, node, target_sum, current_path, current_sum, result, visited):
        if node is None:
            return

        current_path.append(node.value)
        current_sum += node.value

        if current_sum == target_sum:
            path_tuple = tuple(current_path)
            if path_tuple not in visited:
                result.append(current_path[:])
                visited.add(path_tuple)

        self.find_monotonic_paths(node.left, target_sum,
                                  current_path, current_sum, result, visited)
        self.find_monotonic_paths(node.right, target_sum,
                                  current_path, current_sum, result, visited)

        current_path.pop()
        current_sum -= node.value

        self.find_monotonic_paths(
            node.left, target_sum, [], 0, result, visited)
        self.find_monotonic_paths(
            node.right, target_sum, [], 0, result, visited)

    def find_all_monotonic_paths(self, target_sum):
        result = []
        visited = set()
        self.find_monotonic_paths(
            self.root, target_sum, [], 0, result, visited)
        return result
