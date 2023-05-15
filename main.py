import sys

input_file = sys.argv[1]
number = int(sys.argv[2])

with open(input_file) as f:
    A = [int(i) for i in f.readline().split()]

print(A)
print(number)