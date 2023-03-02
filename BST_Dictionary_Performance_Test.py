import random
import timeit
from BSTDictionary import BST_Dictionary
import numpy

avl = BST_Dictionary()

# insert 50000 random keys and values into the AVL tree

for i in range(50000):
     try:
          key = random.randint(1, 1000000)
          value = f"value {i}"
          avl.insert(key, value)
     except KeyError:
        continue
print(f"Total Element :{len(avl.keys())}")
# retrieve a random key 1000 times and calculate the average access time
total_time = 0
totaltime=[]
for i in range(1000):
    key = random.randint(1, 1000000)
    start_time = timeit.default_timer()
    value = avl.search(key)
    end_time = timeit.default_timer()
    total_time += (end_time - start_time)*1000
    totaltime.append(round(total_time,6))
avg_time = total_time / 1000

print(f"Average access time: {avg_time:.10f} milliseconds")
#print(totaltime)
