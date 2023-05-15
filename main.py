import sys
from tree import BST

input_file = sys.argv[1]
sum_number = int(sys.argv[2])

with open(input_file) as f:
    A = [int(i) for i in f.readline().split()]

print(A)
print(sum_number)

bst = BST()
bst.build_from_array(A)
bst.printTree()
