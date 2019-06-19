import time
from collections import Counter

orig1 = time.time()

# Algorithm 1 
# --------------
def topKFrequent(nums):
    k = Counter(nums)
    return k

nlist=[1,1,1,2,2,4,2,4,6,6,2,4,1,5,5,5,5]
res = topKFrequent(nlist)
res_sorted = sorted(res.items(), key=lambda pair: pair[1], reverse=True)
print(res_sorted)
for k,v in res_sorted:
   if v == 4:
      print(k)

elap1 = time.time() - orig1
print(elap1)

# Algorithm 2 (improved version without using Counter)
# --------------
orig2 = time.time()
dict={}
for elem in nlist:
   if elem not in dict:
       dict[elem] = 1
   else:
       dict[elem] += 1

res_sorted = sorted(dict.items(), key=lambda pair: pair[1], reverse=True)
print(res_sorted)
for k,v in res_sorted:
   if v == 4:
      print(k)

elap2 = time.time() - orig2
print(elap2)
