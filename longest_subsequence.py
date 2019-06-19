import time

orig1 = time.time()
def longest_subsequence(arr, order="ASC"):
    if not arr:
        return 0
    lenar = len(arr)
    cache = [1] * lenar
    for i in range(1, lenar):
        for j in range(i):
            if order == "ASC":
                if arr[i] > arr[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
            else:
                if arr[i] < arr[j]:
                    cache[i] = max(cache[i], cache[j] + 1)
    print(cache)
    return max(cache)

#arr=[9,8,4,12,2,10,6,14,1,9,5,13,11,7,15]
#print(longest_subsequence(arr, "DESC"))
#arr=[0,2,4,3,8,14,12,6,3,1,9]
#print(longest_subsequence(arr))
timenow = time.time()
print(timenow-orig1)
