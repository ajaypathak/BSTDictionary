import random
import timeit
from BST_Dictionary import BSTDictionary
import numpy

avl = BSTDictionary(True)
total_time = 0
totaltime = []

# insert 500000 random keys and values into the AVL tree
total_Elements=500
start_time = timeit.default_timer()
for i in range(total_Elements):
    key = random.randint(1, 1000000)
    value = f"value {i}"
    avl.addValue(key, value)
end_time = timeit.default_timer()
total_time += (end_time - start_time)*1000

print(f"Total Element :{len(avl.keys())}. Time Taken for Dictionary Creation {total_time}")

# retrieve a random key 1000 times and calculate the average access time

for i in range(5):
    try:
        key = random.randint(1, 1000000)
        start_time = timeit.default_timer()
        value = avl.search(key)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)*1000
        totaltime.append(round(total_time, 6))
    except KeyError as ke:
        continue

avg_time = total_time / 1000

print(f"Average access time: {avg_time:.10f} milliseconds")
# print(totaltime)

random_list = [random.randint(1, 1000000) for _ in range(50000)]
random_list.sort()


total_time = 0
totaltime = []
bstTree = BSTDictionary(True)
start_time = timeit.default_timer()
for num in random_list:
    key=num
    value="value {num}"
    bstTree.addValue(key,value)
end_time = timeit.default_timer()
total_time += (end_time - start_time)*1000
print(f"Total Element :{len(bstTree.keys())}. Time Taken for Sorted Dictionary Creation {total_time}")

for i in range(1000):
    try:
        key = random.randint(1, 1000000)
        start_time = timeit.default_timer()
        value = avl.search(key)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)*1000
        totaltime.append(round(total_time, 6))
    except KeyError as ke:
        continue

avg_time = total_time / 1000

print(f"Average access time: {avg_time:.10f} milliseconds")