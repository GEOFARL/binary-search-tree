import sys
from tree import BST

input_file = sys.argv[1]
sum_number = int(sys.argv[2])
program_name = sys.argv[0][:-3]

with open(input_file) as f:
    A = [int(i) for i in f.readline().split()]

print(A)
print(sum_number)


bst = BST()
bst.build_from_array(A)
bst.printTree()
paths = bst.find_all_monotonic_paths(sum_number)

with open(f"{program_name}_output.txt", mode="w") as f:
    for i in range(len(paths)):
        for j in range(len(paths[i])):
            f.write(f'{paths[i][j]} ')
        if i != len(paths) - 1:
            f.write('\n')
